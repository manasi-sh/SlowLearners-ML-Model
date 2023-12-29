"""Main module for the streamlit Dyslexia app"""

import streamlit as st
import time
from pymysql import *
from pymysql import cursors

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

#local_css("style.css")
#remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')


import home
import quiz
import survey
import login


PAGES = {
    "Login": login,
    "Home": home,
    "Quiz": quiz,
    "Survey": survey
    
}

# st.sidebar.title("Pages")
# radio = st.sidebar.radio(label="", options=["Set A", "Set B", "Add them"])

# session_state = SessionState.get(a=0, b=0)  # Pick some initial values.

# if radio == "Set A":
#     session_state.a = float(st.text_input(label="What is a?", value=session_state.a))
#     st.write(f"You set a to {session_state.a}")
# elif radio == "Set B":
#     session_state.b = float(st.text_input(label="What is b?", value=session_state.b))
#     st.write(f"You set b to {session_state.b}")
# elif radio == "Add them":
#     st.write(f"a={session_state.a} and b={session_state.b}")
#     button = st.button("Add a and b")
#     if button:
#         st.write(f"a+b={session_state.a+session_state.b}")
        

def main():

    st.sidebar.title("LearnEase")
    st.sidebar.text(" ""AI for Slow Learners"" ")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(PAGES.keys()))

    

    with st.spinner(text = f"Loading {page} ..."):
        
        PAGES[page].main()
        

    st.sidebar.title("About App")

    st.sidebar.info(
        """
        This App uses Machine Learning to Detect Slow Learners.  
        
        """
    )
# It uses Streamlit for implemention of beatiful and easy web app.
#     st.sidebar.title("Contact Developer")
#     st.sidebar.info(
#         """
#         This app is develop by Dyslexiaworkin Organization. You can contact us at
#         [Dyslexiaworkin](https://github.com/dyslexiaworkin).
# """
#     )

   #st.sidebar.markdown("[![Github](https://github.com/aryanc55/NLPJenny/blob/master/assests/github.png?raw=true)](https://github/aryanc55)")

    # st.sidebar.markdown(
    #     """  [Github](https://github.com/dyslexiaworkin)""")  # change all thses three to  to iamge
    # st.sidebar.markdown("""  [Twitter](https://twitter.com/aryanc55)""")
    

    # st.sidebar.title("Souce Code")
    # st.sidebar.info(
    #     "This an free to use template repository and you are very welcome to **contribute** your awesome "
    #     "comments, questions, resources and apps as "
    #     "[issues](https://github.com/dyslexiaworkin/DyslexiaML/issues) of or "
    #     "[pull requests](https://github.com/dyslexiaworkin/DyslexiaML/pulls) "
    #     "to the [source code](https://github.com/dyslexiaworkin/DyslexiaML). "
    # )


if __name__ == "__main__":
    main()
