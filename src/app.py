import streamlit as st
import pandas as pd
import openai
import io
import os

# Retrieve the OpenAI API key from environment variables
api_key_env = os.getenv("OPENAI_API_KEY")
# Set Streamlit page title
st.title("YouTube Comments Sentiment Labeling")
st.write(
    """
    Upload an Excel file with YouTube comments, provide your OpenAI API key, and 
    specify the prompt for sentiment classification. 
    The app will call the OpenAI API to classify each comment into a sentiment label.
    """
)

# 1) Text input for API key
api_key = st.text_input("OpenAI API Key (required)", type="password")

# 2) File uploader for Excel
uploaded_file = st.file_uploader("Upload an Excel file with comments", type=["xlsx"])

# 3) Text area for the prompt template
default_prompt = (
    "Classify the text into neutral, negative, or positive. "
    "Just return a single word among neutral, negative, or positive."
)

prompt_template = st.text_area(
    "Prompt Template",
    value=default_prompt,
    help="Adjust this prompt if you want to customize how the classification is performed."
)

# A button to trigger the sentiment labeling process
if st.button("Start Labeling"):
    # -- Basic checks first
    if not api_key:
        st.error("Please provide your OpenAI API key.")
    elif not uploaded_file:
        st.error("Please upload an Excel file.")
    elif not prompt_template.strip():
        st.error("Please provide a valid prompt template.")
    else:
        # -- Read the Excel file into a DataFrame
        try:
            df = pd.read_excel(uploaded_file, header=None)
        except Exception as e:
            st.error(f"Error reading the Excel file: {e}")
            st.stop()

        # You can rename columns for clarity 
        # (assuming the first column is ID and the second column is the comment text)
        if df.shape[1] < 2:
            st.error("Excel file must have at least two columns: [ID, Comment]")
            st.stop()
        df.columns = ["ID", "Comment"] + list(df.columns[2:])

        # -- Initialize OpenAI with the provided API key
        openai.api_key = api_key

        # -- List to collect results
        lst_rs = []

        # -- Iterate through DataFrame rows
        with st.spinner("Processing... Please wait."):
            for i in range(len(df)):
                myno = df.iloc[i]["ID"]
                mysentence = str(df.iloc[i]["Comment"])  # Convert to string if not

                try:
                    # -- Construct the final prompt
                    #    We append the user’s text to the prompt template
                    user_content = f"{prompt_template}\nText: {mysentence}"

                    # -- OpenAI API call for text classification
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
                        messages=[
                            {
                                "role": "user",
                                "content": user_content
                            }
                        ]
                    )

                    # Extract result and store it
                    result = response["choices"][0]["message"]["content"].strip()
                    lst_rs.append([myno, mysentence, result])

                except Exception as e:
                    st.error(f"Error processing row {i}: {e}")
                    lst_rs.append([myno, mysentence, "Error"])

        # -- Convert results list to a DataFrame
        result_df = pd.DataFrame(lst_rs, columns=["ID", "Comment", "Sentiment"])

        # -- Show DataFrame in Streamlit
        st.write("### Classification Results")
        st.dataframe(result_df)

        # -- Save to CSV in memory and offer download
        csv_buffer = io.StringIO()
        result_df.to_csv(csv_buffer, index=False, encoding="utf-8-sig")
        st.download_button(
            label="Download Results as CSV",
            data=csv_buffer.getvalue(),
            file_name="sentiment_analysis_results.csv",
            mime="text/csv"
        )

        st.success("Processing completed and results are ready!")
