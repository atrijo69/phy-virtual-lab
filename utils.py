import streamlit as st
import matplotlib.pyplot as plt

# --------------------------------------------------
# GRAPH PLOTTING FUNCTION (USED BY ALL EXPERIMENTS)
# --------------------------------------------------
def plot_graph(x, y, xlabel, ylabel, title):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True)
    st.pyplot(fig)


# --------------------------------------------------
# CATEGORY CARD (USED ON HOME PAGE)
# --------------------------------------------------
def category_card(title, image_path, description, key):
    st.image(image_path, use_container_width=True)
    st.markdown(f"### {title}")
    st.markdown(description)

    if st.button(f"Open {title}", key=key, use_container_width=True):
        st.session_state.page = title
