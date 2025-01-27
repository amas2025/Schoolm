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
    st.header("📜 Posts")
    st.write("Share and view posts below:")

    # Initialize session state for posts
    if "posts" not in st.session_state:
        st.session_state.posts = []

    # Input for new post
    new_post = st.text_area("Write a new post:")
    if st.button("Submit Post"):
        if new_post.strip():
            # Add the post to session state
            st.session_state.posts.append({
                "content": new_post.strip(),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success("Your post has been submitted!")
        else:
            st.error("Post cannot be empty!")

    # Display submitted posts
    if st.session_state.posts:
        st.write("### Recent Posts")
        for post in reversed(st.session_state.posts):  # Display most recent posts first
            st.markdown(f"""
            <div style="
                background-color: #f9f9f9; 
                padding: 15px; 
                border-radius: 10px; 
                margin-bottom: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
                <p style="font-size: 16px; color: #333; line-height: 1.6;">
                    {post['content']}
                </p>
                <p style="font-size: 12px; color: #888; text-align: right;">
                    Posted on: {post['timestamp']}
                </p>
            </div>
            """, unsafe_allow_html=True)

# Section: Announcements
def display_announcements():
    st.header("📢 Announcements")
    st.write("Share and view announcements below:")

    # Initialize session state for announcements
    if "announcements" not in st.session_state:
        st.session_state.announcements = []

    # Input for new announcement
    new_announcement = st.text_area("Write a new announcement:")
    if st.button("Submit Announcement"):
        if new_announcement.strip():
            # Add the announcement to session state
            st.session_state.announcements.append({
                "content": new_announcement.strip(),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success("Your announcement has been submitted!")
        else:
            st.error("Announcement cannot be empty!")

    # Display submitted announcements
    if st.session_state.announcements:
        st.write("### Recent Announcements")
        for announcement in reversed(st.session_state.announcements):  # Display most recent announcements first
            st.markdown(f"""
            <div style="
                background-color: #f1f1f1; 
                padding: 15px; 
                border-radius: 10px; 
                margin-bottom: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
                <p style="font-size: 16px; color: #333; line-height: 1.6;">
                    {announcement['content']}
                </p>
                <p style="font-size: 12px; color: #888; text-align: right;">
                    Announced on: {announcement['timestamp']}
                </p>
            </div>
            """, unsafe_allow_html=True)

# Section: Homework
def display_homework():
    st.header("📂 Homework")
    st.write("Upload and view homework assignments.")

    uploaded_file = st.file_uploader("Upload a homework file (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])
    if uploaded_file:
        st.success(f"**{uploaded_file.name}** has been uploaded successfully!")
        if uploaded_file.type == "text/plain":
            st.write("### File Content")
            st.text(uploaded_file.getvalue().decode("utf-8"))
        else:
            st.info("Preview is only available for text files.")

# Section: Exam Schedule
def display_exam_schedule():
    st.header("📅 Exam Schedule")
    st.write("Upload and view the exam schedule.")

    uploaded_file = st.file_uploader("Upload an exam schedule file (.xlsx)", type=["xlsx"])
    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)
            st.write("### Uploaded Exam Schedule")
            st.dataframe(df.style.highlight_max(axis=0), use_container_width=True)
        except Exception as e:
            st.error("Error processing the uploaded file.")
            st.exception(e)

# Section: Results
def display_results():
    st.header("📊 Results")
    st.write("Upload an Excel file with 'Name' and 'Marks' columns to display results.")

    uploaded_file = st.file_uploader("Upload an Excel file (.xlsx or .xls)", type=["xlsx", "xls"])
    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)

            # Validate required columns
            if "Name" not in df.columns or "Marks" not in df.columns:
                st.error("The Excel file must contain 'Name' and 'Marks' columns.")
                return

            # Assign grades
            df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
            df["Grade"] = df["Marks"].apply(assign_grade)

            # Display results table
            st.write("### Processed Results Table")
            st.dataframe(df.style.applymap(
                lambda x: "color: red;" if x == "Failed" else "", subset=["Grade"]
            ), use_container_width=True)

        except Exception as e:
            st.error("An error occurred while processing the file.")
            st.exception(e)

# Main function to handle navigation
def main():
    st.title("🏫 School App")

    # Sidebar navigation
    menu = st.sidebar.radio("Navigate", ["Posts", "Announcements", "Homework", "Exam Schedule", "Results"])

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
