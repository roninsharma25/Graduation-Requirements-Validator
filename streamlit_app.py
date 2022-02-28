import streamlit as st
import os
from utils import *


st.title('Graduation Requirements Validator')

### Add template file download feature

### Add file upload feature
fileUploader = st.file_uploader('Select a file')

if st.button('Submit File'):
    if fileUploader is None:
        st.write('You neede to select a file')
    else:
        st.write('File submitted')
        df = analyzeData(fileUploader)
        st.write(df)

