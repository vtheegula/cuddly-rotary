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
    page_title="Gen-AI for Analysis",
    page_icon="📊",
    layout="wide"
)

# Load custom CSS
load_css()

# Initialize session state
initialize_session_state()

def main():
    st.title("📊 Gen-AI Analysis")

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
            st.header("3. Generate Analysis")
            if st.button("🔍 Analyze with AI", type="primary"):
                with st.spinner("Analyzing your data..."):
                    analysis = analyze_data(df)
                    st.session_state.last_analysis = analysis
                    st.session_state.analysis_data = True

                    # Open analysis in new window using JavaScript
                    js_code = """
                        <script>
                        window.open('/pages/analysis', '_blank', 'width=800,height=600');
                        </script>
                    """
                    st.markdown(js_code, unsafe_allow_html=True)
                    st.success("Analysis complete! Check the new window for results and ask follow-up questions there.")

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