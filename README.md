# AI-Powered CSV Data Analyzer

A powerful Streamlit web application designed for intuitive CSV data analysis, leveraging AI to transform raw data into meaningful insights.

## Features

- Upload and preview CSV files
- AI-powered data analysis
- Interactive Q&A with your data
- Detailed visualizations
- Multi-window interface for better organization

## Setup Instructions

1. Clone this repository
2. Create a `.env` file based on `.env.example`
3. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/account/api-keys)
4. Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:5000`

## Environment Variables

Copy `.env.example` to `.env` and update the values:
- `OPENAI_API_KEY`: Your OpenAI API key (required)

## Note

Make sure to never commit your actual API keys or sensitive information to version control. The `.env` file is included in `.gitignore` for this purpose.
