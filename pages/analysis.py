import streamlit as st
import pandas as pd
from ai_analyzer import analyze_data, ask_followup_question

st.set_page_config(
    page_title="Analysis Results",
    page_icon="🔍",
    layout="wide"
)

# Load custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton > button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

if 'analysis_data' not in st.session_state:
    st.warning("⚠️ Please start from the main page and upload data first.")
    st.stop()

# Display analysis results
st.title("🔍 Data Analysis Results")

if 'current_data' in st.session_state and 'last_analysis' in st.session_state:
    st.info(st.session_state.last_analysis)
    
    # Q&A section
    st.header("Ask Follow-up Questions")
    user_question = st.text_input("What would you like to know about the data?")
    
    if user_question:
        if st.button("Ask Question"):
            with st.spinner("Getting answer..."):
                answer = ask_followup_question(
                    st.session_state.current_data,
                    st.session_state.last_analysis,
                    user_question
                )
                st.info(answer)
                
                # Store question and answer in history
                if 'qa_history' not in st.session_state:
                    st.session_state.qa_history = []
                st.session_state.qa_history.append({
                    "question": user_question,
                    "answer": answer
                })
    
    # Display Q&A history
    if 'qa_history' in st.session_state and st.session_state.qa_history:
        st.subheader("Previous Questions & Answers")
        for qa in st.session_state.qa_history:
            with st.expander(f"Q: {qa['question']}"):
                st.write(qa['answer'])
