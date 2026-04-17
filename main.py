import streamlit as st 

todo_list = ["Cook Lunch","Clean House", "Do Dishes", "Do Laundry","Watch Movies"]

st.title("Todo Website")

col1, col2, col3 = st.columns(3)
with col1:
    total = len(todo_list)
    st.info(f"Total To Do \n\n {total}")
    
with col2:
    in_progress = 5
    st.info(f"In Progress \n\n {in_progress}")  
    
with col3:
    completed = total-in_progress
    st.info(f"Completed \n\n {completed}") 
    
todo_item = st.text_input("Input a todo",placeholder=" Enter todo") 
if st.button("Add a todo"):
   if len(todo_item) >= 5: 
       todo_list.append(todo_item) 
       st.success("Todo Added")
    #    st.write(todo_list)
   else:
       st.error("Please have atleast five character")

# if st.button("Add a todo") and len(todo_item) < 5: todo_item.append(new_item)
    

for item in todo_list:
    st.info(f"{item}")
     
       






