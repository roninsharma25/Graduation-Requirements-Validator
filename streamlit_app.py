from utils import *
import streamlit as st

pageTitles = ['Graduation Requirements Validator', 'Analyze Results']
pageFormButtons = ['Submit', 'Back']

if 'page' not in st.session_state or 'error' not in st.session_state:
    st.session_state.page = 0
    st.session_state.error = False

st.title(pageTitles[st.session_state.page])


# Cases for each page

if (st.session_state.page == 0):
    ### Add template file download feature
    if st.button('Download Template'):
        print('download template')

    ### Add file upload feature
    fileUploader = st.file_uploader('Select a file')
    
    if (st.session_state.error):
        st.write('You need to select a file')

def buttonCallback():
    if (st.session_state.page == 0):
        if fileUploader is None:
            st.session_state.error = not st.session_state.error
        else:
            st.write('File submitted')
            df = analyzeData(fileUploader)
            st.write(df)
    
            # Switch pages
            st.session_state.page = 1 - st.session_state.page


with st.form(key = 'Form Button'):
    submitButton = st.form_submit_button(label = pageFormButtons[st.session_state.page], on_click = buttonCallback)
