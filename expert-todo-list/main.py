import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Expert To-Do List App" ,layout="centered", initial_sidebar_state="collapsed")

st.markdown("""

""")

st.title("Expert To-Do List App")
st.write("Organize your tasks like a pro! Manage your daily to-do's with ease and style.")

if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

def add_task():
    task_description= st.session_state["new_task"]
    if task_description:
        task = {"task":task_description,"status":"Pending","timestamp":datetime.now()}
        st.session_state["tasks"].append(task)

def complete_task(index):
    st.session_state["tasks"][index]["status"]="Completed"

st.text_input("Enter a new task:",key="new_task")
st.button("Add Task" , on_click=add_task)

if st.session_state["tasks"]:
    df=pd.DataFrame(st.session_state["tasks"])
    df["Time Added"]=df["timestamp"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))
    df.drop("timestamp",axis=1,inplace=True)
    st.dataframe(df[["task","status","Time Added"]])

    for index,task in enumerate(st.session_state["tasks"]):
        if task["status"] == "Pending":
            if st.button(f"Mark as completed - {task["task"]}",key=index):
                complete_task(index)

st.write("## Task Summary:")
pending_tasks = len([task for task in st.session_state["tasks"] if task["status"] == "Pending"])
completed_tasks = len([task for task in st.session_state["tasks"] if task["status"] == "Completed"])
st.write(f"### Total Tasks: {len(st.session_state["tasks"])}")
st.write(f"Pending Tasks: {pending_tasks}")
st.write(f"Completed Tasks: {completed_tasks}")