import streamlit as st
import pandas as pd
from datetime import datetime

DATA_FILE="mood_log.csv"

MOODS = {
    "😄 Happy": "Happy",
    "😐 Neutral": "Neutral",
    "😢 Sad": "Sad",
    "😴 Tired": "Tired",
    "😡 Angry": "Angry"
}

#Load existing mood data
def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date","Mood","Note"])
    
def save_entry(data,mood,note):
    new_entry=pd.DataFrame([[data,mood,note]],columns=["Date","Mood","Note"])
    df=load_data()
    df=pd.concat([df,new_entry],ignore_index=True)
    df.to_csv(DATA_FILE,index=False)

# App UI
st.set_page_config(page_title="Daily Mood tracker",page_icon="😊")
st.title("📅 Daily Mood Tracker")

st.subheader("How are you feeling today?")

#Mood Selection
selected_mood=st.radio("Choose your mood:",list(MOODS.keys()),horizontal=True)

# Journal input
note=st.text_area("Write about your day:",height=150)

# Save Button
if st.button("Save Entry"):
    today=datetime.now().strftime("%Y-%m-%d")
    save_entry(today,MOODS[selected_mood],note)
    st.success("✅ Your mood has been saved")

st.markdown("---")

#Display previous entries
st.subheader("📜 Past Entries")
df=load_data()
if not df.empty:
    st.dataframe(df[::-1],use_container_width=True)
else:
    st.info("No entries yet. Start by saving your first mood!")

# Mood chart
st.markdown("---")
st.subheader("📈 Mood Trends Line Chart")

if not df.empty:
    mood_counts=df["Mood"].value_counts()
    st.bar_chart(mood_counts)