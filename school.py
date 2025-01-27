import streamlit as st
from datetime import datetime

# Function to handle file uploads, display content as a post, and add reactions
def upload_and_display_file_as_post_with_reaction(menu_key):
    # Use session state to store uploaded files and reactions for each menu
    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = {}
    if "reactions" not in st.session_state:
        st.session_state.reactions = {}

    st.subheader(f"Upload a file for {menu_key}")
    
    # File uploader
    uploaded_file = st.file_uploader(f"Upload a file for {menu_key}", key=menu_key)
    
    if uploaded_file:
        # Save the uploaded file and current timestamp in session state
        st.session_state.uploaded_files[menu_key] = {
            "file": uploaded_file,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        # Initialize reactions for the menu key
        st.session_state.reactions[menu_key] = 0
        st.success(f"File for {menu_key} uploaded successfully!")

    # Show uploaded file content as a post if available
    if menu_key in st.session_state.uploaded_files:
        uploaded_data = st.session_state.uploaded_files[menu_key]
        file_content = uploaded_data["file"].getvalue().decode("utf-8")  # Assuming text file. Adjust for other formats.
        timestamp = uploaded_data["timestamp"]

        # Display the file content in a styled "post" format with timestamp
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

        # Add heart reaction
        col1, col2 = st.columns([0.1, 0.9])  # Create two columns for the heart icon and reaction count
        with col1:
            if st.button("❤️", key=f"heart_{menu_key}"):
                st.session_state.reactions[menu_key] += 1  # Increment the reaction count

        with col2:
            st.write(f"{st.session_state.reactions[menu_key]} Reactions")

# Define individual functions for each menu option
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

def display_results():
    st.header('Results')
    upload_and_display_file_as_post_with_reaction('Results')

# Main function
def main():
    # Set the title of the web app
    st.title('School App')

    # Create a sidebar for the menu
    menu = st.sidebar.selectbox('Menu', ['Posts', 'Announcements', 'Homework', 'Exam Schedule', 'Results'])

    # Display the content based on menu selection
    if menu == 'Posts':
        display_posts()
    elif menu == 'Announcements':
        display_announcements()
    elif menu == 'Homework':
        display_homework()
    elif menu == 'Exam Schedule':
        display_exam_schedule()
    elif menu == 'Results':
        display_results()

# Run the main function
if __name__ == '__main__':
    main()
