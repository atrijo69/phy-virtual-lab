import streamlit as st

def ai_lab():
    st.header("🤖 AI PHYSICS ASSISTANT")

    q = st.text_input("Ask a Physics Question (Viva / Theory / Errors)")

    if not q:
        st.info("Try asking: 'What is Hall Effect?' or 'Why Newton's rings are circular?'")
        return

    q = q.lower()

    answers = {
        "hall": "Hall Effect occurs due to Lorentz force on charge carriers in magnetic field.",
        "newton": "Newton’s rings are circular due to symmetry of air film thickness.",
        "band gap": "Band gap is the energy difference between conduction and valence band.",
        "franck": "Franck–Hertz experiment proves quantized atomic energy levels.",
        "young": "Young’s modulus is the ratio of stress to strain within elastic limit.",
        "piezo": "Piezoelectric materials generate voltage under mechanical stress.",
        "thermoelectric": "Thermoelectric generator works on Seebeck effect.",
        "error": "Common errors include parallax, least count error, temperature variation."
    }

    for key in answers:
        if key in q:
            st.success(answers[key])
            return

    st.warning("This question is outside my current syllabus knowledge base.")
