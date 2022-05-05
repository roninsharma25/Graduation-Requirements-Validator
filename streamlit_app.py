from utils import *
from PIL import Image
import streamlit as st

pageTitles = ['Graduation Requirements Validator', 'Input Data', 'Analyze Results']
pageFormButtons = ['Begin', 'Submit', 'Back']

if 'page' not in st.session_state or 'error' not in st.session_state:
    st.session_state.page = 0
    st.session_state.error = False

st.title(pageTitles[st.session_state.page])


# Cases for each page

col1, col2 = st.columns(2)
fileUploader = None

if (st.session_state.page == 0):
    col1.subheader('Streamline the ECE graduation process')
    col1.title(' ')
    col1.title(' ')
    col1.subheader('Quickly identify missing requirements')
    col1.title(' ')
    col1.title(' ')
    col1.subheader('Discover classes to fulfill requirements')
    
    image = Image.open('images/Cornell.png')
    col2.image(image, width = 452)

elif (st.session_state.page == 1):
    col1, col2 = st.columns(2)

    ### Add template file download feature
    if col1.button('Download Template'):
        print('download template')

    ### Add file upload feature
    fileUploader = col2.file_uploader('Select a file')

    if (st.session_state.error):
        st.write('You need to select a file')

elif (st.session_state.page == 2):
    col1, col2 = st.columns(2)

    col1.write('File submitted')
    col1.write(st.session_state.data)
    col2.write('Problems')
    col2.write(st.session_state.problems)

def buttonCallback():
    global fileUploader
    if (st.session_state.page == 0):

        st.session_state.page = 1
    
    elif (st.session_state.page == 1):
        if fileUploader is None:
            st.session_state.error = not st.session_state.error

        else:

            st.session_state.data, st.session_state.problems = analyzeData(fileUploader)

            # Switch pages
            st.session_state.page = 2
    
    else: # last page

        # Switch pages
        st.session_state.page = 1



def buttonBackCallback():
    st.session_state.page -= 1

print(st.session_state.page)


with col1.form(key = 'Form Button'):
    submitButton = st.form_submit_button(label = pageFormButtons[st.session_state.page], on_click = buttonCallback)

if (st.session_state.page == 1):
    backButton = st.button(label = 'Back', on_click = buttonBackCallback)