import streamlit as st
st.set_page_config(page_title="Text File Analyzer", layout="centered")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"
def analyze_text(file_content):
    lines = file_content.splitlines()
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = len(file_content)
    return num_lines, num_words, num_chars

def create_summary(num_lines, num_words, num_chars):
    return f"Lines: {num_lines}\nWords: {num_words}\nCharacters: {num_chars}\n"

VALID_USERNAME = "Rameen"
VALID_PASSWORD = "1234"
def login_page():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.session_state.page = "upload"
            st.success("Login successful! Proceed to file upload.")
            st. rerun()
        else:
            st.error("Invalid username or password.")

def upload_page():
    st.title(" Text File Analyzer")

    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    
    if uploaded_file:
        file_content = uploaded_file.read().decode("utf-8")

        st.subheader("File Content")
        st.text(file_content)

        num_lines, num_words, num_chars = analyze_text(file_content)

        st.subheader("File Statistics")
        st.write(f"**Total Lines:** {num_lines}")
        st.write(f"**Total Words:** {num_words}")
        st.write(f"**Total Characters:** {num_chars}")

        summary = create_summary(num_lines, num_words, num_chars)

        st.download_button(
            label="Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )

    st.button("Logout", on_click=logout)
def logout():
    st.session_state.logged_in = False
    st.session_state.page = "login"
    st.experimental_rerun()
if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "upload":
    if st.session_state.logged_in:
        upload_page()
    else:
        st.session_state.page = "login"
        st.experimental_rerun()
