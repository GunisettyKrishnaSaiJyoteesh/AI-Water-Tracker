import streamlit as st
import pandas as pd
from datetime import datetime
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake_history

if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False

# Welcome section

if not st.session_state.tracker_started:
    st.title("Welcome to the Water Intake Tracker!")
    st.markdown("""
    Track your daily hydration with help of AI assistant. Log your intake and get smart feedback and stay healthy.
                """)
    if st.button("Start Tracking"):
        st.session_state.tracker_started = True
        st.experimental_rerun()
else:
    st.title("AI Water Intake Dashboard")

    #Sidebar : Take input
    st.sidebar.header("Log Water Intake")
    user_id = st.sidebar.text_input("User ID", value="user123")
    intake_ml = st.sidebar.number_input("Water Intake (ml)", min_value=0, step=100)

    if st.sidebar.button("Submit"):
        log_intake(user_id, intake_ml)
        st.sidebar.success(f"Logged {intake_ml} ml for user {user_id}.")

        agent = WaterIntakeAgent()
        feedback = agent.analyze_intake(intake_ml)
        st.info(f"AI Feedback: {feedback}")
    
    #Divider
    st.sidebar.markdown("---")

    # History Section
    st.header("Water Intake History")

    if user_id:
        history = get_intake_history(user_id)
        if history:
            dates = [datetime.strptime(record[1], "%Y-%m-%d") for record in history]
            values = [record[0] for record in history]
            df = pd.DataFrame({"Date": dates, "Intake (ml)": values})

            st.dataframe(df)
            st.line_chart(df.set_index("Date"))

        else:
            st.warning("No intake history found for this user.")
