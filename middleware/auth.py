from supabase_client import get_supabase
import streamlit as st 
supabase = get_supabase()

def sign_in(email,password):
    try:
        user = supabase.auth.sign_in_with_password({"email": email, "password": password})
        
        return user
    except Exception as e :
        st.sidebar.error(f"login failed: {e}")
          
          
# def 