import streamlit as st
import pandas as pd
from datetime import datetime

# Function to assign grades based on marks
def assign_grade(marks):
    if marks < 50:
        return "Failed"
    elif 50 <= marks < 60:
        return "C"
    elif 60 <= marks < 70:
        return "B"
    elif 70 <= marks < 80:
        return "B+"
    elif 80 <= marks < 90:
        return "A"
    elif 90 <= marks <= 100:
        return "A+"
    else:
        return "Invalid Marks"

# Function to handle file uploads and process results
def upload_and_display_results():
    st.header("Results")
    st.subheader("Upload an Excel file with students' marks (Name and Marks)")

    # File uploader for Excel files
    uploaded_file = st.file_uploader("Upload an Excel file (.xlsx or .xls)", type=["xlsx", "xls"], key="results")

    if uploaded_file:
        try:
            # Debug: Display file details
            st.write("**Uploaded File Details:**")
            st.write(f"File Name: {uploaded_file.name}")
            st.write(f"File Type: {uploaded_file.type}")
            
            # Read the Excel file into a DataFrame
            df = pd.read_excel(uploaded_file)

            # Debug: Display raw DataFrame
            st.write("**Raw Data:**")
            st.dataframe(df)

            # Check for required columns
            if "Name" not in df.columns or "Marks" not in df.columns:
                st.error("The Excel file must have 'Name' and 'Marks' columns.")
                return

            # Convert Marks to numeric and handle errors
            df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
            df["Grade"] = df["Marks"].apply(assign_grade)  # Apply grade classification

            # Display the DataFrame as an advanced table
            st.write("**Student Results Table:**")
            st.dataframe(df.style.applymap(
                lambda x: "color: red;" if x == "Failed" else "",
                subset=["Grade"]
            ))

        except Exception as e:
            # Display error message and exception details
            st.error("An error occurred while processing the file.")
            st.exception(e)

# Main function
def main():
    st.title('School App')

    # Sidebar menu buttons
    if st.sidebar.button('Results'):
        upload_and_display_results()

if __name__ == '__main__':
    main()
