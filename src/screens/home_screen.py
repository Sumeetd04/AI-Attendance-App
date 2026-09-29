import streamlit as st

from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
from src.ui.theme import scroll_progress

STUDENT_MASCOT = "https://i.ibb.co/844D9Lrt/mascot-student.png"
TEACHER_MASCOT = "https://i.ibb.co/CsmQQV6X/mascot-prof.png"

STUDENT_FEATS = [
    "Join any class with a simple code",
    "One-time face & voice enrollment",
    "Track your attendance history",
]

TEACHER_FEATS = [
    "Create subjects & share QR codes",
    "Snap classroom photos — AI marks everyone",
    "Instant records for every session",
]

FEATURES = [
    ("🧠", "Face Recognition", "dlib-powered, 128-D embeddings"),
    ("🎙️", "Voice ID", "Speaker verification per student"),
    ("⚡", "Seconds, not minutes", "A whole class in one snapshot"),
    ("🔐", "Privacy-first", "Embeddings only — no raw photos"),
]

STEPS = [
    ("Enroll once", "Students register their face or voice in seconds."),
    ("Snap or record", "Teachers capture one classroom photo or a short clip."),
    ("Attendance done", "SnapClass matches every student and logs it instantly."),
]


def home_screen():

    style_base_layout()
    style_background_home()
    scroll_progress()

    header_home()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        feats = "".join(f"<li>{f}</li>" for f in STUDENT_FEATS)
        st.markdown(
            f"""
            <div class="snap-portal snap-portal-cyan snap-tilt snap-reveal">
                <img class="snap-portal-mascot" src="{STUDENT_MASCOT}" alt="Student mascot" />
                <h3>I'm a Student</h3>
                <p class="snap-portal-desc">Get recognized — no roll calls, no waiting.</p>
                <ul class="snap-portal-feats">{feats}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        feats = "".join(f"<li>{f}</li>" for f in TEACHER_FEATS)
        st.markdown(
            f"""
            <div class="snap-portal snap-portal-pink snap-tilt snap-reveal snap-reveal-1">
                <img class="snap-portal-mascot" src="{TEACHER_MASCOT}" alt="Teacher mascot" />
                <h3>I'm a Teacher</h3>
                <p class="snap-portal-desc">Run your classroom on autopilot.</p>
                <ul class="snap-portal-feats">{feats}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    features_html = "".join(
        f"""
        <div class="snap-feature snap-reveal{' snap-reveal-1' if i == 1 else ''}{' snap-reveal-2' if i == 2 else ''}">
            <div class="snap-feature-ico">{icon}</div>
            <div class="snap-feature-t"><b>{title}</b><small>{sub}</small></div>
        </div>
        """
        for i, (icon, title, sub) in enumerate(FEATURES)
    )
    st.markdown(f'<div class="snap-features">{features_html}</div>', unsafe_allow_html=True)

    steps_html = "".join(
        f"""
        <div class="snap-step snap-reveal{' snap-reveal-1' if i == 1 else ''}{' snap-reveal-2' if i == 2 else ''}">
            <div class="snap-step-num">{i + 1}</div>
            <b>{title}</b>
            <p>{text}</p>
        </div>
        """
        for i, (title, text) in enumerate(STEPS)
    )
    st.markdown(
        f'<div class="snap-steps-title">How it works</div><div class="snap-steps">{steps_html}</div>',
        unsafe_allow_html=True,
    )

    footer_home()
