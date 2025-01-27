import streamlit as st
import pandas as pd
from datetime import datetime

# Predefined access key
ACCESS_KEY = "1234"

# Authentication Function
def authenticate():
    st.title("🏫 School App - Login")
    st.write("Please enter the access key to continue:")
    user_key = st.text_input("Access Key", type="password")

    if st.button("Submit"):
        if user_key == ACCESS_KEY:
            st.session_state["authenticated"] = True
            st.success("Access granted! Redirecting to the app...")
        else:
            st.error("Invalid access key. Please try again.")

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

# Other sections (Announcements, Homework, Exam Schedule, Results) remain the same...

# Enhanced Navigation Bar
def enhanced_navigation():
    st.sidebar.markdown("<h4 style='text-align: center; margin-bottom: 20px;'>📚 Navigation</h4>", unsafe_allow_html=True)

    menu = st.sidebar.radio(
        "Navigate to",
        ["📜 Posts", "📢 Announcements", "📂 Homework", "📅 Exam Schedule", "📊 Results"],
        label_visibility="collapsed"
    )
    return menu

# Main function
def main():
    # Check if the user is authenticated
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        authenticate()
    else:
        # Show the main app if authenticated
        st.title("🏫 School App")
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
