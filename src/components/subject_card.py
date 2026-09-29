import streamlit as st

from src.ui.theme import progress_bar


def subject_card(
    name,
    code,
    section,
    stats=None,
    footer_callback=None,
    icon="📘",
    footer_kind="brand",
    progress=None,
):
    """Glass 3D subject card.

    - stats: list of (icon, label, value) tuples
    - footer_callback: optional callback rendered below the card (e.g. a button)
    - footer_kind: "brand" | "danger" — tints the footer button accordingly
    - progress: optional (attended, total) tuple → animated progress bar
    """

    stats_html = ""
    if stats:
        pills = "".join(
            f'<span class="snap-stat">{icon_} <b>{value}</b> {label}</span>'
            for icon_, label, value in stats
        )
        stats_html = f'<div class="snap-stats">{pills}</div>'

    progress_html = ""
    if progress is not None:
        attended, total = progress
        progress_html = progress_bar(attended, total)

    st.markdown(
        f"""
        <div class="snap-card snap-tilt snap-reveal" data-snap-footer="{footer_kind}">
            <span class="snap-card-accent"></span>
            <div class="snap-card-head">
                <div class="snap-card-ico">{icon}</div>
                <div class="snap-card-t">
                    <h3>{name}</h3>
                    <div class="snap-card-meta">Section {section}</div>
                </div>
                <span class="snap-code-chip">{code}</span>
            </div>
            {stats_html}
            {progress_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

    if footer_callback:
        footer_callback()
