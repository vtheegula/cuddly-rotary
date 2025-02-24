import streamlit as st

def load_css():
    """
    Apply custom CSS styling
    """
    st.markdown("""
        <style>
        .stButton > button {
            width: 100%;
        }
        .upload-text {
            text-align: center;
            padding: 20px;
        }
        .st-emotion-cache-16idsys p {
            font-size: 16px;
        }
        </style>
    """, unsafe_allow_html=True)

def initialize_session_state():
    """
    Initialize session state variables
    """
    if 'current_data' not in st.session_state:
        st.session_state.current_data = None
    
    if 'last_analysis' not in st.session_state:
        st.session_state.last_analysis = None
    
    if 'qa_history' not in st.session_state:
        st.session_state.qa_history = []
