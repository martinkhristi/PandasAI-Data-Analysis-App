import streamlit as st
import pandas as pd
from pandasai import Agent
import os

def main():
    st.title("PandasAI Data Analysis App")

    # Input field for the PandasAI API Key
    api_key = st.text_input("Enter your PANDASAI_API_KEY:", type="password")

    if api_key:
        os.environ["PANDASAI_API_KEY"] = api_key
        st.success("PANDASAI_API_KEY set successfully!")
    else:
        st.warning("Please enter your PANDASAI_API_KEY to start using the app.")

    # File upload
    uploaded_file = st.file_uploader("Upload your CSV or Excel file:", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Determine file type and read data
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            data = pd.read_excel(uploaded_file)

        st.write("### Uploaded Data Preview")
        st.dataframe(data.head())

        # Initialize PandasAI Agent
        agent = Agent(data)

        # Input for the user's query
        query = st.text_input("Enter your analysis question:")

        if query:
            try:
                # Perform analysis using PandasAI
                response = agent.chat(query)
                st.write("### PandasAI Response:")
                st.write(response)
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
