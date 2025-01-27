import streamlit as st

# Function to handle file uploads and display uploaded files
def upload_and_display_file(menu_key):
    # Use session state to store uploaded files for each menu
    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = {}

    st.write(f"Upload files for {menu_key}")
    
    # File uploader
    uploaded_file = st.file_uploader(f"Upload a file for {menu_key}", key=menu_key)
    
    if uploaded_file:
        # Save the uploaded file in session state under the current menu key
        st.session_state.uploaded_files[menu_key] = uploaded_file
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    
    # Show uploaded file if available
    if menu_key in st.session_state.uploaded_files:
        st.write("Uploaded File:")
        uploaded_file = st.session_state.uploaded_files[menu_key]
        st.write(f"Filename: {uploaded_file.name}")
        st.write("File Content:")
        st.write(uploaded_file.getvalue().decode("utf-8"))  # Assuming text file. For other formats, handle appropriately.

# Define individual functions for each menu option
def display_posts():
    st.header('Posts')
    upload_and_display_file('Posts')

def display_announcements():
    st.header('Announcements')
    upload_and_display_file('Announcements')

def display_homework():
    st.header('Homework')
    upload_and_display_file('Homework')

def display_exam_schedule():
    st.header('Exam Schedule')
    upload_and_display_file('Exam Schedule')

def display_results():
    st.header('Results')
    upload_and_display_file('Results')

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
