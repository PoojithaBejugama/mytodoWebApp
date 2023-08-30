import streamlit as st
import functions


def add_todo():
    todo = st.session_state["input"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

#def delete_todos():



todos = functions.get_todos()
st.title("My todo App")

st.subheader("One of a kind todo app")
st.write("get oraganized")

for index, item in enumerate(todos):
    checkbox= st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="", placeholder= "add new item...", on_change=add_todo, key="input")

st.button(label="Edit", key="Edit")



print("Hello")