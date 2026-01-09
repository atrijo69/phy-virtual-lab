import streamlit as st
import numpy as np
from utils import plot_graph

def modern_lab():
    st.header("🧪 MODERN & ENERGY PHYSICS LAB")

    exp = st.selectbox(
        "Select Experiment",
        [
            "Franck–Hertz Experiment",
            "Piezoelectric Effect",
            "Thermoelectric Generator"
        ]
    )

    # ---------------- FRANCK HERTZ ----------------
    if exp == "Franck–Hertz Experiment":
        st.subheader("⚛️ Franck–Hertz Experiment")

        V = np.linspace(0, 90, 200)
        excitation = st.slider("Excitation Potential (V)", 10.0, 15.0, 11.5)

        I = np.sin(2 * np.pi * V / excitation)**2 + 0.2
        plot_graph(V, I, "Voltage (V)", "Current", "Franck–Hertz Curve")

        with st.expander("📘 Theory"):
            st.markdown("""
The experiment confirms discrete atomic energy levels.

**Formula:**
\\[
\\Delta E = e \\Delta V
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Stable voltage supply  
• Tube warming required  
• Avoid sudden changes
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Contact potential  
• Thermal noise  
• Voltage reading error
""")

    # ---------------- PIEZOELECTRIC ----------------
    elif exp == "Piezoelectric Effect":
        st.subheader("🔊 Piezoelectric Effect")

        force = np.linspace(0, 100, 20)
        k = st.slider("Piezoelectric Constant", 0.01, 0.1, 0.05)
        voltage = k * force

        plot_graph(force, voltage, "Force (N)", "Voltage (V)", "Piezoelectric Response")

        with st.expander("📘 Theory"):
            st.markdown("""
Certain crystals generate voltage when mechanical stress is applied.

**Relation:**
\\[
V \\propto F
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Uniform force application  
• Avoid mechanical shock  
• Proper electrode contact
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Non-uniform stress  
• Mechanical losses  
• Electrical noise
""")

    # ---------------- THERMOELECTRIC ----------------
    else:
        st.subheader("🌡 Thermoelectric Generator")

        deltaT = np.linspace(0, 150, 20)
        S = st.slider("Seebeck Coefficient (mV/K)", 0.05, 0.3, 0.12)
        voltage = S * deltaT

        plot_graph(deltaT, voltage, "ΔT (K)", "Voltage (mV)", "Seebeck Effect")

        with st.expander("📘 Theory"):
            st.markdown("""
A temperature difference across junctions produces emf (Seebeck effect).

**Formula:**
\\[
V = S\\Delta T
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Maintain steady temperature gradient  
• Proper insulation  
• Avoid heat loss
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Heat leakage  
• Sensor lag  
• Environmental loss
""")
