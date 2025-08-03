import streamlit as st
import time

def logout():
  if st.button("Logout"):
    st.session_state.clear()
    st.success("Finalizando o Sistema!")
    time.sleep(3)
    st.rerun()