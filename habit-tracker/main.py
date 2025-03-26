import streamlit as st
import pandas as pd
import datetime

st.title("Habit Tracker")
st.image("https://cdn.shopify.com/s/files/1/0840/8370/3830/files/1605802340-special-habit-tracker.jpg",use_column_width=True)
if "habits" not in st.session_state:
    st.session_state.habits=[]

if "progress" not in st.session_state:
    st.session_state.progress={}

def add_habit(habit_name):
    if habit_name and habit_name not in st.session_state.habits:
        st.session_state.habits.append(habit_name)
        st.session_state.progress[habit_name]=[]

def update_progress(habit_name,completed):
    today=datetime.date.today()
    if habit_name in st.session_state.progress:
        st.session_state.progress[habit_name].append((today,completed))

st.subheader("Add a new habit")
new_habit=st.text_input("Enter a habit:")
if st.button("Add Habit"):
    add_habit(new_habit)
    st.success(f"Habit '{new_habit}' added!")

st.subheader("Track Your Habits")

if st.session_state.habits:
    for habit in st.session_state.habits:
        completed_today=st.checkbox(f"{habit} completed today?",key=habit)
        if completed_today:
            update_progress(habit,True)
            st.success(f"{habit} marked as completed!")
        else:
            update_progress(habit,False)

st.subheader("Habit Progress")
for habit,progress in st.session_state.progress.items():
    completed_days = sum(1 for day,completed in progress if completed)
    total_days = len(progress)
    if total_days > 0:
        completion_rate = (completed_days/total_days)*100
        st.text(f"{habit}:{completion_rate:.2f}% completion rate")
        st.progress(completion_rate/100)
    else:
        st.text(f"{habit}: No progress yet")
