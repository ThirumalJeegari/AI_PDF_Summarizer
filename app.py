import streamlit as st

from groq import Groq

from PyPDF2 import PdfReader
# from openai  import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client =Groq(
    api_key= os.getenv("GROQ_API_KEY")
    # base_url ="https://api.groq.com/openai/v1"
   
)

st.title("AI PDF Summerizer")

file_upload = st.file_uploader("Please Upload :",type="pdf")




text = ""
if file_upload is not None:
    st.success("You uploaded the document successfully Now Click on Summerize PDF!")

if st.button("Summarize PDF"):

    Reader = PdfReader(file_upload)

    for i in Reader.pages:
        extracted = i.extract_text()
        if extracted:
            text += extracted
        # st.write(text)


    
    user_prompt = text
    if user_prompt:

        try:
            response =client.chat.completions.create(
                model = "llama-3.1-8b-instant",
                messages = [
                    {
                        "role":"system",
                        "content":"You are a helpful assistant, give me simplified ad very short answer."
                    },
                    {
                        "role":"user",
                        "content": user_prompt
                    }
                ]       
            )
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")






