import streamlit as st
import numpy as np
from utils import plot_graph

def mechanics_lab():
    st.header("⚙️ MECHANICS LAB")

    exp = st.selectbox(
        "Select Experiment",
        [
            "Simple Pendulum",
            "Young's Modulus (Flexure)",
            "Modulus of Rigidity (Static)",
            "Modulus of Rigidity (Dynamic)",
            "Melde's Experiment"
        ]
    )

    # ---------------- SIMPLE PENDULUM ----------------
    if exp == "Simple Pendulum":
        st.subheader("🕰 Simple Pendulum")

        L = st.slider("Length (m)", 0.2, 2.0, 1.0)
        g = 9.8
        T = 2 * np.pi * np.sqrt(L / g)

        st.success(f"Time Period T = {T:.3f} s")

        l_vals = np.linspace(0.2, 2, 20)
        T_vals = 2 * np.pi * np.sqrt(l_vals / g)
        plot_graph(l_vals, T_vals, "Length (m)", "Time Period (s)", "Length vs Time Period")

        with st.expander("📘 Theory"):
            st.markdown("""
A simple pendulum performs simple harmonic motion for small angular oscillations.

**Formula:**
\\[
T = 2\pi \sqrt{\\frac{L}{g}}
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Angular displacement should be small  
• Length measured accurately  
• Avoid air currents
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Error in length measurement  
• Reaction time error  
• Air resistance neglected
""")

    # ---------------- YOUNG'S MODULUS ----------------
    elif exp == "Young's Modulus (Flexure)":
        st.subheader("📏 Young's Modulus (Flexure)")

        L = st.number_input("Distance between knife edges (cm)", 60.0)
        b = st.number_input("Breadth of bar (cm)", 2.0)
        d = st.number_input("Depth of bar (cm)", 0.5)
        m = st.slider("Load (kg)", 0.5, 2.5, 1.0)
        y = st.slider("Depression (cm)", 0.01, 0.1, 0.04)

        Y = (m * 9.8 * L**3) / (4 * b * d**3 * y)
        st.success(f"Young's Modulus Y = {Y:.2e} dyne/cm²")

        with st.expander("📘 Theory"):
            st.markdown("""
When a beam is supported at two points and loaded at the center, it bends.

**Formula:**
\\[
Y = \\frac{mgL^3}{4bd^3y}
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Load applied gradually  
• Beam within elastic limit  
• Knife edges clean
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Error in depression measurement  
• Zero error of instruments  
• Non-uniform beam
""")

    # ---------------- RIGIDITY STATIC ----------------
    elif exp == "Modulus of Rigidity (Static)":
        st.subheader("🔩 Modulus of Rigidity (Static)")

        l = st.number_input("Length of wire (cm)", 100.0)
        r = st.number_input("Radius of wire (cm)", 0.05)
        d = st.number_input("Pulley diameter (cm)", 5.0)
        m = st.slider("Load (kg)", 0.5, 3.0, 1.0)
        theta = st.slider("Angular twist (degree)", 1.0, 10.0, 4.0)

        eta = (180 * l * d * 9.8 / (np.pi * r**4)) * (m / theta)
        st.success(f"Rigidity Modulus η = {eta:.2e}")

        with st.expander("📘 Theory"):
            st.markdown("""
Twisting a wire produces angular deformation proportional to applied torque.

**Formula:**
\\[
\eta = \\frac{180ldg}{\pi r^4} \\frac{m}{\theta}
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Wire free from kinks  
• Load steady  
• Accurate angular reading
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Error in angular measurement  
• Friction at pulley  
• Radius measurement error
""")

    # ---------------- RIGIDITY DYNAMIC ----------------
    elif exp == "Modulus of Rigidity (Dynamic)":
        st.subheader("⏱ Modulus of Rigidity (Dynamic)")

        l = st.slider("Length (cm)", 50.0, 150.0, 100.0)
        T = st.slider("Time Period (s)", 1.0, 5.0, 2.5)
        I = st.number_input("Moment of Inertia", 10.0)

        eta = (8 * np.pi**2 * I * l) / T**2
        st.success(f"Rigidity Modulus η = {eta:.2e}")

        with st.expander("📘 Theory"):
            st.markdown("""
Time period of torsional oscillation depends on rigidity of the wire.

**Formula:**
\\[
\eta = \\frac{8\pi^2Il}{T^2}
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• Small oscillations  
• Average time readings  
• Uniform wire
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Time measurement error  
• Air damping  
• Inaccurate inertia
""")

    # ---------------- MELDE'S ----------------
    elif exp == "Melde's Experiment":
        st.subheader("🌊 Melde's Experiment")

        Tn = st.slider("Tension (N)", 5, 50, 20)
        mu = st.number_input("Linear density (kg/m)", 0.01)
        f = st.slider("Frequency (Hz)", 20, 100, 50)

        v = np.sqrt(Tn / mu)
        lam = v / f

        st.success(f"Wave Velocity = {v:.2f} m/s")
        st.success(f"Wavelength = {lam:.2f} m")

        with st.expander("📘 Theory"):
            st.markdown("""
Standing waves are formed on stretched strings.

**Formula:**
\\[
v = \\sqrt{\\frac{T}{\mu}}, \\quad v = f\lambda
\\]
""")

        with st.expander("⚠️ Precautions"):
            st.markdown("""
• String properly stretched  
• Steady vibration  
• Free pulley motion
""")

        with st.expander("📉 Error Analysis"):
            st.markdown("""
• Error in tension  
• Node counting error  
• Air damping
""")
