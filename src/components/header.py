import streamlit as st

LOGO_URL = "https://i.ibb.co/YTYGn5qV/logo.png"


def header_home():
    """Landing-page hero: orbiting 3D rings around the logo, animated wordmark."""

    st.markdown(
        f"""
        <div class="snap-hero">
            <div class="snap-hero-badge"><span class="snap-pulse"></span> AI-POWERED ATTENDANCE</div>

            <div class="snap-logo-stage">
                <div class="snap-orbit"></div>
                <div class="snap-orbit snap-orbit-2"></div>
                <img class="snap-logo" src="{LOGO_URL}" alt="SnapClass logo" />
            </div>

            <h1 class="snap-hero-title">Snap<span>Class</span></h1>
            <p class="snap-hero-sub">
                Roll call in seconds — students are marked present by their
                <b>face</b> or <b>voice</b>, not by paperwork.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def header_dashboard():
    """Compact logo lockup for dashboards and auth screens (styles in theme.py)."""

    st.markdown(
        f"""
        <div class="snap-lockup snap-in">
            <img src="{LOGO_URL}" alt="SnapClass logo" />
            <div class="snap-lockup-t">SnapClass<span>AI Attendance</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
