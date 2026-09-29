import streamlit as st


def _footer() -> None:
    st.markdown(
        """
        <div class="snap-footer snap-reveal">
            <div class="snap-footer-mark">SC</div>
            <p><b>SnapClass</b> — attendance powered by faces &amp; voices</p>
            <p class="snap-footer-dim">© 2026 SnapClass · Built with Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_home():
    _footer()


def footer_dashboard():
    _footer()
