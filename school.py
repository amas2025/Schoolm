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

    if "posts" not in st.session_state:
        st.session_state.posts = []

    new_post = st.text_area("Write a new post:")
    if st.button("Submit Post"):
        if new_post.strip():
            st.session_state.posts.append({
                "content": new_post.strip(),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success("Your post has been submitted!")
        else:
            st.error("Post cannot be empty!")

    if st.session_state.posts:
        st.write("### Recent Posts")
        for post in reversed(st.session_state.posts):
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

    if "announcements" not in st.session_state:
        st.session_state.announcements = []

    new_announcement = st.text_area("Write a new announcement:")
    if st.button("Submit Announcement"):
        if new_announcement.strip():
            st.session_state.announcements.append({
                "content": new_announcement.strip(),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success("Your announcement has been submitted!")
        else:
            st.error("Announcement cannot be empty!")

    if st.session_state.announcements:
        st.write("### Recent Announcements")
        for announcement in reversed(st.session_state.announcements):
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

            if "Name" not in df.columns or "Marks" not in df.columns:
                st.error("The Excel file must contain 'Name' and 'Marks' columns.")
                return

            df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
            df["Grade"] = df["Marks"].apply(assign_grade)

            st.write("### Processed Results Table")
            st.dataframe(df.style.applymap(
                lambda x: "color: red;" if x == "Failed" else "", subset=["Grade"]
            ), use_container_width=True)

        except Exception as e:
            st.error("An error occurred while processing the file.")
            st.exception(e)

# Enhanced Navigation Bar
def enhanced_navigation():
    # Sidebar Header
    st.sidebar.markdown("<h4 style='text-align: center; margin-bottom: 20px;'>📚 Navigation</h4>", unsafe_allow_html=True)

    # Sidebar Navigation Menu
    menu = st.sidebar.radio(
        "Navigate to",
        ["📜 Posts", "📢 Announcements", "📂 Homework", "📅 Exam Schedule", "📊 Results"],
        label_visibility="collapsed"
    )
    return menu

# Main function
def main():
    st.title("🏫 School App")

    # Enhanced Navigation
    menu = enhanced_navigation()

    if "Posts" in menu:
        display_posts()
    elif "Announcements" in menu:
        display_announcements()
    elif "Homework" in menu:
        display_homework()
    elif "Exam Schedule" in menu:
        display_exam_schedule()
    elif "Results" in menu:
        display_results()

if __name__ == "__main__":
    main()
