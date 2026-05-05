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

if st.button("Summarize PDF"):


    text = ""
    if file_upload is not None:
        st.success("You uploaded the document successfully!")

        
        Readed = PdfReader(file_upload)

        for i in Readed.pages:
            extracted = i.extract_text()
            if extracted:
                text += extracted
            # st.write(text)


        max_len = 2000
        if len(text)>max_len:
            user_prompt = text[:2000]  
        else:
            user_prompt = text


        if user_prompt:

            try:
                response =client.chat.completions.create(
                    model = "llama-3.1-8b-instant",
                    messages = [
                        {
                            "role":"system",
                            "content":"You are a helpful assistant, give me simplified ad very short answer in 5-6 lines"
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






