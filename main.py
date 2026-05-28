import streamlit as st 
from supabase_client import get_supabase
from middleware.auth import sign_in

supabase = get_supabase()

# Creating login sidebar

st.sidebar.title("Login Form")
#st.sidebar.markdown("This is a streamlit sidebar")
username  = st.sidebar.text_input("Enter username",placeholder="Username") 
password = st.sidebar.text_input("Enter Password",placeholder="Password") 


col1, col2 = st.sidebar.columns(2)

    
with col1:
    if col1.button("Login"):
        user_session = sign_in(username, password)
        # st.write(user_session.user.email)
        st.write(supabase.auth.get_user())
        if user_session and user_session.user.email:
            st.session_state["user"] = user_session 
            st.sidebar.success(f"Welcome {user_session.user.email}")
            st.rerun()
        
with col2:
    col2.button("Sign Up")   
    
    
# st.sidebar.text("Don't have a account?")
#forgot password and create account
if "user" in st.session_state:
    todo_list = supabase.table("todolist").select("*").execute().data
else:
    todo_list=[]



st.title("Todo Website")

if "user" in st.session_state:
    st.success(f"Welcome {username}")
    
col1, col2, col3 = st.columns(3)
with col1:
    total = len(todo_list)
    st.info(f"Total To Do \n\n {total}")
    
with col2:
    in_progress = sum(1 for item in todo_list if not item['is_completed'])
    st.info(f"In Progress \n\n {in_progress}")  
    
with col3:
    completed = total-in_progress
    st.info(f"Completed \n\n {completed}") 
    
todo_item = st.text_input("Input a todo",placeholder=" Enter todo") 
if st.button("Add a todo"):
   if len(todo_item) >= 5: 
    #    todo_list.append(todo_item) 
        supabase.table("todolist").insert({"name":todo_item}).execute()
        st.success("Todo Added")
        st.rerun() 
    #    st.write(todo_list)
   else:
       st.error("Please have atleast five character")

# if st.button("Add a todo") and len(todo_item) < 5: todo_item.append(new_item)
    

for item in todo_list:
    # st.info(f"{item['name']}")
    button_key = f"btn_{item['id']}"
    
    # Determine the label and style based on state
    label = f"✅ {item['name']}" if item['is_completed'] else f"⭕ {item['name']}"
     
     # Render the button
    if st.button(label, key=button_key, use_container_width=True):
        # Toggle the value in Supabase
        new_status = not item['is_completed']
        
        supabase.table("todolist").update({"is_completed": new_status}).eq("id", item['id']).execute()
        
        # Rerun to update the UI colors immediately
        st.rerun()  





