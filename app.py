from modules.risk_analysis import calculate_risk
import streamlit as st
from modules.recommendations import generate_recommendation
from modules.data_storage import save_assessment
from modules.data_storage import load_assessment
from modules.visualisations import risk_time
from modules.visualisations import sleep_vs_risk
from modules.visualisations import stress_vs_risk

st.sidebar.title("🧠 StudyWell")
st.sidebar.caption("Your study & wellness dashboard")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "📝 Assessment", "📈 My Trends", "📜 History", "💡 Recommendations"]
)
if page == "🏠 Home":
    st.markdown(
        "<h1 style='text-align: center;'>🧠 StudyWell</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align: center;'>Understand your study patterns and wellness habits.</p>",
        unsafe_allow_html=True
    )

    history = load_assessment()
    if len(history) == 0:
        st.info("Complete your first assignment to see your quick stats here.")
    else:
        latest = history.iloc[-1]
        st.subheader("📊 Your Latest Stats")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📚 Study Hours", f"{latest["study_hours"]} hrs")
        with col2:
            st.metric("😴 Sleep", f"{latest["sleep_hours"]} hrs")
        with col3:
            st.metric("🧠 Stress", f"{latest["stress"]}/10")
        with col4:
            st.metric("⚠️ Risk", f"{latest["risk_score"]}/13")


elif page == "📝 Assessment":
    st.title("New Assessment")
    st.subheader("Log today's study habits")
    study_hours = st.number_input("How many hours did you study? ", min_value=0, max_value=24)
    sleep_hours = st.number_input("How many hours did you sleep? ", min_value=0, max_value=24)
    stress = st.slider("What is your stress level on a scale of 1 to 10?", min_value=1, max_value=10)
    breaks = st.number_input("How many breaks do you typically take while studying in a day? ", min_value=0, max_value=30)
    screen_time = st.number_input("How many hours of screen time did you have today? ", min_value=0, max_value=24)

    if st.button("Analyse"):
        score, risk_level, risk_factors, positive_habits = calculate_risk(study_hours, sleep_hours, breaks, stress, screen_time)
        st.subheader("Your StudyWell Assessment")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Risk score:", score)
        with col2:
            st.write("Risk level:", risk_level.upper())

        st.subheader("Risk Score")
        st.progress(score / 13)
        st.write(f"**{score} / 13 — {risk_level} Risk**")

        if risk_level == "Low":
            st.success("Your current patterns fall within the low-risk range.")
        elif risk_level == "Moderate":
            st.warning("Some areas of your routine may need attention.")
        else:
            st.error("Several areas of your routine have been flagged.")

        st.subheader("What this means")
        if risk_level == "High":
            st.write("Your contributing factors indicate a compounding cycle: making study hours less productive and driving"
                     " stress higher due to disrupted sleep, long study hours, and screen time. This lowers cognitive "
                     "function and emotional resilience.")
            print()
            st.write("Primary Operational Impacts:")
            st.write("1. Cognitive Fatigue & Brain Fog: Continuous focus without strategic breaks depletes prefrontal cortex"
                     " resources, degrading working memory, critical thinking, and retention.")
            st.write("2. Physical Symptoms: Chronic tension headaches, digestive issues, fatigue that sleep doesn't fix, or "
                     "lowered immunity.")
            st.write("3. Emotional Exhaustion: Feeling dread, irritability, anxiety, or complete numbness whenever you "
                     "think about studying.")

        if risk_level == "Moderate":
            st.write("This essentially means is that even though these factors are not causing an immediate burnout or"
                     " systemic breakdown, but they create a constant baseline level of friction. Over time, this subtle"
                     " drain erodes efficiency, mood, and retention.")
            print()
            st.write("Since you don't need a total routine overhaul, small tactical shifts will produce the highest return"
                     " on energy.")

        if risk_level == "Low":
            st.write("Your assessment flagged relatively few risk-related patterns based on StudyWell's scoring rules. "
                     "Keep maintaining the habits that are working well for you.")

        if risk_factors:
            st.write("### ⚠️ Areas to Improve")
            for x in risk_factors:
                st.write("•", x)

        if positive_habits:
            st.write("### 🌱 Healthy Habits")
            for z in positive_habits:
                st.write("✓", z)

        save_assessment(study_hours, sleep_hours, stress, breaks, screen_time, score, risk_level)

elif page == "📈 My Trends":
    st.title("📈 My Trends")

    history = load_assessment()
    if len(history) < 2:
        st.info("Complete at least two assessments to start viewing your trends.")
    else:
        st.subheader("Risk Score over Time")
        j = risk_time(history)
        st.plotly_chart(j, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Sleep Vs. Risk")
            k = sleep_vs_risk(history)
            st.plotly_chart(k, use_container_width=True)

        with col2:
            st.subheader("Stress Vs. Risk")
            m = stress_vs_risk(history)
            st.plotly_chart(m, use_container_width=True)

elif page == "📜 History":
    st.title("📜 Assessment History")
    history = load_assessment()
    if len(history) == 0:
        st.info("No assessment history yet. Complete an assessment to see it here.")
    else:
        st.dataframe(history, use_container_width=True)

elif page == "💡 Recommendations":
    st.title("💡 Recommendations")
    history = load_assessment()
    if len(history) == 0:
        st.info("Complete at least two assessments to start viewing your trends.")
    else:
        latest = history.iloc[-1]
        score, risk_level, risk_factors, positive_habits = calculate_risk(
            latest["study_hours"],
            latest["sleep_hours"],
            latest["breaks"],
            latest["stress"],
            latest["screen_time"]
        )
        recommendations = generate_recommendation(risk_factors)
        if recommendations:
            for recommendation in recommendations:
                st.write("•", recommendation)
        else:
            st.success("No specific recommendations were generated from your latest assessment.")


