import streamlit as st
import time
from utils import *


# Function to delay the reload to show the success message
def delay():
    time.sleep(0.5)


st.set_page_config(page_title="To Do List App", layout="centered")

# Set title and description
st.title("📝 To Do List App")
st.write("A simple To-Do List app built with Streamlit and FastAPI")


# Create tabs for navigation
tabs = st.tabs(["View All Tasks", "Create Task",
               "View Task", "Update Task", "Delete Task"])

# Tab: View All Tasks
with tabs[0]:
    st.header("All Tasks")

    # Fetch fresh task data every time this tab is selected
    tasks = get_all_tasks()

    if tasks:
        for task in tasks:
            # Create a container for each task
            with st.container():
                # Display task information along with checkbox
                st.markdown(f"""
                <div style='border:1px solid #ddd; padding:10px; border-radius:5px; margin:5px 0;'>
                    <b>Task ID:</b> {task['id']} <br>
                    <b>Title:</b> {task['title']} <br>
                </div>
                """, unsafe_allow_html=True)

                # Checkbox to mark task as completed
                completed = st.checkbox(
                    f"Completed?", value=task['completed'], key=f"completed_{task['id']}")

                # Update the task completion status when checkbox is clicked
                if completed != task['completed']:
                    update_task(task['id'], task['title'],
                                task['description'], completed)
                    delay()
                    st.rerun()
    else:
        st.info("No tasks found! You can create a new task at the 'Create Task' tab.")

# Tab: Create Task
with tabs[1]:
    st.header("Create a new task")
    title = st.text_input("Task Title", key="create_title")
    description = st.text_area("Task Description", key="create_description")

    if st.button("Create Task", key="create_button"):
        if not title:
            st.error("Title is required!")
        else:
            create_task(title, description)
            delay()
            st.rerun()

# Tab: View a specific task
with tabs[2]:
    st.header("View a specific task")
    task_id = st.number_input("Enter task ID", step=1, key="view_task_id")

    if st.button("Get Task", key="view_button"):
        task = get_task(task_id)
        if task:
            with st.container():
                st.markdown(f"""
                <div style='border:1px solid #ddd; padding:10px; border-radius:5px; margin:5px 0;'>
                    <b>Task ID:</b> {task['id']} <br>
                    <b>Title:</b> {task['title']} <br>
                    <b>Description:</b> {task['description']} <br>
                    <b>Completed:</b> {task['completed']} <br>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Task not found!")

# Tab: Update Task
with tabs[3]:
    st.header("Update a task")

    # Step 1: Enter the Task ID and fetch the existing task details
    task_id = st.number_input("Enter task ID", step=1, key="update_task_id")

    # Initialize session state for task details
    if 'fetched_task' not in st.session_state:
        st.session_state.fetched_task = None

    # Fetch the task
    if st.button("Fetch Task", key="fetch_button"):
        task = get_task(task_id)
        if task:
            st.session_state.fetched_task = task
        else:
            st.error("Task not found!")
            st.session_state.fetched_task = None

    # Display and allow edits to the fetched task
    if st.session_state.fetched_task:
        title = st.text_input(
            "New Task Title", value=st.session_state.fetched_task['title'], key="update_title")
        description = st.text_area(
            "New Task Description", value=st.session_state.fetched_task['description'], key="update_description")
        completed = st.checkbox(
            "Completed?", value=st.session_state.fetched_task['completed'], key="update_completed")

        # Update the task with the modified fields
        if st.button("Update Task", key="update_button"):
            if not title:
                st.error("Title is required!")
            else:
                update_task(task_id, title, description, completed)
                delay()
                st.rerun()

# Tab: Delete Task
with tabs[4]:
    st.header("Delete a task")
    task_id = st.number_input("Enter task ID", step=1, key="delete_task_id")

    if st.button("Delete Task", key="delete_button"):
        delete_task(task_id)
        delay()
        st.rerun()
