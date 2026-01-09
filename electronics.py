import streamlit as st
import numpy as np
from utils import plot_graph

def electronics_lab():
    st.header("⚡ ELECTRONICS & SOLID STATE LAB")

    exp = st.selectbox(
        "Select Experiment",
        [
            "Carey Foster Bridge",
            "Hall Effect",
            "e/m of Electron",
            "Band Gap (Four Probe)",
            "Solar Cell Characteristics"
        ]
    )

    # ---------------- CAREY FOSTER ----------------
    if exp == "Carey Foster Bridge":
        st.subheader("🔗 Carey Foster Bridge")

        X = st.slider("Known Resistance X (Ω)", 0.1, 1.0, 0.2)
        l1 = st.slider("Balance Length l₁ (cm)", 10.0, 90.0, 40.0)
        l2 = st.slider("Balance Length l₂ (cm)", 10.0, 90.0, 60.0)

        rho = X / abs(l2 - l1)
        Y = X - rho * (l2 - l1)

        st.success(f"Resistance per unit length ρ = {rho:.4f} Ω/cm")
        st.success(f"Unknown resistance Y = {Y:.4f} Ω")

        with st.expander("📘 Theory"):
            st.markdown("""
Carey Foster bridge is used to determine very low resistance using balance lengths.

**Formula:**
\\[
Y = X - \rho(l_2 - l_1)
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Tight electrical connections  
• Jockey contact should be light  
• Low current to avoid heating
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Contact resistance  
• Non-uniform bridge wire  
• Reading error in length
""")

    # ---------------- HALL EFFECT ----------------
    elif exp == "Hall Effect":
        st.subheader("🧲 Hall Effect")

        I = st.slider("Current (A)", 0.1, 5.0, 1.0)
        B = st.slider("Magnetic Field (T)", 0.1, 2.0, 0.5)
        t = st.number_input("Thickness (m)", 0.001)

        Vh = (I * B) / t
        st.success(f"Hall Voltage Vₕ = {Vh:.4f} V")

        with st.expander("📘 Theory"):
            st.markdown("""
When a current-carrying conductor is placed in a magnetic field,
a transverse voltage is produced.

**Formula:**
\\[
V_H = \\frac{IB}{nt}
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Uniform magnetic field  
• Constant temperature  
• Clean electrical contacts
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Temperature variation  
• Field non-uniformity  
• Electrical noise
""")

    # ---------------- E/M ----------------
    elif exp == "e/m of Electron":
        st.subheader("🔄 e/m of Electron")

        V = st.slider("Accelerating Voltage (V)", 100, 500, 200)
        B = st.slider("Magnetic Field (T)", 0.01, 0.2, 0.05)
        r = st.slider("Radius (m)", 0.02, 0.2, 0.08)

        em = (2 * V) / (B**2 * r**2)
        st.success(f"e/m = {em:.2e} C/kg")

        with st.expander("📘 Theory"):
            st.markdown("""
Electrons moving in a magnetic field follow circular paths.

**Formula:**
\\[
\\frac{e}{m} = \\frac{2V}{B^2 r^2}
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Stable voltage supply  
• Uniform magnetic field  
• Accurate radius measurement
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Error in magnetic field value  
• Radius reading error  
• Voltage fluctuation
""")

    # ---------------- BAND GAP ----------------
    elif exp == "Band Gap (Four Probe)":
        st.subheader("🔋 Band Gap of Semiconductor")

        T = np.linspace(300, 450, 20)
        Eg_actual = st.slider("Expected Band Gap (eV)", 0.5, 1.2, 0.67)
        k = 8.617e-5

        rho = np.exp(Eg_actual / (2 * k * T))
        plot_graph(1/T, np.log(rho), "1/T", "ln(ρ)", "ln(ρ) vs 1/T")

        slope = np.polyfit(1/T, np.log(rho), 1)[0]
        Eg = 2 * k * slope
        st.success(f"Calculated Band Gap Eᵍ ≈ {Eg:.3f} eV")

        with st.expander("📘 Theory"):
            st.markdown("""
Resistivity of a semiconductor varies exponentially with temperature.

**Formula:**
\\[
E_g = 2k \\times slope
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Slow temperature variation  
• Constant current  
• Good probe contact
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Temperature lag  
• Contact resistance  
• Instrument calibration
""")

    # ---------------- SOLAR CELL ----------------
    else:
        st.subheader("☀️ Solar Cell Characteristics")

        V = np.linspace(0, 0.6, 50)
        I = np.maximum(0, 1 - V/0.6)
        P = V * I

        plot_graph(V, I, "Voltage (V)", "Current (A)", "I–V Curve")
        plot_graph(V, P, "Voltage (V)", "Power (W)", "Power Curve")

        with st.expander("📘 Theory"):
            st.markdown("""
Solar cells convert light energy into electrical energy using p-n junctions.

**Formula:**
\\[
P = VI
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Constant illumination  
• Avoid shadowing  
• Gradual load variation
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Fluctuating light intensity  
• Temperature variation  
• Meter least count
""")
