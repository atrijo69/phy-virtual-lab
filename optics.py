import streamlit as st
import numpy as np
from utils import plot_graph

def optics_lab():
    st.header("🔦 OPTICS LAB")

    exp = st.selectbox(
        "Select Experiment",
        [
            "Newton's Rings",
            "Laser Diffraction",
            "Laser Free Space Communication"
        ]
    )

    # ---------------- NEWTON'S RINGS ----------------
    if exp == "Newton's Rings":
        st.subheader("🟠 Newton's Rings")

        lam = st.number_input("Wavelength (nm)", 589.0) * 1e-9
        Dn = st.number_input("Dₙ (mm)", 4.0) * 1e-3
        Dnm = st.number_input("Dₙ₊ₘ (mm)", 6.0) * 1e-3
        m = st.slider("Order difference", 1, 20, 10)

        R = (Dnm**2 - Dn**2) / (4 * m * lam)
        st.success(f"Radius of Curvature R = {R:.3f} m")

        with st.expander("📘 Theory"):
            st.markdown("""
Newton’s rings are formed due to interference of light reflected from air film.

**Formula:**
\\[
R = \\frac{D_{n+m}^2 - D_n^2}{4m\lambda}
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Clean optical surfaces  
• Monochromatic light  
• Avoid vibration
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Diameter measurement error  
• Least count of microscope  
• Non-uniform air film
""")

    # ---------------- LASER DIFFRACTION ----------------
    elif exp == "Laser Diffraction":
        st.subheader("🔴 Laser Diffraction")

        d = st.number_input("Grating spacing (nm)", 1000.0) * 1e-9
        m = st.slider("Order", 1, 3, 1)
        theta = st.slider("Angle (degrees)", 5.0, 60.0, 20.0)

        lam = d * np.sin(np.radians(theta)) / m
        st.success(f"Wavelength λ = {lam*1e9:.2f} nm")

        with st.expander("📘 Theory"):
            st.markdown("""
Diffraction occurs when light passes through narrow slits.

**Formula:**
\\[
\lambda = \\frac{d\sin\theta}{m}
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Never view laser directly  
• Accurate angle reading  
• Proper grating alignment
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Vernier least count  
• Misalignment error  
• Angular reading error
""")

    # ---------------- LASER COMM ----------------
    else:
        st.subheader("📡 Laser Free Space Communication")

        d = st.slider("Distance (m)", 10, 500, 100)
        noise = st.slider("Noise Level", 0.0, 1.0, 0.2)

        t = np.linspace(0, 1, 1000)
        signal = np.sin(2 * np.pi * 5 * t)
        received = signal * np.exp(-d / 300) + noise * np.random.randn(len(t))

        plot_graph(t, received, "Time", "Amplitude", "Received Signal")

        with st.expander("📘 Theory"):
            st.markdown("""
Laser signals attenuate with distance and noise.

**Relation:**
Signal ∝ e⁻ᵈ
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Proper alignment  
• Avoid ambient light  
• Stable source
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Noise interference  
• Atmospheric loss  
• Detector sensitivity
""")
