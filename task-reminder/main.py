import streamlit as st
import datetime

# Set title and image
st.title("Task Reminder App")
st.image("https://cdn.ecommercedns.uk/files/8/212198/7/40437937/image.jpg", use_column_width=True)

# User input for task and reminder duration
task = st.text_input("Enter the task you want to be reminded of:")
reminder_duration = st.number_input("Set reminder duration (in minutes):", min_value=1, max_value=120)

# Store reminder time in session state
if st.button("Set Reminder"):
    if task and reminder_duration:
        st.session_state.reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=reminder_duration)
        st.session_state.task = task
        st.success(f"Reminder set for '{task}' in {reminder_duration} minutes!")

# Check if reminder time has passed
if "reminder_time" in st.session_state and "task" in st.session_state:
    current_time = datetime.datetime.now()
    if current_time >= st.session_state.reminder_time:
        st.balloons()
        st.error(f"Time to: {st.session_state.task}!")
        del st.session_state.reminder_time  # Clear reminder after notification
