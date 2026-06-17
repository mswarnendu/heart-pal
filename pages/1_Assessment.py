import streamlit as st
import random
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from database import *

st.set_page_config(
    page_title="HeartPal | Assessment",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="auto"
)


def load_and_train():
    df = pd.read_csv("data/ml_training.csv")

    X = df.drop("HeartDiseaseorAttack", axis=1).values
    y = df["HeartDiseaseorAttack"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000, class_weight="balanced")
    model.fit(X_train, y_train)

    return model


def get_model():
    return load_and_train()


if not st.session_state.get("username"):
    st.warning("Please log in to view your risk history.")
else:

    facts = [
        "Heart disease is the #1 cause of death in the US, responsible for 1 in every 5 deaths.",
        "High blood pressure affects nearly half of American adults, but many don't know they have it.",
        "Smoking doubles your risk of heart disease.",
        "Even 30 minutes of moderate exercise 5 days a week significantly lowers your risk.",
        "High cholesterol has no symptoms — the only way to know is to get tested.",
        "People with diabetes are 2x more likely to develop heart disease.",
        "A healthy BMI between 18.5 and 24.9 is one of the strongest protective factors against heart disease.",
        "Heart disease is largely preventable — up to 80% of cases are linked to lifestyle factors.",
        "Women are just as likely as men to die from heart disease, but symptoms often present differently.",
        "Eating fruits and vegetables daily can reduce your risk of heart disease by up to 20%.",
        "Stress increases your risk of heart disease by raising blood pressure and promoting inflammation.",
        "Heavy alcohol use raises blood pressure and can weaken the heart muscle over time.",
        "About 805,000 Americans have a heart attack every year — one every 40 seconds.",
        "Getting 7–9 hours of sleep per night is linked to a lower risk of heart disease.",
        "Obesity increases your risk of heart disease by straining the heart and raising blood pressure.",
        "Aspirin therapy is no longer universally recommended — talk to your doctor before starting it.",
        "Air pollution exposure, even short-term, increases the risk of heart attack.",
        "Depression and heart disease are closely linked — each increases the risk of the other.",
        "A diet high in saturated fat raises LDL cholesterol, a major risk factor for heart disease.",
        "The Mediterranean diet is one of the most studied and proven heart-healthy eating patterns.",
        "Secondhand smoke increases the risk of heart disease by about 25–30%.",
        "Heart disease costs the US over $200 billion per year in healthcare and lost productivity.",
        "Atrial fibrillation (irregular heartbeat) increases the risk of stroke fivefold.",
        "Regular physical activity can lower LDL cholesterol and raise HDL (good) cholesterol.",
        "Sodium intake is directly linked to high blood pressure — most Americans eat too much salt.",
        "Sitting for long periods is linked to heart disease risk even in people who exercise regularly.",
        "Omega-3 fatty acids found in fish like salmon can reduce inflammation and protect the heart.",
        "Losing just 5–10% of body weight can significantly improve heart disease risk factors.",
        "Hypertension is called the 'silent killer' because it rarely causes noticeable symptoms.",
        "Dark chocolate in moderation has been shown to improve blood vessel function.",
        "Type 2 diabetes and heart disease share many of the same risk factors.",
        "Gum disease has been linked to an increased risk of heart disease.",
        "High triglyceride levels are an independent risk factor for heart disease.",
        "The heart beats about 100,000 times per day and pumps around 2,000 gallons of blood.",
        "Heart attacks are more common on Monday mornings than any other time of the week.",
        "Cold weather causes blood vessels to constrict, increasing the risk of heart attack.",
        "Family history of heart disease significantly increases your personal risk.",
        "Trans fats, found in some processed foods, are among the worst dietary contributors to heart disease.",
        "Quitting smoking reduces your risk of heart disease by half within just one year.",
        "High-sensitivity CRP is a blood marker of inflammation that predicts heart disease risk.",
        "More than 50% of heart attacks occur in people with normal cholesterol levels.",
        "Chronic kidney disease and heart disease are strongly linked and share many risk factors.",
        "Standing desks and regular movement breaks can help offset the effects of a sedentary job.",
        "Eating fewer than 5g of salt per day can reduce blood pressure significantly.",
        "Yoga and meditation have been shown to lower blood pressure and reduce heart disease risk.",
        "Cocaine use dramatically increases the risk of heart attack, even in young people.",
        "HDL cholesterol above 60 mg/dL is considered protective against heart disease.",
        "Early menopause is associated with a higher risk of heart disease in women.",
        "Loneliness and social isolation are as harmful to heart health as smoking 15 cigarettes a day.",
        "Regular health checkups are the best way to catch and manage risk factors before they become dangerous.",
    ]

    if "fact" not in st.session_state:
        st.session_state.fact = random.choice(facts)

    st.title("HeartPal Monthly Risk Assesment")
    st.markdown("---")
    st.info(f"*Did you know?* {st.session_state.fact}")

    tab1, tab2, tab3 = st.tabs(["Health Info", "Lifestyle", "Demographics"])

    with tab1:
        high_blood_pressure = st.checkbox(
            "Have you told a doctor you have high blood pressure?")
        high_chol = st.checkbox(
            "Have you ever been told you have high cholesterol?")
        chol_check = st.checkbox(
            "Have you had a cholesterol check in the last 5 years?")
        stroke = st.checkbox("Have you ever had a stroke?")
        diabetes = st.checkbox("Have you been diagnosed with diabetes?")
        diff_walk = st.checkbox(
            "Do you have serious difficulty walking or climbing stairs?")
        bmi = st.slider("BMI", 10, 65, 20)
        gen_health = st.slider(
            "General Health (1 = Excellent, 5 = Poor)", 1, 5, 2)
        phys_health = st.slider("Days Physical Health Not Good", 1, 30, 15)
        mental_health = st.slider("Days Mental Health Not Good", 1, 30, 15)

    with tab2:
        smoker = st.checkbox(
            "Have you smoked at least 100 cigarettes in your lifetime?")
        phys_activity = st.checkbox(
            "Have you done physical exercise in the last 30 days?")
        fruits = st.checkbox("Do you eat fruit at least once a day?")
        veggies = st.checkbox("Do you eat vegetables at least once a day?")
        alcohol = st.checkbox(
            "Do you have more than 14 drinks a week (men) or 7 (women)?")

    with tab3:
        sex = st.selectbox("Biological Sex", ["Male", "Female"])
        age = st.slider("Age", 18, 80, 24)
        healthcare = st.checkbox(
            "Do you have any form of health insurance or coverage?")
        doc_price = st.checkbox(
            "Was there ever a time where you had to go to the doctor but couldn't due to cost?")
        education = st.selectbox("Highest Education Level", [
            "Some High School", "High School Graduate", "Some College",
            "College Graduate", "Some Graduate School", "Graduate Degree",
        ])
        income = st.selectbox("Annual Household Income", [
            "Under $10,000", "$10,000 - $15,000", "$15,000 - $20,000",
            "$20,000 - $25,000", "$25,000 - $35,000", "$35,000 - $50,000",
            "$50,000 - $75,000", "$75,000 or more",
        ])

    st.markdown("---")

    education_val = (
        [
            "Some High School",
            "High School Graduate",
            "Some College",
            "College Graduate",
            "Some Graduate School",
            "Graduate Degree",
        ].index(education)
        + 1
    )
    income_val = (
        [
            "Under $10,000",
            "$10,000 - $15,000",
            "$15,000 - $20,000",
            "$20,000 - $25,000",
            "$25,000 - $35,000",
            "$35,000 - $50,000",
            "$50,000 - $75,000",
            "$75,000 or more",
        ].index(income)
        + 1
    )

    sex_val = 1 if sex == "Male" else 0
    age_val = (age - 18) // 5 + 1

    inputs = np.array(
        [
            [
                int(high_blood_pressure),
                int(high_chol),
                int(chol_check),
                bmi,
                int(smoker),
                int(stroke),
                int(diabetes),
                int(phys_activity),
                int(fruits),
                int(veggies),
                int(alcohol),
                int(healthcare),
                int(doc_price),
                gen_health,
                mental_health,
                phys_health,
                int(diff_walk),
                sex_val,
                age_val,
                education_val,
                income_val,
            ]
        ]
    )

    if st.button("Calculate Risk"):
        with st.spinner("Preparing your results..."):
            model = get_model()

        probs = model.predict_proba(inputs)[0]

        if already_submitted_this_month(st.session_state.username):
            st.error(
                "You've already completed this month's assessment. Check back next month!")
        else:
            probs = model.predict_proba(inputs)[0]
            save_result(st.session_state.username, probs[1] * 100)

            feature_names = [
                "High Blood Pressure", "High Cholesterol", "Cholesterol Check",
                "BMI", "Smoker", "Stroke", "Diabetes", "Physical Activity",
                "Fruits", "Vegetables", "Heavy Alcohol Use", "Healthcare Coverage",
                "Avoided Doctor Due to Cost", "General Health", "Mental Health",
                "Physical Health", "Difficulty Walking", "Sex", "Age",
                "Education Level", "Income Level"
            ]

            coefficients = model.coef_[0]
            user_input = inputs[0]

            contributions = coefficients * user_input
            factor_df = pd.DataFrame({
                "factor": feature_names,
                "contribution": contributions
            })

            top_risks = factor_df.sort_values(
                "contribution", ascending=False).head(3)
            st.subheader("Top Risk Factors")
            for _, row in top_risks.iterrows():
                st.write(f"- {row['factor']}")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Probability of High Risk",
                          f"{(probs[1] * 100):.2f}%")
            with col2:
                st.metric("Model Confidence", f"{(max(probs) * 100):.2f}%")
