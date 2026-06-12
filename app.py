"""
PlantGuard AI — Streamlit Web Application
==========================================
Détection des maladies des plantes via MobileNetV2
12 classes : Corn (4) + Grape (4) + Tomato (4)

Mirrors the PlantGuard AI Desktop App with:
  • Dark theme matching the desktop UI
  • Full treatment recommendations (natural + chemical)
  • Confidence warnings & top-3 predictions
  • Multilingual support (EN / FR / AR)

Run:
    streamlit run app.py
"""

import streamlit as st
import tensorflow as tf
import numpy as np
import os
from PIL import Image
from translations import (
    tr, get_treatments, set_lang, get_lang,
    SUPPORTED_LANGS, TREATMENTS_I18N
)

# ══════════════════════════════════════════════════════════════
#  PAGE CONFIG  (must be first Streamlit call)
# ══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="PlantGuard AI — Disease Detection",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════
#  CONSTANTS
# ══════════════════════════════════════════════════════════════
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "saved_models", "v2_best_mobilenetv2_12classes.keras")

CLASS_NAMES = [
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___healthy",
]

# ══════════════════════════════════════════════════════════════
#  LANGUAGE STATE  (session-based)
# ══════════════════════════════════════════════════════════════
if "lang" not in st.session_state:
    st.session_state.lang = "en"
set_lang(st.session_state.lang)

# ══════════════════════════════════════════════════════════════
#  CUSTOM CSS  — Dark theme matching the Desktop App
# ══════════════════════════════════════════════════════════════
def inject_css():
    lang = get_lang()
    direction = "rtl" if lang == "ar" else "ltr"
    text_align = "right" if lang == "ar" else "left"

    st.markdown(f"""
    <style>
        /* ── Import Google Font ───────────────────────────── */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        /* ── Root & Body ──────────────────────────────────── */
        :root {{
            --bg: #0D1117;
            --card: #161B22;
            --card-hover: #1C2333;
            --border: #30363D;
            --green: #3FB950;
            --green-dark: #238636;
            --yellow: #D29922;
            --red: #F85149;
            --text: #E6EDF3;
            --muted: #8B949E;
            --nat-bg: #0D1F12;
            --nat-brd: #238636;
            --chem-bg: #1A1200;
            --chem-brd: #BB8009;
            --hlth-bg: #0C2A3C;
            --hlth-brd: #1F6FEB;
        }}

        /* ── RTL / LTR Direction ──────────────────────────── */
        .main .block-container, .stMarkdown, .stAlert {{
            direction: {direction};
            text-align: {text_align};
        }}

        .stApp {{
            background-color: var(--bg);
            font-family: 'Inter', 'Segoe UI', sans-serif;
            color: var(--text);
        }}

        /* ── Sidebar ──────────────────────────────────────── */
        section[data-testid="stSidebar"] {{
            background: linear-gradient(180deg, #0D2818 0%, var(--bg) 100%);
            border-right: 1px solid var(--border);
        }}
        section[data-testid="stSidebar"] * {{
            color: var(--text) !important;
        }}

        /* ── Header banner ────────────────────────────────── */
        .header-banner {{
            background: linear-gradient(135deg, #0D2818 0%, #0D1117 50%, #0D1520 100%);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 28px 36px;
            margin-bottom: 24px;
            position: relative;
            overflow: hidden;
        }}
        .header-banner::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, rgba(63,185,80,0.08) 0%, transparent 70%);
            border-radius: 50%;
        }}
        .header-title {{
            font-size: 2rem;
            font-weight: 800;
            color: var(--green);
            margin: 0;
            letter-spacing: -0.5px;
        }}
        .header-subtitle {{
            font-size: 0.95rem;
            color: var(--muted);
            margin: 4px 0 0 0;
            font-weight: 400;
        }}
        .header-status {{
            display: inline-block;
            background: rgba(35, 134, 54, 0.15);
            border: 1px solid var(--green-dark);
            border-radius: 20px;
            padding: 4px 14px;
            font-size: 0.8rem;
            color: var(--green);
            margin-top: 10px;
            font-weight: 500;
        }}

        /* ── Cards ────────────────────────────────────────── */
        .result-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 16px;
            backdrop-filter: blur(10px);
            transition: border-color 0.3s ease;
        }}
        .result-card:hover {{
            border-color: #484F58;
        }}

        .plant-badge {{
            display: inline-block;
            padding: 4px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.3px;
        }}
        .badge-healthy {{
            background: var(--green-dark);
            color: var(--green);
        }}
        .badge-disease {{
            background: #2D1B00;
            color: var(--yellow);
        }}

        .disease-name {{
            font-size: 1.35rem;
            font-weight: 700;
            margin: 12px 0 8px 0;
        }}
        .disease-name.healthy {{ color: var(--green); }}
        .disease-name.disease {{ color: #F0B429; }}

        /* ── Confidence bar ───────────────────────────────── */
        .conf-bar-container {{
            background: var(--border);
            border-radius: 6px;
            height: 10px;
            overflow: hidden;
            margin: 8px 0 16px 0;
        }}
        .conf-bar-fill {{
            height: 100%;
            border-radius: 6px;
            transition: width 0.8s ease;
        }}
        .conf-green {{ background: linear-gradient(90deg, #238636, #3FB950); }}
        .conf-yellow {{ background: linear-gradient(90deg, #9e6a03, #D29922); }}
        .conf-red {{ background: linear-gradient(90deg, #b62324, #F85149); }}

        /* ── Top-3 predictions ────────────────────────────── */
        .top3-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 6px 0;
            border-bottom: 1px solid rgba(48, 54, 61, 0.5);
        }}
        .top3-row:last-child {{ border-bottom: none; }}
        .top3-rank {{
            color: var(--muted);
            font-weight: 700;
            font-size: 0.85rem;
            min-width: 28px;
        }}
        .top3-name {{
            flex: 1;
            font-size: 0.9rem;
            padding: 0 10px;
        }}
        .top3-name.primary {{ color: var(--text); font-weight: 600; }}
        .top3-name.secondary {{ color: var(--muted); }}
        .top3-pct {{
            font-weight: 700;
            font-size: 0.9rem;
            min-width: 60px;
            text-align: right;
        }}
        .top3-pct.primary {{ color: var(--green); }}
        .top3-pct.secondary {{ color: var(--muted); }}

        /* ── Treatment cards ──────────────────────────────── */
        .treatment-card {{
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 14px;
            border-width: 1px;
            border-style: solid;
        }}
        .treatment-card.natural {{
            background: var(--nat-bg);
            border-color: var(--nat-brd);
        }}
        .treatment-card.chemical {{
            background: var(--chem-bg);
            border-color: var(--chem-brd);
        }}
        .treatment-card.healthy {{
            background: var(--hlth-bg);
            border-color: var(--hlth-brd);
        }}
        .treatment-header {{
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom-width: 1px;
            border-bottom-style: solid;
        }}
        .treatment-header.natural {{
            color: var(--nat-brd);
            border-bottom-color: var(--nat-brd);
        }}
        .treatment-header.chemical {{
            color: var(--chem-brd);
            border-bottom-color: var(--chem-brd);
        }}
        .treatment-header.healthy {{
            color: var(--hlth-brd);
            border-bottom-color: var(--hlth-brd);
        }}
        .treatment-item {{
            display: flex;
            align-items: flex-start;
            margin-bottom: 8px;
            line-height: 1.5;
        }}
        .treatment-num {{
            font-weight: 700;
            min-width: 24px;
            font-size: 0.9rem;
        }}
        .treatment-num.natural {{ color: var(--nat-brd); }}
        .treatment-num.chemical {{ color: var(--chem-brd); }}
        .treatment-text {{
            color: var(--text);
            font-size: 0.9rem;
        }}

        /* ── Warning banners ──────────────────────────────── */
        .warning-banner {{
            border-radius: 12px;
            padding: 16px 20px;
            margin-bottom: 14px;
            border-width: 1px;
            border-style: solid;
        }}
        .warning-low {{
            background: #2D0A0A;
            border-color: var(--red);
        }}
        .warning-moderate {{
            background: #1A1200;
            border-color: var(--yellow);
        }}
        .warning-title {{
            font-weight: 700;
            font-size: 0.95rem;
            margin-bottom: 4px;
        }}
        .warning-title.low {{ color: var(--red); }}
        .warning-title.moderate {{ color: var(--yellow); }}
        .warning-desc {{
            color: var(--text);
            font-size: 0.85rem;
            opacity: 0.9;
        }}

        /* ── Ready placeholder ────────────────────────────── */
        .ready-placeholder {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 60px 40px;
            text-align: center;
        }}
        .ready-title {{
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 10px;
        }}
        .ready-desc {{
            color: var(--muted);
            font-size: 0.95rem;
            margin-bottom: 20px;
        }}
        .supported-box {{
            background: var(--nat-bg);
            border: 1px solid var(--nat-brd);
            border-radius: 10px;
            padding: 14px 20px;
            display: inline-block;
        }}
        .supported-title {{
            color: var(--green);
            font-weight: 700;
            font-size: 0.9rem;
            margin-bottom: 4px;
        }}
        .supported-list {{
            color: var(--text);
            font-size: 0.85rem;
        }}

        /* ── Healthy message ──────────────────────────────── */
        .healthy-message {{
            background: var(--hlth-bg);
            border: 1px solid var(--hlth-brd);
            border-radius: 12px;
            padding: 18px 22px;
            margin-bottom: 14px;
            color: var(--text);
            font-size: 1rem;
        }}

        /* ── Divider ──────────────────────────────────────── */
        .custom-divider {{
            height: 1px;
            background: var(--border);
            margin: 12px 0;
            border: none;
        }}

        /* ── Confidence label ─────────────────────────────── */
        .conf-label {{
            color: var(--muted);
            font-size: 0.9rem;
        }}
        .conf-value {{
            font-weight: 700;
            font-size: 0.95rem;
        }}
        .conf-value.green {{ color: var(--green); }}
        .conf-value.yellow {{ color: var(--yellow); }}
        .conf-value.red {{ color: var(--red); }}

        /* ── Hide Streamlit defaults ──────────────────────── */
        #MainMenu {{ visibility: hidden; }}
        footer {{ visibility: hidden; }}
        header {{ visibility: hidden; }}

        /* ── File uploader styling ────────────────────────── */
        [data-testid="stFileUploader"] {{
            background: var(--card);
            border: 2px dashed var(--border);
            border-radius: 16px;
            padding: 20px;
        }}
        [data-testid="stFileUploader"]:hover {{
            border-color: var(--green);
        }}

        /* ── Button styling ───────────────────────────────── */
        .stButton > button {{
            background-color: var(--green-dark) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
            font-size: 1rem !important;
            padding: 12px 24px !important;
            width: 100%;
            transition: all 0.3s ease !important;
        }}
        .stButton > button:hover {{
            background-color: var(--green) !important;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(63, 185, 80, 0.3) !important;
        }}
        .stButton > button:active {{
            background-color: #1a5c26 !important;
            transform: translateY(0);
        }}

        /* ── Select box styling ───────────────────────────── */
        .stSelectbox > div > div {{
            background-color: var(--card) !important;
            border-color: var(--border) !important;
            color: var(--text) !important;
            border-radius: 8px !important;
        }}

        /* ── Section label styling ────────────────────────── */
        .section-label {{
            color: var(--muted);
            font-weight: 700;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 8px;
        }}

        /* ── Image container ──────────────────────────────── */
        .uploaded-image-container {{
            background: var(--card);
            border: 2px solid var(--green);
            border-radius: 16px;
            padding: 10px;
            margin-bottom: 14px;
            text-align: center;
        }}

        /* ── Sidebar info card ────────────────────────────── */
        .sidebar-info {{
            background: rgba(13, 31, 18, 0.6);
            border: 1px solid var(--nat-brd);
            border-radius: 10px;
            padding: 14px;
            margin-top: 16px;
            font-size: 0.82rem;
            color: var(--text);
        }}
        .sidebar-info-title {{
            color: var(--green);
            font-weight: 700;
            font-size: 0.85rem;
            margin-bottom: 6px;
        }}
    </style>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  MODEL LOADING
# ══════════════════════════════════════════════════════════════
@st.cache_resource
def load_model():
    """Load the MobileNetV2 12-class model."""
    return tf.keras.models.load_model(MODEL_PATH)


# ══════════════════════════════════════════════════════════════
#  PREDICTION
# ══════════════════════════════════════════════════════════════
def predict_disease(img: Image.Image):
    """Run prediction and return (class_name, confidence, top3)."""
    model = load_model()
    img = img.convert("RGB").resize((224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    predictions = model.predict(img_array, verbose=0)
    probs = predictions[0]

    # Top-3
    top3_idx = np.argsort(probs)[::-1][:3]
    top3 = [(CLASS_NAMES[i], float(probs[i])) for i in top3_idx]

    predicted_class = CLASS_NAMES[np.argmax(probs)]
    confidence = float(np.max(probs))

    return predicted_class, confidence, top3


# ══════════════════════════════════════════════════════════════
#  HTML BUILDERS
# ══════════════════════════════════════════════════════════════
def render_header():
    """Render the branded header banner."""
    model_exists = os.path.exists(MODEL_PATH)
    status_text = tr("status_ready") if model_exists else tr("status_missing").format(items="Model")
    st.markdown(f"""
    <div class="header-banner">
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 2.2rem;">🌿</span>
            <div>
                <p class="header-title">{tr("app_name")}</p>
                <p class="header-subtitle">{tr("app_subtitle")}</p>
            </div>
        </div>
        <div class="header-status">{'✅' if model_exists else '❌'} {status_text}</div>
    </div>
    """, unsafe_allow_html=True)


def render_ready_placeholder():
    """Render the 'Ready to Analyse' placeholder."""
    supported_title = tr("supported_title")
    supported_list = tr("supported_list").replace("\n", "<br>")
    st.markdown(f"""
    <div class="ready-placeholder">
        <div class="ready-title">{tr("ready_title")}</div>
        <div class="ready-desc">{tr("ready_desc").replace(chr(10), "<br>")}</div>
        <div class="supported-box">
            <div class="supported-title">{supported_title}</div>
            <div class="supported-list">{supported_list}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_confidence_bar(confidence):
    """Render a color-coded confidence progress bar."""
    pct = confidence * 100
    if confidence >= 0.90:
        color_class = "conf-green"
        val_class = "green"
    elif confidence >= 0.70:
        color_class = "conf-yellow"
        val_class = "yellow"
    else:
        color_class = "conf-red"
        val_class = "red"

    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span class="conf-label">{tr("confidence")}</span>
        <span class="conf-value {val_class}">{pct:.1f}%</span>
    </div>
    <div class="conf-bar-container">
        <div class="conf-bar-fill {color_class}" style="width: {pct}%;"></div>
    </div>
    """, unsafe_allow_html=True)


def render_top3(top3):
    """Render the top-3 predictions."""
    st.markdown(f"""
    <div style="color: var(--muted); font-size: 0.85rem; font-weight: 600; margin-bottom: 8px;">
        {tr("top_predictions")}
    </div>
    """, unsafe_allow_html=True)

    rows_html = ""
    for i, (cn, cp) in enumerate(top3):
        info = get_treatments(cn)
        display = info.get("display", cn) if info else cn
        primary = "primary" if i == 0 else "secondary"
        rows_html += f"""
        <div class="top3-row">
            <span class="top3-rank">#{i+1}</span>
            <span class="top3-name {primary}">{display}</span>
            <span class="top3-pct {primary}">{cp*100:.1f}%</span>
        </div>
        """

    st.markdown(rows_html, unsafe_allow_html=True)


def render_warning(confidence):
    """Render confidence warning banners if applicable."""
    if confidence < 0.60:
        st.markdown(f"""
        <div class="warning-banner warning-low">
            <div class="warning-title low">⚠️ {tr("low_conf_title")}</div>
            <div class="warning-desc">{tr("low_conf_desc").replace(chr(10), "<br>")}</div>
        </div>
        """, unsafe_allow_html=True)
    elif confidence < 0.80:
        st.markdown(f"""
        <div class="warning-banner warning-moderate">
            <div class="warning-title moderate">⚡ {tr("mod_conf_title")}</div>
        </div>
        """, unsafe_allow_html=True)


def render_treatment_card(title, items, card_type="natural"):
    """Render a treatment card (natural/chemical/healthy)."""
    icon = {"natural": "🌱", "chemical": "🧪", "healthy": "💙"}.get(card_type, "📋")
    items_html = ""
    for i, item in enumerate(items):
        items_html += f"""
        <div class="treatment-item">
            <span class="treatment-num {card_type}">{i+1}.</span>
            <span class="treatment-text">{item}</span>
        </div>
        """

    st.markdown(f"""
    <div class="treatment-card {card_type}">
        <div class="treatment-header {card_type}">{icon} {title}</div>
        {items_html}
    </div>
    """, unsafe_allow_html=True)


def render_results(class_name, confidence, top3):
    """Render the full results panel."""
    info = get_treatments(class_name)
    if not info:
        st.error(f"{tr('error_prefix')} Unknown class: {class_name}")
        return

    display = info.get("display", class_name)
    plant = info.get("plant", "Unknown")
    disease = info.get("disease", None)
    natural = info.get("natural", [])
    chemical = info.get("chemical", [])
    healthy = disease is None

    # Confidence warning
    render_warning(confidence)

    # Result card
    badge_class = "badge-healthy" if healthy else "badge-disease"
    status = tr("status_healthy") if healthy else tr("status_disease")
    name_class = "healthy" if healthy else "disease"

    st.markdown(f"""
    <div class="result-card">
        <span class="plant-badge {badge_class}">{plant}</span>
        <div class="disease-name {name_class}">{status} {display}</div>
        <div class="custom-divider"></div>
    """, unsafe_allow_html=True)

    # Confidence bar
    render_confidence_bar(confidence)

    # Divider
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    # Top-3
    render_top3(top3)

    # Close result card
    st.markdown('</div>', unsafe_allow_html=True)

    # Treatment section
    if healthy:
        st.markdown(f"""
        <div class="healthy-message">
            ✅ {tr("healthy_msg").replace(chr(10), "<br>")}
        </div>
        """, unsafe_allow_html=True)
        if natural:
            render_treatment_card(tr("preventive_title"), natural, "natural")
    else:
        if natural:
            render_treatment_card(tr("natural_title"), natural, "natural")
        if chemical:
            render_treatment_card(tr("chemical_title"), chemical, "chemical")


# ══════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════
def build_sidebar():
    """Build the sidebar with language selector, uploader, and controls."""
    with st.sidebar:
        # Language selector
        st.markdown(f'<div class="section-label">🌍 Language</div>', unsafe_allow_html=True)
        lang_options = list(SUPPORTED_LANGS.keys())
        lang_labels = {
            "en": "🇬🇧 English",
            "fr": "🇫🇷 Français",
            "ar": "🇸🇦 العربية",
        }
        current_idx = lang_options.index(st.session_state.lang)
        selected = st.selectbox(
            "Language",
            lang_options,
            index=current_idx,
            format_func=lambda x: lang_labels.get(x, x),
            label_visibility="collapsed",
            key="lang_select",
        )
        if selected != st.session_state.lang:
            st.session_state.lang = selected
            set_lang(selected)
            st.rerun()

        st.markdown("---")

        # Upload section
        st.markdown(f'<div class="section-label">📤 {tr("upload_label")}</div>', unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            tr("upload_label"),
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed",
            key="file_uploader",
        )

        # Show uploaded image
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, use_container_width=True)

            # Analyse button
            analyse_clicked = st.button(
                f"🔬 {tr('btn_analyse')}",
                use_container_width=True,
                key="btn_analyse",
            )

            # Reset button
            if st.button(
                f"↺ {tr('btn_reset')}",
                use_container_width=True,
                key="btn_reset",
            ):
                st.session_state.pop("file_uploader", None)
                st.session_state.pop("results", None)
                st.rerun()

            return uploaded_file, image, analyse_clicked

        # Supported plants info
        st.markdown(f"""
        <div class="sidebar-info">
            <div class="sidebar-info-title">🌿 {tr("supported_title")}</div>
            {tr("supported_list").replace(chr(10), "<br>")}
        </div>
        """, unsafe_allow_html=True)

        return None, None, False


# ══════════════════════════════════════════════════════════════
#  MAIN APP
# ══════════════════════════════════════════════════════════════
def main():
    inject_css()

    # Sidebar
    uploaded_file, image, analyse_clicked = build_sidebar()

    # Header
    render_header()

    # Main content area
    if analyse_clicked and image is not None:
        # Show loading
        with st.spinner(tr("loading")):
            class_name, confidence, top3 = predict_disease(image)

        # Store results in session
        st.session_state.results = {
            "class_name": class_name,
            "confidence": confidence,
            "top3": top3,
        }

    # Display results or placeholder
    if "results" in st.session_state:
        r = st.session_state.results
        render_results(r["class_name"], r["confidence"], r["top3"])
    elif uploaded_file is not None:
        # Image uploaded but not yet analysed
        render_ready_placeholder()
    else:
        render_ready_placeholder()


if __name__ == "__main__":
    main()