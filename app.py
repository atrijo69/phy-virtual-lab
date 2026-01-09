import streamlit as st
from mechanics import mechanics_lab
from optics import optics_lab
from electronics import electronics_lab
from modern import modern_lab
from ai_assistant import ai_lab
from utils import category_card

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AI Virtual Physics Lab",
    page_icon="🔬",
    layout="wide"
)

# --------------------------------------------------
# GLOBAL WATERMARK (ALL PAGES)
# --------------------------------------------------
st.markdown("""
<style>
.watermark {
    position: fixed;
    bottom: 10px;
    right: 15px;
    opacity: 0.25;
    font-size: 0.75rem;
    color: #9ca3af;
    z-index: 9999;
    pointer-events: none;
    font-style: italic;
}
</style>

<div class="watermark">
    © Atrijo Das | All Rights Reserved
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
nav = st.sidebar.radio(
    "Navigate",
    ["Home", "Mechanics", "Optics", "Electronics", "Modern Physics", "AI Assistant"],
    index=["Home", "Mechanics", "Optics", "Electronics", "Modern Physics", "AI Assistant"].index(st.session_state.page)
)

# Always sync sidebar selection
st.session_state.page = nav

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
if st.session_state.page == "Home":
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        padding: 3rem;
        border-radius: 20px;
        color: white;
        text-align: center;">
        <h1>AI-Based Virtual Physics Laboratory</h1>
        <p style="font-size:1.1rem;">
            Complete Digital Undergraduate Physics Lab<br>
            <b>Simulations • Theory • Viva • Error Analysis</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🧪 Laboratory Modules")

    col1, col2 = st.columns(2)

    with col1:
        category_card(
            "Mechanics",
            "assets/mechanics.png",
            "Simple Pendulum, Young’s Modulus, Rigidity, Melde’s Experiment",
            "mech"
        )

        category_card(
            "Optics",
            "assets/optics.png",
            "Newton’s Rings, Laser Diffraction, Free-Space Optics",
            "opt"
        )

    with col2:
        category_card(
            "Electronics",
            "assets/electronics.png",
            "Hall Effect, Band Gap, Solar Cell, Carey Foster Bridge",
            "elec"
        )

        category_card(
            "Modern Physics",
            "assets/modern.png",
            "Franck–Hertz, Piezoelectric, Thermoelectric Generator",
            "mod"
        )

    st.markdown("""
    ---
    ### 🚀 Why This Virtual Lab?
    • 📴 No physical hardware required  
    • 📊 Automated graphs & calculations  
    • 📘 Integrated theory, precautions & error analysis  
    • 🧠 Viva / exam practice inside app  
    • 📱 Mobile-friendly & APK-ready  
    """)

    # -------- FOOTER (HOME PAGE ONLY) --------
    st.markdown("""
    <div style="
        text-align:center;
        color:#9ca3af;
        font-size:0.85rem;
        margin-top:3rem;">
        © 2026 Atrijo Das. All Rights Reserved.<br>
        Developed by Atrijo Das | PHYCATHON<br>
        Institute of Engineering & Management, Kolkata
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# LAB ROUTING
# --------------------------------------------------
elif st.session_state.page == "Mechanics":
    mechanics_lab()

elif st.session_state.page == "Optics":
    optics_lab()

elif st.session_state.page == "Electronics":
    electronics_lab()

elif st.session_state.page == "Modern Physics":
    modern_lab()

elif st.session_state.page == "AI Assistant":
    ai_lab()
