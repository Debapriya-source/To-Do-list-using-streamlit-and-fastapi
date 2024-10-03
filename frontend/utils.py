import streamlit as st
import requests

# Function to create a task
BASE_URL = "http://127.0.0.1:8000/tasks/"


def create_task(title, description):
    data = {"id": -1, "title": title,
            "description": description, "completed": False}
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 200:
        st.success("Task created successfully!")
    else:
        st.error(f"Error: {response.status_code}")

# Function to get all tasks


def get_all_tasks():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code}")
        return []

# Function to get a task by ID


def get_task(task_id):
    response = requests.get(f"{BASE_URL}{task_id}")
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code}")
        return None

# Function to update a task


def update_task(task_id, title, description, completed):
    data = {"id": task_id, "title": title,
            "description": description, "completed": completed}
    response = requests.put(f"{BASE_URL}{task_id}", json=data)
    if response.status_code == 200:
        st.success("Task updated successfully!")
    else:
        st.error(f"Error: {response.status_code}")

# Function to delete a task


def delete_task(task_id):
    response = requests.delete(f"{BASE_URL}{task_id}")
    if response.status_code == 200:
        st.success("Task deleted successfully!")
    else:
        st.error(f"Error: {response.status_code}")
