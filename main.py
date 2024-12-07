from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
import streamlit as st

# .env 파일 로드
load_dotenv()

# OpenAI API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY가 설정되지 않았습니다.")

# ChatOpenAI 초기화
chat_model = ChatOpenAI(api_key=api_key)

# Streamlit 앱 설정
st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        result = chat_model.invoke(subject + "에 대한 시를 써줘")
        st.write(result.content)