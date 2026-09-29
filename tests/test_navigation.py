"""UI navigation regression tests — run with `python3 tests/test_navigation.py` or pytest.

These cover every screen transition that does NOT need a database, so they run
anywhere with only the repo requirements installed. AppTest runs the real app
script in-process; dummy Supabase credentials are injected via AppTest.secrets
because the client is created lazily and never called on these screens.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from streamlit.testing.v1 import AppTest

APP = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app.py")

# app.py imports the voice/face pipelines at module level; skip cleanly if the
# heavy ML dependencies (resemblyzer/dlib) are not installed in this environment.
try:
    import resemblyzer  # noqa: F401
    import dlib  # noqa: F401

    _ML_DEPS_MISSING = False
except ModuleNotFoundError:
    _ML_DEPS_MISSING = True

pytestmark = pytest.mark.skipif(
    _ML_DEPS_MISSING, reason="voice/face ML dependencies not installed (see requirements.txt)"
)


def _app(login_type=None):
    at = AppTest.from_file(APP, default_timeout=60)
    at.secrets["SUPABASE_URL"] = "https://dummy.invalid"
    at.secrets["SUPABASE_PUBLISHABLE_KEY"] = "dummy"
    if login_type:
        at.session_state["login_type"] = login_type
    at.run()
    return at


def _btn(at, label):
    matches = [b for b in at.button if (b.label or "").strip() == label]
    assert matches, f"button {label!r} not found; buttons: {[b.label for b in at.button]}"
    return matches[0]


def test_home_screen_renders():
    at = _app()
    assert not at.exception
    _btn(at, "Student Portal")
    _btn(at, "Teacher Portal")


def test_home_to_teacher_portal():
    at = _app()
    _btn(at, "Teacher Portal").click().run()
    assert not at.exception
    assert at.session_state["login_type"] == "teacher"
    _btn(at, "Login")
    _btn(at, "Register Instead")


def test_home_to_student_portal():
    at = _app()
    _btn(at, "Student Portal").click().run()
    assert not at.exception
    assert at.session_state["login_type"] == "student"


def test_teacher_register_screen():
    at = _app("teacher")
    _btn(at, "Register Instead").click().run()
    assert not at.exception
    labels = [t.label for t in at.text_input]
    assert labels == ["Enter username", "Enter name", "Enter password", "Confirm your password"]


def test_back_to_home():
    at = _app("teacher")
    _btn(at, "Go back to Home").click().run()
    assert not at.exception
    assert at.session_state["login_type"] is None


def test_join_code_switches_to_student():
    at = AppTest.from_file(APP, default_timeout=60)
    at.secrets["SUPABASE_URL"] = "https://dummy.invalid"
    at.secrets["SUPABASE_PUBLISHABLE_KEY"] = "dummy"
    at.query_params["join-code"] = "CS101"
    at.run()
    assert not at.exception
    assert at.session_state["login_type"] == "student"


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  PASS {name}")
            except Exception as e:  # noqa: BLE001
                failures += 1
                print(f"  FAIL {name}: {e}")
    print("OK" if not failures else f"{failures} FAILURES")
    sys.exit(1 if failures else 0)
