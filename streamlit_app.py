from utils import *
from PIL import Image
import streamlit as st

pageTitles = ['Graduation Requirements Validator', 'Upload and Process Requirements', 'Analyze Results']
pageFormButtons = ['Begin', 'Submit', 'Back']

if 'page' not in st.session_state or 'error' not in st.session_state:
    st.session_state.page = 0
    st.session_state.error = False
    st.session_state.templateData = pd.read_csv('template.csv').to_csv(index = False).encode('utf-8')

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

    col1.subheader('Download the template file')
    col1.markdown('*You should download this template file and enter your courses.*')
    col1.header('')

    # Template file download
    if col1.download_button(label='Download Template', data = st.session_state.templateData, 
                            file_name = 'template.csv', mime = 'text/csv'):
        print('download template')
    
    col1.subheader('')
    col1.write('')

    # File upload feature
    col2.subheader('Upload your course history')
    col2.markdown('*After you entered your courses in the file, you should upload it below.*')
    fileUploader = col2.file_uploader('')

    if (st.session_state.error):
        st.write('You need to select a file')

elif (st.session_state.page == 2):
    col1, col2 = st.columns(2)

    col1.subheader('Class Data Submitted')
    col1.markdown('*Here is the class data you submitted.*')
    col1.write(st.session_state.data)

    col1.subheader(' ')
    col1.subheader('Requirement Exploration')
    class_ = col1.text_input('Class Input', '')
    if (class_):
        res = getRequirement(class_)
        if (res == NOT_INCORPORATED):
            msg = NOT_INCORPORATED
        else:
            msg = f'{class_} can satisfy the following requirements: {res}.'
        col1.write(msg)
    
    col1.subheader(' ')

    col2.subheader('Requirement Feedback')
    col2.markdown('*If you are missing any requirements, they are listed below.*')
    for problem in st.session_state.problems:
        col2.markdown(f'- {problem}')

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


if (st.session_state.page != 1):
    with col1.form(key = 'Form Button'):
        submitButton = st.form_submit_button(label = pageFormButtons[st.session_state.page], on_click = buttonCallback)
else:
    with col2.form(key = 'Form Button'):
        submitButton = st.form_submit_button(label = pageFormButtons[st.session_state.page], on_click = buttonCallback)


if (st.session_state.page == 1):
    backButton = col1.button(label = 'Back', on_click = buttonBackCallback)