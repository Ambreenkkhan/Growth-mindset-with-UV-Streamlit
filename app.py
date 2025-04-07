import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Set page config
st.set_page_config(page_title="Daily Growth Tracker", layout="centered")

# Title
st.title("📈 Daily Growth Tracker")

# Mood selection
mood = st.radio("How did you feel today?", ("Happy", "Neutral", "Sad"))

# Daily Learning input
learning_input = st.text_area("What did you learn today?")

# Save today's date
today_date = datetime.today().strftime('%Y-%m-%d')

# Placeholder for daily log
if "learning_data" not in st.session_state:
    st.session_state.learning_data = []

# Submit today's learning
if st.button("Submit Today's Learning"):
    if learning_input and mood:
        st.session_state.learning_data.append({
            "date": today_date,
            "learning": learning_input,
            "mood": mood
        })
        st.success("Your progress has been saved! 🎉")

        # Immediately show the newly added log
        st.markdown("### ✏️ Your Latest Entry:") 
        st.markdown(f"**{today_date}** - Mood: {mood}")
        st.markdown(f"Learning: {learning_input}")
        st.markdown("---")
    else:
        st.warning("Please enter both mood and what you learned today!")

# Show past entries (excluding today's if already shown above)
if st.session_state.learning_data:
    st.header("📚 Your Previous Learning Log")
    for entry in reversed(st.session_state.learning_data[:-1]):
        st.markdown(f"**{entry['date']}** - Mood: {entry['mood']}")
        st.markdown(f"Learning: {entry['learning']}")
        st.markdown("---")

# 🌟 Motivational Quote of the Week
quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is the sum of small efforts, repeated day in and day out. – Robert Collier",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you."
]
quote_of_the_week = random.choice(quotes)
st.markdown(f"### 🌟 Motivational Quote of the Week: {quote_of_the_week}")

# Footer
st.markdown("---")
st.markdown("Developed by **Ambreen Adnan**")
