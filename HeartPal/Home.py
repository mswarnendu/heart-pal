import streamlit as st

st.set_page_config(
    page_title="HeartPal",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="auto"
)


def login():
    st.title("HeartPal Login")
    st.caption(
        "Enter your name to view your risk history and take your monthly assessment.")

    name = st.text_input("Your name", placeholder="e.g. Alex")

    if st.button("Get started") and name.strip():
        st.session_state.username = name.strip()
        st.rerun()


if "username" not in st.session_state:
    login()
    st.stop()


st.title("HeartPal: Small Check-ins, Big Difference")
st.subheader("Cardiovascular Awareness Tool")
st.write("""HeartPal helps you understand how your estimated cardivascular risk changes over time
         using interpretable machine learning.
         
         This tool is for awareness and education, not medical diagnosis.
         """)

st.markdown("---")
st.info("Use the sidebar to start an assessment or view your risk history")
