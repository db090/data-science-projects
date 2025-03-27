import streamlit as st
import datetime
import time
st.title("Task Reminder App")
st.image("https://cdn.ecommercedns.uk/files/8/212198/7/40437937/image.jpg",use_column_width=True)
task=st.text_input("Enter the task you want to be reminded of:")
reminder_duration=st.number_input("Set reminder duration (in minutes):",min_value=1,max_value=120)
if st.button("Set Reminder"):
    if task and reminder_duration:
        reminder_time=datetime.datetime.now()+datetime.timedelta(minutes=reminder_duration)
        st.success(f"Remainder set for '{task}' in {reminder_duration} minutes at {reminder_time.strftime('%I:%M %p')}!")
        while True:
            current_time=datetime.datetime.now()
            if current_time >= reminder_time:
                st.balloons()
                st.error(f"Time to: {task}!")
                break
            time.sleep(60)
    else:
        st.warning("Please enter a task and set a reminder duration!")