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


st.title("HeartPal")
st.markdown("---")
st.subheader("What does HeartPal do?")
st.write("""HeartPal helps you understand how your estimated cardivascular risk changes over time
         using interpretable machine learning.
         
         This tool is for awareness and education, not medical diagnosis.
         """)

st.markdown("---")
st.subheader("How It Works")
st.write("""1. **Start an Assessment**: Click on the "Start Assessment" option in the sidebar to begin your cardiovascular risk evaluation.
2. **Provide Information**: Answer a series of questions about your health, lifestyle, and demographics.
3. **View Results**: See your risk factors and the probability of being at high risk for cardiovascular disease.
4. **Track Progress**: View your risk history over time to understand how your habits and health changes affect your risk.
""")
st.markdown("---")
st.subheader("Why Is Heart Health Important?")
st.image("display/highest_deaths_us.png",
         caption="Number of Deaths from Leading Causes in the United States (2024)")
st.write("""Heart disease is the leading cause of death for both men and women in the United States. 
         By understanding your cardiovascular risk factors and making healthy lifestyle choices, 
         you can significantly reduce your risk of developing heart disease and other related conditions.
         """)
st.markdown("---")
st.subheader("Get Started")
st.write("To get started, click on the 'Assessment' option in the sidebar to begin your cardiovascular risk evaluation.")
st.write("To look at your risk history, click on the 'History' option in the sidebar. Be aware that history does not show until at leasttwo assessments have been completed.")
st.info("Use the sidebar to start an assessment or view your risk history")
