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
    st.subheader("Upload a text file with students' marks (Name and Marks)")

    # File uploader for .txt files
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"], key="results")

    if uploaded_file:
        try:
            # Read the file content into a DataFrame
            # Assuming the .txt file is comma-separated or tab-separated
            df = pd.read_csv(uploaded_file, delimiter=",|\\t", engine="python")  # Handles both comma and tab separators

            # Check for required columns
            if "Name" not in df.columns or "Marks" not in df.columns:
                st.error("The file must have 'Name' and 'Marks' columns.")
                return

            # Convert Marks to numeric and handle errors
            df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
            df["Grade"] = df["Marks"].apply(assign_grade)  # Apply grade classification

            # Display the DataFrame as an advanced table
            st.write("**Student Results Table**")
            st.dataframe(df.style.applymap(
                lambda x: "color: red;" if x == "Failed" else "",
                subset=["Grade"]
            ))

        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")

# Other menu handlers
def display_posts():
    st.header('Posts')
    upload_and_display_file_as_post_with_reaction('Posts')

def display_announcements():
    st.header('Announcements')
    upload_and_display_file_as_post_with_reaction('Announcements')

def display_homework():
    st.header('Homework')
    upload_and_display_file_as_post_with_reaction('Homework')

def display_exam_schedule():
    st.header('Exam Schedule')
    upload_and_display_file_as_post_with_reaction('Exam Schedule')

# Helper function to handle generic uploads
def upload_and_display_file_as_post_with_reaction(menu_key):
    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = {}
    if "reactions" not in st.session_state:
        st.session_state.reactions = {}

    st.subheader(f"Upload a file for {menu_key}")
    uploaded_file = st.file_uploader(f"Upload a file for {menu_key}", key=menu_key)
    
    if uploaded_file:
        st.session_state.uploaded_files[menu_key] = {
            "file": uploaded_file,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        st.session_state.reactions[menu_key] = 0
        st.success(f"File for {menu_key} uploaded successfully!")

    if menu_key in st.session_state.uploaded_files:
        uploaded_data = st.session_state.uploaded_files[menu_key]
        file_content = uploaded_data["file"].getvalue().decode("utf-8")
        timestamp = uploaded_data["timestamp"]

        st.markdown(f"""
        <div style="
            background-color: #f9f9f9; 
            padding: 15px; 
            border-radius: 10px; 
            border: 1px solid #ddd;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);">
            <p style="font-size: 16px; color: #333; line-height: 1.6;">
                {file_content}
            </p>
            <p style="font-size: 12px; color: #666; text-align: right;">
                Uploaded on: {timestamp}
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            if st.button("❤️", key=f"heart_{menu_key}"):
                st.session_state.reactions[menu_key] += 1

        with col2:
            st.write(f"{st.session_state.reactions[menu_key]} Reactions")

# Main function
def main():
    st.title('School App')

    # Sidebar menu buttons
    if st.sidebar.button('Posts'):
        display_posts()
    if st.sidebar.button('Announcements'):
        display_announcements()
    if st.sidebar.button('Homework'):
        display_homework()
    if st.sidebar.button('Exam Schedule'):
        display_exam_schedule()
    if st.sidebar.button('Results'):
        upload_and_display_results()

if __name__ == '__main__':
    main()
