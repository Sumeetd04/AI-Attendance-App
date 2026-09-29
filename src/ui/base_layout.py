"""Backwards-compatible layout API — all styling now lives in src/ui/theme.py."""

from src.ui.theme import (
    style_background_dashboard,
    style_background_home,
    style_base_layout,
)

__all__ = [
    "style_background_dashboard",
    "style_background_home",
    "style_base_layout",
]
