import os
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Updated comment for clarity
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def analyze_data(df: pd.DataFrame) -> str:
    """
    Analyze the dataframe using OpenAI's GPT model
    """
    # Prepare data summary
    data_info = {
        "columns": df.columns.tolist(),
        "shape": df.shape,
        "sample": df.head(5).to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "summary": df.describe().to_dict()
    }
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """You are a data analysis expert. Analyze the given dataset and provide:
                    1. Overview of the data
                    2. Key insights and patterns
                    3. Potential areas for further investigation
                    Be concise but informative."""
                },
                {
                    "role": "user",
                    "content": f"Please analyze this dataset: {str(data_info)}"
                }
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error in AI analysis: {str(e)}")

def ask_followup_question(df: pd.DataFrame, previous_analysis: str, question: str) -> str:
    """
    Handle follow-up questions about the data
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """You are a data analysis expert. Answer questions about the dataset
                    based on the previous analysis and the data provided. Be specific and accurate."""
                },
                {
                    "role": "assistant",
                    "content": f"Previous analysis: {previous_analysis}"
                },
                {
                    "role": "user",
                    "content": f"""
                    Question: {question}
                    Dataset info: {df.info(memory_usage='deep')}
                    Dataset sample: {df.head().to_dict()}
                    """
                }
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error in processing question: {str(e)}")
