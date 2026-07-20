import streamlit as st
# streamlit.title('Agentic UI Demo')
st.title('Agentic UI Demo')

home_page = st.Page('Session19B.py', title='Home', icon='🏠')
chat_page = st.Page('Session19C.py', title='AI Chat')
patients_page = st.Page('Session19D.py', title='Patients')

pg = st.navigation([home_page, chat_page, patients_page])
pg.run()
