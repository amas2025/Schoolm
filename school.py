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

# Section: Posts
def display_posts():
    st.header("Posts")
    st.subheader("This is the Posts section.")
    st.write("Here you can view or manage posts from the school.")
    # Add functionality for posts (e.g., creating or displaying posts)
    st.text_area("Write a new post:")
    if st.button("Submit Post"):
        st.success("Your post has been submitted!")

# Section: Announcements
def display_announcements():
    st.header("Announcements")
    st.subheader("This is the Announcements section.")
    st.write("Here you can view or manage school announcements.")
    # Add functionality for announcements (e.g., displaying announcements)
    st.text_area("Write a new announcement:")
    if st.button("Submit Announcement"):
        st.success("Your announcement has been submitted!")

# Section: Homework
def display_homework():
    st.header("Homework")
    st.subheader("This is the Homework section.")
    st.write("Here you can upload or view homework assignments.")
    uploaded_file = st.file_uploader("Upload a homework file (.pdf, .docx, etc.)", type=["pdf", "docx", "txt"])
    if uploaded_file:
        st.success(f"{uploaded_file.name} has been uploaded successfully!")
        st.write(f"Uploaded file content: {uploaded_file.getvalue().decode('utf-8')}" if uploaded_file.type == "text/plain" else "File preview not available.")

# Section: Exam Schedule
def display_exam_schedule():
    st.header("Exam Schedule")
    st.subheader("This is the Exam Schedule section.")
    st.write("Here you can view or upload the exam schedule.")
    uploaded_file = st.file_uploader("Upload an exam schedule file (.xlsx)", type=["xlsx"])
    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)
            st.write("Uploaded Exam Schedule:")
            st.dataframe(df)
        except Exception as e:
            st.error("Error processing the uploaded file.")
            st.exception(e)

# Section: Results
def display_results():
    st.header("Results")
    st.subheader("This is the Results section.")
    st.write("Upload an Excel file with 'Name' and 'Marks' columns to display results.")
    uploaded_file = st.file_uploader("Upload an Excel file (.xlsx or .xls)", type=["xlsx", "xls"])

    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)

            # Check for required columns
            if "Name" not in df.columns or "Marks" not in df.columns:
                st.error("The Excel file must have 'Name' and 'Marks' columns.")
                return

            # Process marks and assign grades
            df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
            df["Grade"] = df["Marks"].apply(assign_grade)

            # Display the results table
            st.write("**Processed Results Table:**")
            st.dataframe(df.style.applymap(lambda x: "color: red;" if x == "Failed" else "", subset=["Grade"]))

        except Exception as e:
            st.error("An error occurred while processing the file.")
            st.exception(e)

# Main function to handle navigation and rendering
def main():
    st.title("School App")

    # Sidebar navigation
    menu = st.sidebar.radio("Menu", ["Posts", "Announcements", "Homework", "Exam Schedule", "Results"])

    # Navigation handling
    if menu == "Posts":
        display_posts()
    elif menu == "Announcements":
        display_announcements()
    elif menu == "Homework":
        display_homework()
    elif menu == "Exam Schedule":
        display_exam_schedule()
    elif menu == "Results":
        display_results()

if __name__ == "__main__":
    main()
