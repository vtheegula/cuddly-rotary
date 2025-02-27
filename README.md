# CSV Analyzer with AI

A powerful Streamlit web application designed for intuitive CSV data analysis, leveraging AI to transform raw data into meaningful insights. The application provides users with advanced analytical capabilities, interactive visualizations, and intelligent Q&A functionality.

## Features

- 📤 Upload and preview CSV data
- 📊 Analyze data patterns and insights using AI
- 💬 Ask follow-up questions about your data
- 📝 Track question & answer history
- 🔒 Secure API integration

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install streamlit openai pandas python-dotenv
```

3. Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

4. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Upload your CSV file using the file uploader
2. Preview your data in the interactive table
3. Click "Analyze with AI" to get insights about your data
4. Ask follow-up questions about your data in the new window
5. View your Q&A history below

## Technologies Used

- Streamlit framework
- OpenAI GPT integration
- Python data analysis libraries
- Responsive web interface

## License

This project is licensed under the MIT License - see the LICENSE file for details.
