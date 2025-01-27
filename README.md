```
# LLM-R-D

## Overview

This repository contains various projects utilizing Large Language Models (LLMs). The projects leverage different tools and technologies to build applications involving natural language processing and machine learning.

## Projects

### 1. LLM Chat App

This project is a chatbot application built using Streamlit, LangChain, and OpenAI's LLM model. The app allows users to upload PDF files and interact with the content using natural language queries.

#### Features

- Upload and parse PDF files.
- Split text into manageable chunks for processing.
- Generate embeddings using OpenAI's API.
- Store and retrieve embeddings using FAISS.
- Answer user queries based on the content of the PDF.

#### How to Run

1. Clone the repository.
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up environment variables in a `.env` file:
    ```dotenv
    OPENAI_API_KEY=your_open_ai_api_key
    ```
4. Run the Streamlit app:
    ```bash
    streamlit run New\ folder/app1.py
    ```

### 2. Smart ATS System (Application Tracking System)

This project is an application that evaluates resumes against job descriptions using Google's generative AI model. It helps job seekers improve their resumes by providing feedback on matching percentages and missing keywords.

#### Features

- Upload and parse PDF resumes.
- Use a prompt template to interact with Google's generative AI.
- Provide feedback on resume and job description matching.

#### How to Run

1. Clone the repository.
2. Install the required dependencies:
    ```bash
    pip install -r Smart\ ATS\ system\ \(Application\ Tracking\ System\)/requirements.txt
    ```
3. Set up environment variables in a `.env` file:
    ```dotenv
    GOOGLE_API_KEY=your_google_api_key
    ```
4. Run the Streamlit app:
    ```bash
    streamlit run Smart\ ATS\ system\ \(Application\ Tracking\ System\)/app.py
    ```

## Repository Structure

- `.env`: Environment variables configuration file.
- `New folder/app1.py`: Source code for the LLM Chat App.
- `New folder/config.yaml`: Configuration file for API keys.
- `README.md`: This README file.
- `Smart ATS system (Application Tracking System)/app.py`: Source code for the Smart ATS System.
- `Smart ATS system (Application Tracking System)/requirements.txt`: Dependencies for the Smart ATS System.
- `app.py`: Main application file for the LLM Chat App.

## Dependencies

- Streamlit
- LangChain
- OpenAI API
- FAISS
- PyPDF2
- dotenv
- google-generativeai
- pdf2image

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [OpenAI](https://platform.openai.com/docs/models)
- [Google Generative AI](https://ai.google/)

Made with ❤️ by [Prompt Engineer](https://youtube.com/@engineerprompt)
```

Feel free to customize this README file further to suit your specific needs. Let me know if there are any additional details you would like to include.
