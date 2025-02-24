import streamlit as st
import pandas as pd
from ai_analyzer import analyze_data, ask_followup_question
from utils import load_css, initialize_session_state
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="CSV Data Analyzer",
    page_icon="📊",
    layout="wide"
)

# Load custom CSS
load_css()

# Initialize session state
initialize_session_state()

def main():
    st.title("📊 CSV Data Analyzer with AI")
    
    # File upload section
    st.header("1. Upload Your CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            # Read and display the data
            df = pd.read_csv(uploaded_file)
            st.session_state.current_data = df
            
            st.header("2. Data Preview")
            st.dataframe(df, use_container_width=True)
            
            # Analysis section
            st.header("3. Analysis")
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if st.button("🔍 Analyze with AI", type="primary"):
                    with st.spinner("Analyzing your data..."):
                        analysis = analyze_data(df)
                        st.session_state.last_analysis = analysis
                        
            with col2:
                if st.session_state.last_analysis:
                    st.info(st.session_state.last_analysis)
            
            # Q&A section
            if st.session_state.last_analysis:
                st.header("4. Ask Follow-up Questions")
                user_question = st.text_input("What would you like to know about the data?")
                
                if user_question:
                    if st.button("Ask Question"):
                        with st.spinner("Getting answer..."):
                            answer = ask_followup_question(
                                df, 
                                st.session_state.last_analysis,
                                user_question
                            )
                            st.info(answer)
                            
                            # Store question and answer in history
                            st.session_state.qa_history.append({
                                "question": user_question,
                                "answer": answer
                            })
                
                # Display Q&A history
                if st.session_state.qa_history:
                    st.subheader("Previous Questions & Answers")
                    for qa in st.session_state.qa_history:
                        with st.expander(f"Q: {qa['question']}"):
                            st.write(qa['answer'])
                            
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
            
    else:
        # Display instructions when no file is uploaded
        st.info("👆 Upload a CSV file to get started!")
        
        # Sample capabilities section
        with st.expander("ℹ️ What can this app do?"):
            st.write("""
            - 📤 Upload and preview CSV data
            - 📊 Analyze data patterns and insights using AI
            - 💬 Ask follow-up questions about your data
            - 📝 Track question & answer history
            - 🔒 Secure API integration
            """)

if __name__ == "__main__":
    main()
