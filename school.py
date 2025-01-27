import streamlit as st

# Function to handle file uploads and display content as a post
def upload_and_display_file_as_post(menu_key):
    # Use session state to store uploaded files for each menu
    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = {}

    st.subheader(f"Upload a file for {menu_key}")
    
    # File uploader
    uploaded_file = st.file_uploader(f"Upload a file for {menu_key}", key=menu_key)
    
    if uploaded_file:
        # Save the uploaded file in session state under the current menu key
        st.session_state.uploaded_files[menu_key] = uploaded_file
        st.success(f"File for {menu_key} uploaded successfully!")

    # Show uploaded file content as a post if available
    if menu_key in st.session_state.uploaded_files:
        uploaded_file = st.session_state.uploaded_files[menu_key]
        file_content = uploaded_file.getvalue().decode("utf-8")  # Assuming text file. For other formats, adjust as needed.

        # Display the file content in a styled "post" format
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
        </div>
        """, unsafe_allow_html=True)

# Define individual functions for each menu option
def display_posts():
    st.header('Posts')
    upload_and_display_file_as_post('Posts')

def display_announcements():
    st.header('Announcements')
    upload_and_display_file_as_post('Announcements')

def display_homework():
    st.header('Homework')
    upload_and_display_file_as_post('Homework')

def display_exam_schedule():
    st.header('Exam Schedule')
    upload_and_display_file_as_post('Exam Schedule')

def display_results():
    st.header('Results')
    upload_and_display_file_as_post('Results')

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
