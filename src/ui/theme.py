"""
SnapClass design system — "Aurora Glass 3D".

Central place for all presentation code: global theme CSS, the animated 3D
background scene, scroll-driven effects and reusable HTML component builders.

Pure CSS/HTML (no injected JavaScript) so nothing can ever interfere with
Streamlit's event handling — every effect degrades gracefully in browsers
that lack a feature.
"""

import streamlit as st

# --------------------------------------------------------------------------- #
#  Fonts + design tokens                                                      #
# --------------------------------------------------------------------------- #

_FONTS = (
    "@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700"
    "&family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap');"
)

# --------------------------------------------------------------------------- #
#  Global stylesheet (applied on every screen)                                #
# --------------------------------------------------------------------------- #

_BASE_CSS = """
/* ------------------------------------------------------------------ tokens */
:root {
    --snap-bg: #060913;
    --snap-bg-2: #0b1128;
    --snap-ink: #e9ecfb;
    --snap-muted: #9aa3c7;
    --snap-brand: #5865f2;
    --snap-brand-2: #8b96ff;
    --snap-violet: #8a5cff;
    --snap-pink: #eb459e;
    --snap-pink-2: #ff7ac8;
    --snap-cyan: #38e1ff;
    --snap-green: #34d8a8;
    --snap-glass: rgba(139, 150, 255, 0.055);
    --snap-glass-2: rgba(139, 150, 255, 0.10);
    --snap-stroke: rgba(139, 150, 255, 0.16);
    --snap-stroke-2: rgba(139, 150, 255, 0.32);
    --snap-font-display: 'Space Grotesk', 'Outfit', sans-serif;
    --snap-font-body: 'Outfit', sans-serif;
    --snap-font-mono: 'JetBrains Mono', monospace;
}
.stApp { background: var(--snap-bg); }

/* --------------------------------------------------------------- app chrome */
div[data-testid="stAppViewContainer"],
section[data-testid="stMain"] {
    background: transparent !important;
}

#MainMenu, header[data-testid="stHeader"], footer,
div[data-testid="stToolbar"], div[data-testid="stStatusWidget"] {
    display: none !important;
}

div[data-testid="stMainBlockContainer"].block-container {
    position: relative;
    z-index: 1;
    background: transparent;
    max-width: 1150px;
    margin: 0 auto;
    padding-top: 2.2rem;
    padding-bottom: 5rem;
}

@media (max-width: 640px) {
    div[data-testid="stMainBlockContainer"].block-container {
        padding: 1.4rem 1rem 4rem;
    }
}

/* --------------------------------------------------------------- scrollbar */
section[data-testid="stMain"] {
    scroll-behavior: smooth;
    scrollbar-width: thin;
    scrollbar-color: rgba(88, 101, 242, 0.55) transparent;
}
section[data-testid="stMain"]::-webkit-scrollbar { width: 10px; }
section[data-testid="stMain"]::-webkit-scrollbar-track { background: transparent; }
section[data-testid="stMain"]::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, rgba(88,101,242,.75), rgba(235,69,158,.75));
    border-radius: 99px;
    border: 3px solid var(--snap-bg);
}

::selection { background: rgba(88, 101, 242, 0.45); color: #fff; }

/* -------------------------------------------------------------- typography */
.stApp, .stApp p, .stApp span, .stApp li, .stApp label {
    font-family: var(--snap-font-body);
}
.stApp h1, .stApp h2, .stApp h3, .stApp h4 {
    font-family: var(--snap-font-display);
    color: var(--snap-ink);
    letter-spacing: -0.015em;
}
div[data-testid="stMarkdownContainer"] p { color: #c7cdea; line-height: 1.65; }
div[data-testid="stMarkdownContainer"] a {
    color: var(--snap-brand-2);
    text-decoration: none;
    border-bottom: 1px dashed rgba(139,150,255,.5);
}
div[data-testid="stMarkdownContainer"] a:hover { color: #ffffff; }
div[data-testid="stMarkdownContainer"] strong { color: #ffffff; }

/* ------------------------------------------------------------------ buttons */
div[data-testid="stButton"] > button {
    font-family: var(--snap-font-body) !important;
    font-weight: 600;
    font-size: 0.95rem;
    letter-spacing: 0.02em;
    border-radius: 14px !important;
    border: 1px solid transparent;
    padding: 0.6em 1.4em;
    transition: transform 0.24s cubic-bezier(0.2, 0.7, 0.3, 1.35),
                box-shadow 0.25s ease, background 0.25s ease,
                border-color 0.25s ease, filter 0.25s ease, color 0.2s ease;
    will-change: transform;
    overflow: hidden;
}
div[data-testid="stButton"] > button:hover:not(:disabled) { transform: translateY(-2px); }
div[data-testid="stButton"] > button:active:not(:disabled) { transform: translateY(1px) scale(0.985); }
div[data-testid="stButton"] > button:disabled { opacity: 0.38; }
div[data-testid="stButton"] > button:focus-visible {
    outline: 2px solid var(--snap-cyan) !important;
    outline-offset: 2px !important;
}

div[data-testid="stButton"] > button[kind="primary"] {
    color: #ffffff;
    background: linear-gradient(135deg, #6d7bff 0%, #5865f2 45%, #7c5cff 110%);
    background-size: 170% 170%;
    box-shadow: 0 10px 30px -10px rgba(88, 101, 242, 0.65),
                inset 0 1px 0 rgba(255, 255, 255, 0.28);
}
div[data-testid="stButton"] > button[kind="primary"]:hover:not(:disabled) {
    background-position: 30% 50%;
    box-shadow: 0 18px 44px -12px rgba(88, 101, 242, 0.85),
                inset 0 1px 0 rgba(255, 255, 255, 0.34);
    filter: saturate(1.12);
}

div[data-testid="stButton"] > button[kind="secondary"] {
    color: #dde3ff;
    background: linear-gradient(180deg, rgba(139,150,255,0.16), rgba(139,150,255,0.06));
    border-color: rgba(139, 150, 255, 0.38);
    backdrop-filter: blur(6px);
    box-shadow: 0 8px 26px -16px rgba(0, 0, 0, 0.9),
                inset 0 1px 0 rgba(255, 255, 255, 0.07);
}
div[data-testid="stButton"] > button[kind="secondary"]:hover:not(:disabled) {
    border-color: rgba(139, 150, 255, 0.7);
    background: linear-gradient(180deg, rgba(139,150,255,0.24), rgba(139,150,255,0.10));
    box-shadow: 0 14px 34px -16px rgba(88, 101, 242, 0.7),
                inset 0 1px 0 rgba(255, 255, 255, 0.10);
}

div[data-testid="stButton"] > button[kind="tertiary"] {
    color: var(--snap-muted);
    background: rgba(154, 163, 199, 0.05);
    border-color: rgba(154, 163, 199, 0.17);
}
div[data-testid="stButton"] > button[kind="tertiary"]:hover:not(:disabled) {
    color: #ffffff;
    border-color: rgba(154, 163, 199, 0.42);
    background: rgba(154, 163, 199, 0.10);
}

/* ------------------------------------------------------------------- inputs */
div[data-testid="stWidgetLabel"] p {
    color: var(--snap-muted) !important;
    font-weight: 500;
    font-size: 0.86rem;
    letter-spacing: 0.03em;
}

div[data-testid="stTextInput"] input,
div[data-testid="stSelectbox"] input {
    background: rgba(9, 14, 34, 0.72) !important;
    border: 1px solid rgba(139, 150, 255, 0.24) !important;
    border-radius: 13px !important;
    color: var(--snap-ink) !important;
    font-family: var(--snap-font-body) !important;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04);
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
    caret-color: var(--snap-brand-2);
}
div[data-testid="stTextInput"] input:hover,
div[data-testid="stSelectbox"] input:hover {
    border-color: rgba(139, 150, 255, 0.45) !important;
}
div[data-testid="stTextInput"] input:focus,
div[data-testid="stSelectbox"] input:focus {
    border-color: var(--snap-brand-2) !important;
    box-shadow: 0 0 0 4px rgba(88, 101, 242, 0.16),
                0 10px 30px -14px rgba(88, 101, 242, 0.6) !important;
}
div[data-testid="stTextInput"] input::placeholder,
div[data-testid="stSelectbox"] input::placeholder { color: #525b7f !important; }
div[data-testid="stTextInput"] svg { color: var(--snap-muted) !important; }

/* selectbox dropdown (portaled to body) */
div[data-testid="stSelectboxVirtualDropdown"] {
    background: rgba(12, 17, 40, 0.96) !important;
    border: 1px solid var(--snap-stroke-2);
    border-radius: 14px !important;
    box-shadow: 0 30px 70px -16px rgba(0, 0, 0, 0.85),
                0 0 0 1px rgba(88, 101, 242, 0.10);
    backdrop-filter: blur(16px);
    overflow: hidden;
}
div[data-testid="stSelectboxVirtualDropdown"] [data-item-hl] { border-radius: 9px; }
div[data-testid="stSelectboxVirtualDropdown"] [data-hovered] [data-item-hl],
div[data-testid="stSelectboxVirtualDropdown"] [data-focused] [data-item-hl] {
    background: rgba(88, 101, 242, 0.24);
}
div[data-testid="stSelectboxVirtualDropdown"] [data-disabled] { opacity: 0.4; }

/* file uploader */
div[data-testid="stFileUploaderDropzone"] {
    background: rgba(9, 14, 34, 0.6) !important;
    border: 1px dashed rgba(139, 150, 255, 0.35) !important;
    border-radius: 15px !important;
    color: var(--snap-muted) !important;
    transition: border-color 0.25s ease, background 0.25s ease;
}
div[data-testid="stFileUploaderDropzone"]:hover {
    border-color: rgba(139, 150, 255, 0.7) !important;
    background: rgba(88, 101, 242, 0.08) !important;
}
div[data-testid="stFileUploaderDropzone"] button {
    background: rgba(88, 101, 242, 0.2) !important;
    border: 1px solid rgba(139, 150, 255, 0.4) !important;
    color: #dde3ff !important;
    border-radius: 10px !important;
}

/* camera input — glass frame + scanning line */
div[data-testid="stCameraInput"] {
    border-radius: 20px;
}
div[data-testid="stCameraInputWebcamStyledBox"] {
    position: relative;
    border-radius: 20px !important;
    border: 1px solid rgba(56, 225, 255, 0.28) !important;
    box-shadow: 0 0 0 5px rgba(56, 225, 255, 0.05),
                0 26px 60px -30px rgba(56, 225, 255, 0.4);
    overflow: hidden;
}
div[data-testid="stCameraInputWebcamStyledBox"]::after {
    content: "";
    position: absolute;
    left: 5%;
    right: 5%;
    height: 2px;
    top: 8%;
    background: linear-gradient(90deg, transparent, rgba(56, 225, 255, 0.95), transparent);
    box-shadow: 0 0 16px 3px rgba(56, 225, 255, 0.45);
    animation: snapScan 3.4s ease-in-out infinite;
    pointer-events: none;
    opacity: 0.85;
    z-index: 2;
}
div[data-testid="stCameraInputButton"] {
    background: rgba(9, 14, 34, 0.7) !important;
    border: 1px solid rgba(56, 225, 255, 0.4) !important;
    color: #bfefff !important;
    border-radius: 13px !important;
    backdrop-filter: blur(6px);
}

/* audio input */
div[data-testid="stAudioInputActionButton"] {
    background: rgba(9, 14, 34, 0.7) !important;
    border: 1px solid rgba(235, 69, 158, 0.45) !important;
    color: #ffd0ea !important;
    border-radius: 13px !important;
    backdrop-filter: blur(6px);
}

/* ------------------------------------------------------------------- alerts */
div[data-testid="stAlert"], div[data-testid="stAlertContainer"] {
    border-radius: 14px !important;
    border: 1px solid rgba(139, 150, 255, 0.16);
    background: linear-gradient(180deg, rgba(139,150,255,0.09), rgba(139,150,255,0.035)) !important;
    backdrop-filter: blur(8px);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05),
                0 14px 36px -24px rgba(0, 0, 0, 0.9);
}

/* ------------------------------------------------------------------ dialogs */
div[data-testid="stDialog"] {
    background: rgba(3, 5, 14, 0.6) !important;
    backdrop-filter: blur(10px) saturate(1.3);
}
div[data-testid="stDialog"] > div {
    background: linear-gradient(180deg, rgba(21, 27, 60, 0.96), rgba(10, 14, 34, 0.97)) !important;
    border: 1px solid rgba(139, 150, 255, 0.22);
    border-radius: 22px !important;
    box-shadow: 0 44px 120px -24px rgba(0, 0, 0, 0.85),
                0 0 0 1px rgba(88, 101, 242, 0.08),
                inset 0 1px 0 rgba(255, 255, 255, 0.08);
    animation: snapDialogIn 0.5s cubic-bezier(0.18, 0.9, 0.32, 1.18) both;
    transform-origin: top center;
}

/* ------------------------------------------------------------------- toasts */
div[data-testid="stToast"] {
    background: rgba(15, 21, 48, 0.94) !important;
    border: 1px solid rgba(139, 150, 255, 0.3);
    border-radius: 14px !important;
    box-shadow: 0 24px 60px -18px rgba(0, 0, 0, 0.85),
                0 0 30px -8px rgba(88, 101, 242, 0.35);
    backdrop-filter: blur(12px);
    animation: snapToastIn 0.45s cubic-bezier(0.2, 0.9, 0.3, 1.3) both;
}
div[data-testid="stToast"] [data-testid="stToastText"] { color: var(--snap-ink) !important; }

/* ---------------------------------------------------------------- dataframe */
div[data-testid="stDataFrame"] {
    border: 1px solid var(--snap-stroke);
    border-radius: 16px;
    overflow: hidden;
    background: rgba(9, 14, 34, 0.55);
    box-shadow: 0 20px 50px -28px rgba(0, 0, 0, 0.9),
                inset 0 1px 0 rgba(255, 255, 255, 0.04);
    animation: snapFadeUp 0.55s cubic-bezier(0.2, 0.8, 0.3, 1) both;
}

/* -------------------------------------------------------------------- code */
div[data-testid="stCode"], div[data-testid="stCodeUnhighlighted"] {
    border-radius: 14px !important;
    border: 1px solid var(--snap-stroke);
}
div[data-testid="stMarkdownContainer"] pre,
div[data-testid="stMarkdownContainer"] code {
    font-family: var(--snap-font-mono) !important;
}

/* ------------------------------------------------------------------- images */
div[data-testid="stImageContainer"] {
    border-radius: 16px;
    border: 1px solid var(--snap-stroke);
    background: rgba(139, 150, 255, 0.04);
    padding: 6px;
    box-shadow: 0 18px 44px -28px rgba(0, 0, 0, 0.9);
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}
div[data-testid="stImageContainer"]:hover {
    transform: translateY(-3px);
    border-color: var(--snap-stroke-2);
    box-shadow: 0 24px 54px -24px rgba(88, 101, 242, 0.4);
}
div[data-testid="stImageCaption"] {
    color: var(--snap-muted);
    font-size: 0.84rem;
}

/* ------------------------------------------------------------------ divider */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, rgba(139,150,255,0.4) 22%, rgba(235,69,158,0.4) 78%, transparent) !important;
    margin: 2rem 0 !important;
    position: relative;
    overflow: visible;
}
hr::after {
    content: "";
    position: absolute;
    left: 50%;
    top: 50%;
    width: 42px;
    height: 3px;
    transform: translate(-50%, -50%);
    border-radius: 99px;
    background: linear-gradient(90deg, var(--snap-brand), var(--snap-pink));
    box-shadow: 0 0 14px rgba(88, 101, 242, 0.8);
}

/* --------------------------------------------------------------- exceptions */
div[data-testid="stException"] {
    border-radius: 14px;
    border: 1px solid rgba(255, 110, 150, 0.35);
    background: rgba(60, 12, 30, 0.55);
}

/* ------------------------------------------------------- keyframes library */
@keyframes snapFadeUp {
    from { opacity: 0; transform: translateY(26px); }
    to { opacity: 1; transform: none; }
}
@keyframes snapFadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
@keyframes snapPopIn {
    0% { opacity: 0; transform: scale(0.82) translateY(14px); }
    70% { opacity: 1; transform: scale(1.03) translateY(-2px); }
    100% { opacity: 1; transform: scale(1) translateY(0); }
}
@keyframes snapDialogIn {
    from { opacity: 0; transform: translateY(26px) scale(0.94); }
    to { opacity: 1; transform: none; }
}
@keyframes snapToastIn {
    from { opacity: 0; transform: translateY(-14px) scale(0.95); }
    to { opacity: 1; transform: none; }
}
@keyframes snapScan {
    0%, 100% { top: 7%; }
    50% { top: 91%; }
}
@keyframes snapBob {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-22px); }
}
@keyframes snapCubeSpin {
    from { transform: rotateX(-18deg) rotateY(0deg); }
    to { transform: rotateX(-18deg) rotateY(360deg); }
}
@keyframes snapOrbitSpin {
    from { transform: rotateX(74deg) rotateZ(0deg); }
    to { transform: rotateX(74deg) rotateZ(360deg); }
}
@keyframes snapOrbDriftA {
    from { transform: translate3d(0, 0, 0) scale(1); }
    to { transform: translate3d(9vw, 7vh, 0) scale(1.18); }
}
@keyframes snapOrbDriftB {
    from { transform: translate3d(0, 0, 0) scale(1.1); }
    to { transform: translate3d(-8vw, -6vh, 0) scale(0.94); }
}
@keyframes snapOrbDriftC {
    from { transform: translate3d(0, 0, 0) scale(0.95); }
    to { transform: translate3d(6vw, -8vh, 0) scale(1.15); }
}
@keyframes snapTwinkle {
    0%, 100% { opacity: 0.55; }
    50% { opacity: 1; }
}
@keyframes snapGridMove {
    from { background-position: 0 0; }
    to { background-position: 0 54px; }
}
@keyframes snapBarGrow {
    from { width: 0%; }
}
@keyframes snapBarFlow {
    from { background-position: 0% 0; }
    to { background-position: 200% 0; }
}
@keyframes snapPulseDot {
    0%, 100% { box-shadow: 0 0 0 0 rgba(52, 216, 168, 0.55); }
    60% { box-shadow: 0 0 0 9px rgba(52, 216, 168, 0); }
}
@keyframes snapShine {
    from { background-position: 0% 50%; }
    to { background-position: 200% 50%; }
}

/* ------------------------------------------------------------ 3D background */
.snap-scene {
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    overflow: hidden;
}
.snap-orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(85px);
    opacity: 0.5;
    mix-blend-mode: screen;
    will-change: transform;
}
.snap-orb-a {
    width: 46vw; height: 46vw; left: -12vw; top: -14vh;
    background: radial-gradient(circle at 32% 32%, rgba(88,101,242,0.6), rgba(88,101,242,0) 66%);
    animation: snapOrbDriftA 34s ease-in-out infinite alternate;
}
.snap-orb-b {
    width: 42vw; height: 42vw; right: -12vw; top: 24vh;
    background: radial-gradient(circle at 60% 40%, rgba(235,69,158,0.45), rgba(235,69,158,0) 66%);
    animation: snapOrbDriftB 40s ease-in-out infinite alternate;
}
.snap-orb-c {
    width: 36vw; height: 36vw; left: 30vw; bottom: -16vh;
    background: radial-gradient(circle, rgba(56,225,255,0.30), rgba(56,225,255,0) 62%);
    animation: snapOrbDriftC 46s ease-in-out infinite alternate;
}
.snap-stars {
    position: absolute;
    inset: 0;
    background-image:
        radial-gradient(1.6px 1.6px at 12% 22%, rgba(255,255,255,0.9) 50%, transparent 51%),
        radial-gradient(1.2px 1.2px at 28% 64%, rgba(255,255,255,0.7) 50%, transparent 51%),
        radial-gradient(1.8px 1.8px at 41% 12%, rgba(160,190,255,0.9) 50%, transparent 51%),
        radial-gradient(1.2px 1.2px at 55% 42%, rgba(255,255,255,0.65) 50%, transparent 51%),
        radial-gradient(1.6px 1.6px at 67% 18%, rgba(255,170,220,0.8) 50%, transparent 51%),
        radial-gradient(1.2px 1.2px at 74% 58%, rgba(255,255,255,0.7) 50%, transparent 51%),
        radial-gradient(1.8px 1.8px at 86% 28%, rgba(160,220,255,0.85) 50%, transparent 51%),
        radial-gradient(1.2px 1.2px at 92% 72%, rgba(255,255,255,0.6) 50%, transparent 51%),
        radial-gradient(1.4px 1.4px at 8% 78%, rgba(255,255,255,0.75) 50%, transparent 51%),
        radial-gradient(1.4px 1.4px at 36% 88%, rgba(200,180,255,0.7) 50%, transparent 51%),
        radial-gradient(1.2px 1.2px at 60% 82%, rgba(255,255,255,0.55) 50%, transparent 51%),
        radial-gradient(1.6px 1.6px at 80% 90%, rgba(255,200,235,0.65) 50%, transparent 51%);
    animation: snapTwinkle 7s ease-in-out infinite;
}
.snap-gridfloor {
    position: absolute;
    left: -42%;
    right: -42%;
    bottom: -12vh;
    height: 58vh;
    background-image:
        linear-gradient(rgba(124,139,255,0.35) 1px, transparent 1px),
        linear-gradient(90deg, rgba(124,139,255,0.35) 1px, transparent 1px);
    background-size: 54px 54px;
    transform: perspective(640px) rotateX(64deg);
    transform-origin: 50% 0;
    animation: snapGridMove 3.2s linear infinite;
    opacity: 0.16;
    -webkit-mask-image: linear-gradient(to bottom, transparent 0, #000 34%, #000 76%, transparent 100%);
    mask-image: linear-gradient(to bottom, transparent 0, #000 34%, #000 76%, transparent 100%);
}
.snap-float { position: absolute; perspective: 760px; animation: snapBob 9s ease-in-out infinite; }
.snap-float-a { left: 6.5%; top: 21vh; }
.snap-float-b { right: 8%; top: 33vh; animation-delay: -3.2s; }
.snap-float-c { right: 24%; bottom: 17vh; animation-delay: -6.4s; }
.snap-cube {
    --s: 72px;
    position: relative;
    width: var(--s);
    height: var(--s);
    transform-style: preserve-3d;
    animation: snapCubeSpin 30s linear infinite;
}
.snap-cube-sm { --s: 42px; }
.snap-cube i {
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(124,139,255,0.17), rgba(88,101,242,0.04));
    border: 1px solid rgba(139,150,255,0.42);
    box-shadow: inset 0 0 24px rgba(124,139,255,0.14);
}
.snap-cube i:nth-child(1) { transform: translateZ(calc(var(--s) / 2)); }
.snap-cube i:nth-child(2) { transform: rotateY(180deg) translateZ(calc(var(--s) / 2)); }
.snap-cube i:nth-child(3) { transform: rotateY(90deg) translateZ(calc(var(--s) / 2)); }
.snap-cube i:nth-child(4) { transform: rotateY(-90deg) translateZ(calc(var(--s) / 2)); }
.snap-cube i:nth-child(5) { transform: rotateX(90deg) translateZ(calc(var(--s) / 2)); }
.snap-cube i:nth-child(6) { transform: rotateX(-90deg) translateZ(calc(var(--s) / 2)); }
.snap-cube-pink i {
    background: linear-gradient(135deg, rgba(235,69,158,0.19), rgba(235,69,158,0.04));
    border-color: rgba(255,122,200,0.42);
    box-shadow: inset 0 0 24px rgba(235,69,158,0.14);
}
.snap-cube-cyan i {
    background: linear-gradient(135deg, rgba(56,225,255,0.16), rgba(56,225,255,0.03));
    border-color: rgba(56,225,255,0.4);
    box-shadow: inset 0 0 24px rgba(56,225,255,0.12);
}
.snap-vignette {
    position: absolute;
    inset: 0;
    background:
        radial-gradient(120% 90% at 50% 0%, rgba(88,101,242,0.10), transparent 55%),
        radial-gradient(140% 120% at 50% 55%, transparent 55%, rgba(3,5,12,0.75) 100%);
}
@media (max-width: 900px) {
    .snap-float-c { display: none; }
}
@media (max-width: 640px) {
    .snap-float { display: none; }
    .snap-gridfloor { opacity: 0.10; }
}

/* ------------------------------------------------------- reusable surfaces */
.snap-card, .snap-portal {
    position: relative;
    background: linear-gradient(165deg, rgba(148,163,255,0.088), rgba(148,163,255,0.028) 55%, rgba(235,69,158,0.05));
    border: 1px solid var(--snap-stroke);
    border-radius: 24px;
    padding: 1.55rem 1.65rem;
    backdrop-filter: blur(14px);
    box-shadow: 0 20px 54px -30px rgba(0, 0, 0, 0.9), inset 0 1px 0 rgba(255,255,255,0.07);
    overflow: hidden;
}
.snap-card-accent {
    position: absolute;
    top: 0; left: 9%; right: 9%;
    height: 2px;
    border-radius: 99px;
    background: linear-gradient(90deg, transparent, var(--snap-brand), var(--snap-pink), transparent);
    opacity: 0.8;
}

/* 3D tilt + glare sweep on hover (pure CSS, no JS) */
.snap-tilt {
    transition: transform 0.45s cubic-bezier(0.2, 0.7, 0.3, 1.25), box-shadow 0.4s ease, border-color 0.3s ease;
    transform-style: preserve-3d;
    will-change: transform;
}
.snap-tilt::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: inherit;
    background: linear-gradient(105deg, transparent 42%, rgba(255,255,255,0.09) 48%, rgba(255,255,255,0.22) 50%, rgba(255,255,255,0.09) 52%, transparent 58%);
    transform: translateX(-130%);
    transition: transform 0.9s ease;
    pointer-events: none;
    z-index: 3;
}
.snap-tilt:hover::after { transform: translateX(130%); }
.snap-tilt:hover {
    transform: perspective(1100px) rotateX(4.5deg) rotateY(-5deg) translateY(-8px) scale(1.015);
    box-shadow: 0 34px 74px -26px rgba(0, 0, 0, 0.9), 0 0 46px -12px rgba(88, 101, 242, 0.5);
    border-color: var(--snap-stroke-2);
}

/* section headers with 3D icon tile */
.snap-sec {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin: 0.4rem 0 1.4rem;
    animation: snapFadeUp 0.6s cubic-bezier(0.2, 0.8, 0.3, 1) both;
}
.snap-sec-ico {
    flex: 0 0 auto;
    width: 52px;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    border-radius: 16px;
    background: linear-gradient(145deg, rgba(88,101,242,0.30), rgba(235,69,158,0.18));
    border: 1px solid rgba(139,150,255,0.35);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.22), 0 12px 26px -12px rgba(88,101,242,0.65),
                0 3px 0 0 rgba(30,20,80,0.9);
    transform: perspective(600px) rotateX(12deg);
    transition: transform 0.35s cubic-bezier(0.2, 0.7, 0.3, 1.4);
}
.snap-sec:hover .snap-sec-ico { transform: perspective(600px) rotateX(0deg) rotate(-4deg) scale(1.06); }
.snap-sec-title {
    font-family: var(--snap-font-display);
    font-size: 1.62rem;
    font-weight: 700;
    color: var(--snap-ink);
    margin: 0;
    letter-spacing: -0.02em;
}
.snap-sec-sub { color: var(--snap-muted); margin: 0.15rem 0 0; font-size: 0.95rem; }

/* welcome banner */
.snap-welcome {
    font-family: var(--snap-font-display);
    font-size: 1.45rem;
    font-weight: 600;
    color: var(--snap-ink);
    animation: snapFadeUp 0.6s cubic-bezier(0.2, 0.8, 0.3, 1) both;
    margin-bottom: 0.7rem;
}
.snap-welcome b {
    background: linear-gradient(92deg, #8b96ff 10%, #ff7ac8 90%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
}
.snap-role {
    display: inline-flex;
    align-items: center;
    margin-left: 0.6em;
    font-size: 0.7rem;
    font-family: var(--snap-font-body);
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.32em 0.85em;
    border-radius: 99px;
    background: rgba(88, 101, 242, 0.16);
    border: 1px solid rgba(139, 150, 255, 0.32);
    color: #c9d0ff;
    vertical-align: middle;
    -webkit-text-fill-color: #c9d0ff;
}

/* dashboard logo lockup */
.snap-lockup {
    display: inline-flex;
    align-items: center;
    gap: 0.85rem;
}
.snap-lockup img {
    height: 52px;
    filter: drop-shadow(0 10px 22px rgba(88, 101, 242, 0.6));
    animation: snapBob 6.5s ease-in-out infinite;
}
.snap-lockup-t {
    font-family: var(--snap-font-display);
    font-size: 1.42rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: #f0f2ff;
    line-height: 1.1;
}
.snap-lockup-t span {
    display: block;
    font-family: var(--snap-font-body);
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.24em;
    text-transform: uppercase;
    background: linear-gradient(90deg, #8b96ff, #ff7ac8);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
    margin-top: 2px;
}

/* stats + chips */
.snap-stats { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.05rem; }
.snap-stat {
    display: inline-flex;
    align-items: center;
    gap: 0.45em;
    background: rgba(139, 150, 255, 0.09);
    border: 1px solid rgba(139, 150, 255, 0.17);
    padding: 0.34em 0.85em;
    border-radius: 999px;
    font-size: 0.87rem;
    color: var(--snap-muted);
}
.snap-stat b { color: var(--snap-ink); font-family: var(--snap-font-display); }

.snap-code-chip {
    font-family: var(--snap-font-mono);
    font-size: 0.8rem;
    letter-spacing: 0.06em;
    color: #cdd6ff;
    background: rgba(88, 101, 242, 0.16);
    border: 1px solid rgba(139, 150, 255, 0.35);
    border-radius: 9px;
    padding: 0.32em 0.7em;
    white-space: nowrap;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.08);
}

/* progress bar */
.snap-bar { margin-top: 1.1rem; }
.snap-bar-top {
    display: flex;
    justify-content: space-between;
    font-size: 0.78rem;
    color: var(--snap-muted);
    margin-bottom: 0.42rem;
    letter-spacing: 0.04em;
}
.snap-bar-track {
    position: relative;
    height: 8px;
    border-radius: 99px;
    background: rgba(139, 150, 255, 0.13);
    border: 1px solid rgba(139, 150, 255, 0.12);
    overflow: hidden;
}
.snap-bar-fill {
    height: 100%;
    border-radius: 99px;
    background: linear-gradient(90deg, #5865f2, #8a5cff, #eb459e, #5865f2);
    background-size: 200% 100%;
    animation: snapBarGrow 1.2s cubic-bezier(0.2, 0.8, 0.3, 1) both,
               snapBarFlow 3.6s linear 1.2s infinite;
    box-shadow: 0 0 14px rgba(88, 101, 242, 0.6);
}

/* scroll progress bar (sticky, scroll-driven, guarded by @supports) */
.snap-progress {
    position: sticky;
    top: 0;
    z-index: 40;
    height: 3px;
    margin: -0.6rem 0 0.9rem;
    pointer-events: none;
    display: none;
}
.snap-progress i {
    display: block;
    height: 100%;
    width: 100%;
    border-radius: 99px;
    background: linear-gradient(90deg, #5865f2, #8a5cff, #eb459e);
    transform-origin: 0 50%;
    transform: scaleX(0);
    box-shadow: 0 0 12px rgba(88, 101, 242, 0.8);
}

/* entrance helpers */
.snap-in { animation: snapFadeUp 0.65s cubic-bezier(0.2, 0.8, 0.3, 1) both; }
.snap-in-1 { animation: snapFadeUp 0.65s 0.08s cubic-bezier(0.2, 0.8, 0.3, 1) both; }
.snap-in-2 { animation: snapFadeUp 0.65s 0.16s cubic-bezier(0.2, 0.8, 0.3, 1) both; }
.snap-in-3 { animation: snapFadeUp 0.65s 0.24s cubic-bezier(0.2, 0.8, 0.3, 1) both; }
.snap-pop { animation: snapPopIn 0.6s cubic-bezier(0.2, 0.8, 0.3, 1.25) both; }

/* --------------------------------------------- scroll-driven reveal effects */
/* Progressive enhancement: browsers without scroll-driven animations simply
   show the content fully visible — nothing is ever hidden without support. */
@supports (animation-timeline: view()) {
    .snap-reveal {
        animation: snapReveal linear both;
        animation-timeline: view();
        animation-range: entry 0% entry 78%;
    }
    .snap-reveal-1 { animation-range: entry 0% entry 86%; }
    .snap-reveal-2 { animation-range: entry 0% entry 94%; }
    @keyframes snapReveal {
        from { opacity: 0; transform: translateY(46px) rotateX(9deg) scale(0.975); }
        to { opacity: 1; transform: none; }
    }
}
@supports (animation-timeline: scroll()) {
    .snap-progress { display: block; }
    .snap-progress i { animation: snapProgressGrow linear both; animation-timeline: scroll(nearest); }
    @keyframes snapProgressGrow {
        from { transform: scaleX(0); }
        to { transform: scaleX(1); }
    }
}

/* ------------------------------------------------------ accessibility: motion */
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
    .snap-tilt:hover { transform: none; }
    .snap-tilt::after { display: none; }
}
"""

# --------------------------------------------------------------------------- #
#  Home-screen specific CSS                                                   #
# --------------------------------------------------------------------------- #

_HOME_CSS = """
/* ------------------------------------------------------------------ hero */
.snap-hero {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 1.6rem 0 2.6rem;
}
.snap-hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.6em;
    font-size: 0.74rem;
    font-weight: 600;
    letter-spacing: 0.22em;
    color: #c9d2ff;
    background: rgba(88, 101, 242, 0.13);
    border: 1px solid rgba(139, 150, 255, 0.32);
    border-radius: 99px;
    padding: 0.5em 1.25em;
    backdrop-filter: blur(8px);
    animation: snapFadeUp 0.6s 0.05s cubic-bezier(0.2,0.8,0.3,1) both;
}
.snap-hero-badge .snap-pulse {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--snap-green);
    animation: snapPulseDot 2.2s ease-out infinite;
}
.snap-logo-stage {
    position: relative;
    width: 250px;
    height: 210px;
    margin: 1.6rem 0 0.6rem;
    perspective: 800px;
    animation: snapPopIn 0.9s 0.15s cubic-bezier(0.2, 0.8, 0.3, 1.2) both;
}
.snap-orbit {
    position: absolute;
    left: 50%;
    top: 58%;
    width: 225px;
    height: 225px;
    margin: -112.5px 0 0 -112.5px;
    border-radius: 50%;
    border: 1.5px dashed rgba(139, 150, 255, 0.45);
    animation: snapOrbitSpin 15s linear infinite;
}
.snap-orbit-2 {
    width: 285px;
    height: 285px;
    margin: -142.5px 0 0 -142.5px;
    border-color: rgba(235, 69, 158, 0.25);
    border-style: dotted;
    animation-duration: 26s;
    animation-direction: reverse;
}
.snap-orbit::before {
    content: "";
    position: absolute;
    top: -5px;
    left: 50%;
    width: 9px;
    height: 9px;
    margin-left: -4.5px;
    border-radius: 50%;
    background: #8b96ff;
    box-shadow: 0 0 14px 3px rgba(139, 150, 255, 0.8);
}
.snap-logo {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -54%);
    height: 118px;
    filter: drop-shadow(0 18px 30px rgba(88, 101, 242, 0.55));
    animation: snapBob 6s ease-in-out infinite;
}
.snap-hero-title {
    font-family: var(--snap-font-display);
    font-size: clamp(3rem, 7.5vw, 4.6rem);
    font-weight: 700;
    letter-spacing: -0.035em;
    line-height: 1.02;
    margin: 0;
    color: #f4f6ff;
    animation: snapFadeUp 0.7s 0.25s cubic-bezier(0.2, 0.8, 0.3, 1) both;
}
.snap-hero-title span {
    background: linear-gradient(93deg, #6d7bff, #8a5cff 35%, #eb459e 75%, #ff7ac8);
    background-size: 200% auto;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
    animation: snapShine 5s linear infinite;
    filter: drop-shadow(0 10px 26px rgba(235, 69, 158, 0.35));
}
.snap-hero-sub {
    color: var(--snap-muted);
    font-size: 1.08rem;
    max-width: 540px;
    margin: 0.85rem 0 0;
    animation: snapFadeUp 0.7s 0.35s cubic-bezier(0.2, 0.8, 0.3, 1) both;
}
.snap-hero-sub b { color: #dfe5ff; font-weight: 600; }

/* ---------------------------------------------------------- portal cards */
.snap-portal { text-align: center; padding: 2.1rem 1.8rem 1.8rem; }
.snap-portal-cyan {
    background: linear-gradient(165deg, rgba(56,225,255,0.09), rgba(139,150,255,0.03) 55%, rgba(88,101,242,0.07));
}
.snap-portal-pink {
    background: linear-gradient(165deg, rgba(235,69,158,0.10), rgba(139,150,255,0.03) 55%, rgba(124,92,255,0.08));
}
.snap-portal-mascot {
    height: 128px;
    object-fit: contain;
    filter: drop-shadow(0 16px 26px rgba(0, 0, 0, 0.55));
    animation: snapBob 5.5s ease-in-out infinite;
    transition: transform 0.35s cubic-bezier(0.2, 0.7, 0.3, 1.4);
}
.snap-portal:hover .snap-portal-mascot { transform: scale(1.08) rotate(-2deg); }
.snap-portal h3 {
    font-family: var(--snap-font-display);
    font-size: 1.5rem;
    font-weight: 700;
    margin: 1rem 0 0.3rem;
    color: var(--snap-ink);
}
.snap-portal-desc { color: var(--snap-muted); font-size: 0.96rem; margin: 0 0 1.1rem; }
.snap-portal-feats {
    list-style: none;
    padding: 0;
    margin: 0 auto;
    max-width: 300px;
    text-align: left;
    display: flex;
    flex-direction: column;
    gap: 0.55rem;
}
.snap-portal-feats li {
    display: flex;
    align-items: center;
    gap: 0.65em;
    font-size: 0.92rem;
    color: #c3cae8;
}
.snap-portal-feats li::before {
    content: "✦";
    color: var(--snap-brand-2);
    font-size: 0.8em;
    flex: 0 0 auto;
}

/* --------------------------------------------------------- feature strip */
.snap-features {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.9rem;
    margin: 2.6rem 0 0.6rem;
}
.snap-feature {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    background: linear-gradient(165deg, rgba(148,163,255,0.08), rgba(148,163,255,0.02));
    border: 1px solid var(--snap-stroke);
    border-radius: 18px;
    padding: 0.85rem 1.25rem;
    backdrop-filter: blur(10px);
    box-shadow: 0 16px 40px -28px rgba(0,0,0,0.9), inset 0 1px 0 rgba(255,255,255,0.06);
    transition: transform 0.35s cubic-bezier(0.2, 0.7, 0.3, 1.3), border-color 0.3s ease, box-shadow 0.3s ease;
}
.snap-feature:hover {
    transform: translateY(-4px);
    border-color: var(--snap-stroke-2);
    box-shadow: 0 24px 48px -24px rgba(88,101,242,0.5);
}
.snap-feature-ico {
    width: 42px;
    height: 42px;
    flex: 0 0 auto;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.25rem;
    border-radius: 13px;
    background: linear-gradient(145deg, rgba(88,101,242,0.28), rgba(235,69,158,0.16));
    border: 1px solid rgba(139,150,255,0.32);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.2), 0 8px 18px -10px rgba(88,101,242,0.7);
    transform: perspective(500px) rotateX(14deg);
}
.snap-feature-t { text-align: left; }
.snap-feature-t b {
    display: block;
    font-family: var(--snap-font-display);
    font-size: 0.98rem;
    color: var(--snap-ink);
}
.snap-feature-t small { color: var(--snap-muted); font-size: 0.8rem; }

/* ------------------------------------------------------------ how it works */
.snap-steps-title {
    text-align: center;
    font-family: var(--snap-font-display);
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--snap-ink);
    margin: 3rem 0 1.8rem;
    letter-spacing: -0.02em;
}
.snap-steps {
    display: flex;
    gap: 1.1rem;
    align-items: stretch;
}
.snap-step {
    flex: 1 1 0;
    position: relative;
    text-align: center;
    background: linear-gradient(170deg, rgba(148,163,255,0.07), rgba(148,163,255,0.015));
    border: 1px solid var(--snap-stroke);
    border-radius: 20px;
    padding: 1.7rem 1.2rem 1.4rem;
    backdrop-filter: blur(10px);
    box-shadow: 0 18px 44px -30px rgba(0,0,0,0.9);
    transition: transform 0.35s cubic-bezier(0.2, 0.7, 0.3, 1.3), border-color 0.3s ease;
}
.snap-step:hover { transform: translateY(-6px); border-color: var(--snap-stroke-2); }
.snap-step-num {
    width: 54px;
    height: 54px;
    margin: 0 auto 0.9rem;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--snap-font-display);
    font-size: 1.35rem;
    font-weight: 700;
    color: #fff;
    border-radius: 16px;
    background: linear-gradient(145deg, #6d7bff, #5865f2 55%, #7c5cff);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.4), 0 6px 0 -1px rgba(38,32,110,0.9),
                0 16px 30px -12px rgba(88,101,242,0.8);
    transform: perspective(600px) rotateX(16deg);
    transition: transform 0.35s cubic-bezier(0.2, 0.7, 0.3, 1.4);
}
.snap-step:nth-child(2) .snap-step-num {
    background: linear-gradient(145deg, #a05cff, #7c5cff 55%, #eb459e);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.4), 0 6px 0 -1px rgba(78,32,110,0.9),
                0 16px 30px -12px rgba(160,92,255,0.8);
}
.snap-step:nth-child(3) .snap-step-num {
    background: linear-gradient(145deg, #ff5cb0, #eb459e 55%, #c02d7f);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.4), 0 6px 0 -1px rgba(110,26,74,0.9),
                0 16px 30px -12px rgba(235,69,158,0.8);
}
.snap-step:hover .snap-step-num { transform: perspective(600px) rotateX(2deg) scale(1.07); }
.snap-step b {
    display: block;
    font-family: var(--snap-font-display);
    font-size: 1.05rem;
    color: var(--snap-ink);
    margin-bottom: 0.35rem;
}
.snap-step p { color: var(--snap-muted); font-size: 0.88rem; margin: 0; line-height: 1.55; }

@media (max-width: 760px) {
    .snap-steps { flex-direction: column; }
}

/* ------------------------------------------------------------- home footer */
.snap-footer {
    margin-top: 3.4rem;
    padding-top: 1.8rem;
    border-top: 1px solid rgba(139, 150, 255, 0.14);
    text-align: center;
}
.snap-footer-mark {
    width: 44px;
    height: 44px;
    margin: 0 auto 0.8rem;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--snap-font-display);
    font-weight: 700;
    font-size: 0.95rem;
    color: #fff;
    border-radius: 14px;
    background: linear-gradient(145deg, #5865f2, #7c5cff 60%, #eb459e);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.35), 0 12px 26px -12px rgba(88,101,242,0.8);
    animation: snapBob 7s ease-in-out infinite;
}
.snap-footer p { margin: 0.2rem 0; font-size: 0.92rem; color: var(--snap-muted); }
.snap-footer .snap-footer-dim { font-size: 0.78rem; color: #5f688c; }
"""

# --------------------------------------------------------------------------- #
#  Dashboard specific CSS                                                     #
# --------------------------------------------------------------------------- #

_DASH_CSS = """
/* segmented tab control for the teacher dashboard */
div[data-testid="stHorizontalBlock"]:has([data-snap-tabs]) {
    background: rgba(9, 13, 32, 0.62);
    border: 1px solid var(--snap-stroke);
    border-radius: 18px;
    padding: 6px;
    gap: 6px;
    backdrop-filter: blur(12px);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.05), 0 20px 48px -30px rgba(0,0,0,0.95);
}
div[data-testid="stHorizontalBlock"]:has([data-snap-tabs]) div[data-testid="stColumn"] {
    padding: 0 !important;
    min-width: 0;
}
div[data-testid="stHorizontalBlock"]:has([data-snap-tabs]) div[data-testid="stButton"] {
    width: 100%;
}
div[data-testid="stHorizontalBlock"]:has([data-snap-tabs]) div[data-testid="stButton"] > button {
    width: 100%;
    border-radius: 13px !important;
    font-size: 0.92rem;
}

/* subject card internals */
.snap-card-head {
    display: flex;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
}
.snap-card-ico {
    flex: 0 0 auto;
    width: 50px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    border-radius: 15px;
    background: linear-gradient(145deg, rgba(88,101,242,0.26), rgba(235,69,158,0.15));
    border: 1px solid rgba(139,150,255,0.3);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.2), 0 10px 22px -12px rgba(88,101,242,0.7);
    transform: perspective(560px) rotateX(12deg);
    transition: transform 0.35s cubic-bezier(0.2, 0.7, 0.3, 1.4);
}
.snap-card:hover .snap-card-ico { transform: perspective(560px) rotateX(0deg) rotate(-5deg) scale(1.07); }
.snap-card-t { flex: 1 1 auto; min-width: 0; }
.snap-card-t h3 {
    font-family: var(--snap-font-display);
    font-size: 1.28rem;
    font-weight: 700;
    color: var(--snap-ink);
    margin: 0;
    letter-spacing: -0.015em;
    overflow-wrap: anywhere;
}
.snap-card-meta { color: var(--snap-muted); font-size: 0.85rem; margin-top: 0.2rem; }

/* danger-tinted unenroll buttons (student dashboard columns) */
div[data-testid="stColumn"]:has([data-snap-footer="danger"]) div[data-testid="stButton"] > button {
    color: #ff9dbe;
    border-color: rgba(255, 120, 160, 0.32);
    background: rgba(235, 69, 158, 0.07);
}
div[data-testid="stColumn"]:has([data-snap-footer="danger"]) div[data-testid="stButton"] > button:hover:not(:disabled) {
    color: #ffc4d8;
    border-color: rgba(255, 120, 160, 0.6);
    background: rgba(235, 69, 158, 0.14);
    box-shadow: 0 12px 30px -16px rgba(235, 69, 158, 0.7);
}
"""

# --------------------------------------------------------------------------- #
#  Background scenes                                                          #
# --------------------------------------------------------------------------- #

_CUBE_FACES = "<i></i>" * 6


def _scene(home: bool) -> str:
    cubes = f"""
        <div class="snap-float snap-float-a"><div class="snap-cube">{_CUBE_FACES}</div></div>
        <div class="snap-float snap-float-b"><div class="snap-cube snap-cube-sm snap-cube-pink">{_CUBE_FACES}</div></div>
        <div class="snap-float snap-float-c"><div class="snap-cube snap-cube-sm snap-cube-cyan">{_CUBE_FACES}</div></div>
    """
    grid = '<div class="snap-gridfloor"></div>' if home else ""
    return f"""
    <div class="snap-scene" aria-hidden="true">
        <div class="snap-orb snap-orb-a"></div>
        <div class="snap-orb snap-orb-b"></div>
        <div class="snap-orb snap-orb-c"></div>
        <div class="snap-stars"></div>
        {grid}
        {cubes}
        <div class="snap-vignette"></div>
    </div>
    """


# --------------------------------------------------------------------------- #
#  Public API                                                                 #
# --------------------------------------------------------------------------- #

def _inject(css: str) -> None:
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def style_base_layout() -> None:
    """Global design system — fonts, tokens, widgets, effects."""
    _inject(_FONTS + _BASE_CSS)


def style_background_home() -> None:
    """Aurora scene + home page styles."""
    _inject(_HOME_CSS)
    st.markdown(_scene(home=True), unsafe_allow_html=True)


def style_background_dashboard() -> None:
    """Calmer aurora scene + dashboard styles."""
    _inject(_DASH_CSS)
    st.markdown(_scene(home=False), unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
#  Reusable HTML component builders                                           #
# --------------------------------------------------------------------------- #

def scroll_progress() -> None:
    """Thin gradient bar that fills as the user scrolls (CSS scroll-driven)."""
    st.markdown(
        '<div class="snap-progress"><i></i></div>',
        unsafe_allow_html=True,
    )


def section_header(icon: str, title: str, subtitle: str = "", centered: bool = False) -> None:
    """Section heading with a 3D icon tile."""
    style = " style='justify-content:center; text-align:center; flex-direction:column; gap:.6rem;'" if centered else ""
    sub = f'<p class="snap-sec-sub">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f"""
        <div class="snap-sec"{style}>
            <div class="snap-sec-ico">{icon}</div>
            <div>
                <h2 class="snap-sec-title">{title}</h2>
                {sub}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def welcome_banner(name: str, role: str) -> None:
    """Dashboard welcome line with gradient name + role pill."""
    emoji = "👩‍🏫" if role.lower() == "teacher" else "🎓"
    st.markdown(
        f"""
        <div class="snap-welcome">
            Welcome back, <b>{name}</b>
            <span class="snap-role">{emoji} {role}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def progress_bar(attended: int, total: int, label: str = "attended") -> str:
    """Animated gradient progress bar HTML (used inside subject cards)."""
    pct = int(round(attended / total * 100)) if total else 0
    return f"""
        <div class="snap-bar">
            <div class="snap-bar-top">
                <span>ATTENDANCE</span>
                <span><b>{pct}%</b> {label}</span>
            </div>
            <div class="snap-bar-track">
                <div class="snap-bar-fill" style="width:{min(max(pct, 0), 100)}%"></div>
            </div>
        </div>
    """
