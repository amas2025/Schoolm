import streamlit as st

# Define individual functions for each menu option
def display_posts():
    st.header('Posts')
    st.write('Here you can find the latest posts from the school.')

def display_announcements():
    st.header('Announcements')
    st.write('Here you can find the latest announcements from the school.')

def display_homework():
    st.header('Homework')
    st.write('Here you can find the homework assignments.')

def display_exam_schedule():
    st.header('Exam Schedule')
    st.write('Here you can find the exam schedule.')

def display_results():
    st.header('Results')
    st.write('Here you can find the exam results.')

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
