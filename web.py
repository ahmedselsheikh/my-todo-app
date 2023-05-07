import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout='wide')


def add_todo():
    todo_new = st.session_state.new_todo
    todos.append(todo_new + '\n')
    functions.write_todos(todos)


st.title('My to-do App')
st.subheader('This is my web to-do App')
st.write('This app is to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(f"{todo}", key=f"checkbox_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f'checkbox_{index}']
        st.experimental_rerun()

new_todo = st.text_input(label='Add new todo', placeholder='Add new todo.....',
                         on_change=add_todo, key='new_todo')


# st.session_state
