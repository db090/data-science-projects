import streamlit as st
from PIL import Image
image=Image.open("financial-calculator/images/image.png")
resized_image=image.resize((800,200))


st.title("Financial Calculator")
st.image(resized_image)
st.markdown("### Step 1: Enter your total budget:")
total_budget=st.number_input("Total Budget:",min_value=0)
st.markdown("<hr style='border:1px solid #ccc;'>",unsafe_allow_html=True)
if "tasks" not in st.session_state:
    st.session_state['tasks']=[]
st.markdown("### Step 2: Add a financial task:")
task_name=st.text_input("Task Name (e.g., Rent,Groceries):")
task_amount=st.number_input("Task Amount:",min_value=0)
add_task_button=st.button("Add Task")
if add_task_button:
    if task_name and task_amount > 0 :
        st.session_state['tasks'].append({"name":task_name,"amount":task_amount})
        st.success(f"Task '{task_name}' with amount {task_amount} added!")
    else:
        st.warning("Please enter both a task name and a valid account.")

if st.session_state["tasks"]:
    st.markdown("<br><br><h3>Your Financial Tasks:</h3>",unsafe_allow_html=True)
    total_expenses = 0
    for task in st.session_state['tasks']:
        st.write(f"- **{task["name"]}**:**{task['amount']}**")
        total_expenses+=task['amount']
    remaining_budget=total_budget-total_expenses
    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown(f"### Total Expenses: **{total_expenses}**")
    st.markdown(f"### Remaining Budget (Savings): **{remaining_budget}**")

st.markdown("<hr style='border:1px solid #ccc;'>",unsafe_allow_html=True)

clear_button=st.button("Clear All Tasks")
if clear_button:
    st.session_state['tasks']=[]
    st.success("All tasks cleared")