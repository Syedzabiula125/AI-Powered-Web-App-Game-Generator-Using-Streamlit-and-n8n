import streamlit as st
import requests
import subprocess
import re
import os
import sys

st.title("AI-Powered Web AppGame Generator Using Streamlit and n8n")

text=st.text_area("Enter your Requriements for WebApp or AppGame")


if st.button("submit"):
    if text:
        response=requests.post(url='https://infosyed.app.n8n.cloud/webhook-test/19140b2f-bb9a-47cf-b1c9-c2821d164c2d',json={"text":text})
        if response.status_code==200:
            st.success("Successed")
            #st.write( response.json()['output'])


            clean_code = re.sub(r"```python|```", "", response.json()['output']).strip()

            with open("web.py", "w", encoding="utf-8") as file:
                file.write(clean_code)

            subprocess.run(['python',"web.py"])

