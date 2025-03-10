# YouTube Comments Sentiment Labeling App

A simple **Streamlit** application that uses the **OpenAI** API to classify YouTube comments by sentiment (e.g., *neutral*, *negative*, *positive*). Users can upload an Excel file containing comments, provide their OpenAI API key, and specify a prompt to guide the classification.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Author](#Alaa Alawdi)
- [License](#license)

---



## Overview

This application allows you to:
1. **Input** your OpenAI API key.
2. **Upload** an Excel file (\*.xlsx) containing YouTube comments.
3. **Provide** a custom prompt (with a default prompt given).
4. **Run** the classification using OpenAI’s GPT-3.5-turbo model (or GPT-4 if you have access).
5. **Download** the results as a CSV file.

It utilizes **Streamlit** for the web interface and **pandas** for data handling.

---

## Features

- **Simple File Upload**: Drag-and-drop or browse for your Excel file.
- **Custom Prompting**: Tailor your prompt to your specific sentiment categories or tasks.
- **Real-Time Progress**: View real-time status messages during classification.
- **Download Results**: Export labeled data as a CSV file.

---

## Requirements

1. **Python** 3.7 or higher
2. **pip** (Python package manager)
3. The following Python libraries:
   - [streamlit](https://streamlit.io/)
   - [pandas](https://pandas.pydata.org/)
   - [openai](https://pypi.org/project/openai/)
   - [openpyxl](https://pypi.org/project/openpyxl/) (for reading `.xlsx` files)
   - [io] (part of the Python standard library)
   - [os] (part of the Python standard library)

---
# How to Install

Below are step-by-step instructions to install and set up the project’s dependencies:

1. **Clone or download** this repository:
    ```bash
    git clone https://github.com/ALaaAlawdi/Yutube-Comments-Labeling.git
    cd Yutube-Comments-Labeling
    ```

2. **Create and activate a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```
    - On **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - On **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

3. **Install required packages** (recommended method using a requirements file):
    ```bash
    pip install -r requirements.txt
    ```
    If you don’t have a `requirements.txt` file, install the libraries manually:
    ```bash
    pip install streamlit pandas openai openpyxl
    ```

4. **Set your OpenAI API Key** if needed:
    ```bash
    export OPENAI_API_KEY="your-api-key-here"
    ```
    Alternatively, you can simply enter your key in the Streamlit text input when prompted.

5. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

6. **Open your browser**:
    - The app usually starts at [http://localhost:8501](http://localhost:8501).
    - Use the app interface to upload your Excel file and enter your OpenAI API Key.


    ## Usage

    To run the application using Docker, follow these steps:

    1. **Build the Docker image**:
        ```bash
        docker build -t streamlit_image .
        ```

    2. **Run the Docker container**:
        ```bash
        docker run --name streamlit_container -p 8501:8501 -d -v %cd%:/app streamlit_image
        ```

    3. **Open your browser**:
        - The app usually starts at [http://localhost:8501](http://localhost:8501).
        - Use the app interface to upload your Excel file and enter your OpenAI API Key.

    ---


    ## Docker Compose

    To run the application using Docker Compose, follow these steps:

    1. **Create a `docker-compose.yml` file** in the root directory of your project with the following content:
        ```yaml
        version: '3.8'

        services:
          streamlit:
            image: streamlit_image
            build: .
            ports:
              - "8501:8501"
            volumes:
              - .:/app
        ```

    2. **Build and start the application** using Docker Compose:
        ```bash
        docker-compose up --build
        ```

    3. **Open your browser**:
        - The app usually starts at [http://localhost:8501](http://localhost:8501).
        - Use the app interface to upload your Excel file and enter your OpenAI API Key.
