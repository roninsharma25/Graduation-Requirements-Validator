from utils import *
import streamlit as st
import pageSelector


page = st.button('Start')

if 'pageClicked' not in st.session_state:
    st.session_state.pageClicked = 0

pages = ['Home', 'Download', 'View Results']

if (page):
    st.session_state.pageClicked += 1
    st.session_state.pageClicked = 0 if st.session_state.pageClicked >= len(pages) else st.session_state.pageClicked


print(st.session_state.pageClicked)
st.write(pages[st.session_state.pageClicked])


# application = pageSelector.PageSelector()
# page = 0


# def homePage():
#     global page
#     st.title('Graduation Requirements Validator')

#     ### Add template file download feature

#     ### Add file upload feature
#     if (page == 0):
#         button = st.button('Start')

#         if not button:
#             fileUploader = st.file_uploader('Select a file')

#             if st.button('Submit File'):
#                 if fileUploader is None:
#                     st.write('You need to select a file')
#                 else:
#                     st.write('File submitted')
#                     df = analyzeData(fileUploader)
#                     st.write(df)
    
#         if button:
#             page = 1
#             application.setPage(page)

# def downloadPage():
#     st.title('Download Page')

# application.createPage('Home Page', homePage)
# application.createPage('Download Page', downloadPage)

# application.setPage(page)
