import streamlit as st
import pandas as pd

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

# Function to upload and process results
def upload_and_display_results():
    st.header("Results")
    st.subheader("Upload an Excel file with 'Name' and 'Marks' columns")

    # File uploader for Excel files
    uploaded_file = st.file_uploader("Upload an Excel file (.xlsx or .xls)", type=["xlsx", "xls"])

    if uploaded_file:
        try:
            # Read the Excel file
            df = pd.read_excel(uploaded_file)

            # Validate columns
            if "Name" not in df.columns or "Marks" not in df.columns:
                st.error("The Excel file must have 'Name' and 'Marks' columns.")
                return

            # Process the marks and calculate grades
            df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
            df["Grade"] = df["Marks"].apply(assign_grade)

            # Display the results table
            st.write("**Processed Results Table:**")
            st.dataframe(df.style.applymap(lambda x: "color: red;" if x == "Failed" else "", subset=["Grade"]))

        except Exception as e:
            # Display error messages
            st.error("An error occurred while processing the file.")
            st.exception(e)

# Main function
def main():
    st.title("School App")

    # Sidebar menu
    menu = st.sidebar.radio("Menu", ["Posts", "Announcements", "Homework", "Exam Schedule", "Results"])

    if menu == "Results":
        upload_and_display_results()
    else:
        st.write(f"You selected {menu}. Content for this section is not implemented.")

if __name__ == "__main__":
    main()
