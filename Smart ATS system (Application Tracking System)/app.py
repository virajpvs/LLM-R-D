# streamlit run app.py
# http://localhost:8501/


import google.generativeai as genai
import PyPDF2 as pdf
from PyPDF2 import PdfReader
import os
import streamlit as st

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# gemini pro response


def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


# prompt template
input_prompt = """
Hey act as a skilled or very experienced ATS (Application Tracking System)
with deep understanding of tech field, machine lerning engineering, data science,
software engineering, data analyst, MLOps engineer and A big data engineer. your 
task is to evaluate the resume based on the given job description.
you must consider the job market is very competitive and you should 
provide best assistance for improving the resumes. Assign the 
percentage Matching based on jd and the missing key words 
with high accuracy.
resume:{text}
description:{jd}

I want the response in one single string having the stucture 
{{"JD Match": " %", "Missing keywords: []", "Profile Summery":""}}
"""

# streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader(
    "Upload Your Resume", type="pdf", help="Please uplaod the pdf")
submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        responce = get_gemini_response(input_prompt)
        st.text("Result:")
        st.subheader(responce)
