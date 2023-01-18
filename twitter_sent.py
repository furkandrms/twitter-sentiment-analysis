import json
from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from get_tweets import *
import time as ts 
from datetime import time
import matplotlib.pyplot as plt
import openai
openai.api_key = "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"
import gradio as gr
import openpyxl


#st.set_page_config(layout="wide")
st.set_page_config(page_title="Our Webpage", page_icon=":four_leaf_clover:", layout="wide")



def load_lottieurl(url: str):
    r = requests.get(url, "r")
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>/{f.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    choose = option_menu("Main Menu", ["Home", "Project", 'Who We Are', 'Chat With ChatGPT','Pomodoro'],
        icons=['house','files', 'person-lines-fill','chat','clock'], menu_icon="cast", default_index=1)
    choose

if choose == "Home":

    with st.container():
        left_column, center_column, right_column = st.columns(3)
        with left_column:
            st.write("")
        with center_column:
            lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_7uJbyxfjPR.json")

            st_lottie(lottie_hello,
                      key="hello",
                      speed=1,
                      reverse=False,
                      loop=True,
                      quality="low",
                      height=None,
                      width=300,
                      )
        with right_column:
            st.write("")

    with st.container():
        left_column,center_column,right_column = st.columns(3)
        with left_column:
            st.header(":blue[What you can find?]")
            st.write("##")

        with right_column:
            st.write("")
        with center_column:
            st.write("")
        st.markdown(
            """
            - Twitter Sentiment Analysis
                - You can analysis your tweets and see ratio how much have positive,negative and neutral. 
            - Who we are
                - You can see information about us and you can contact via linkedin with us.
            - ChatGPT Chatbox
                - This is ChatGPT, everything you need is here for you.
            """
        )

elif choose == 'Chat With ChatGPT':
    with st.container():

        st.title("Chatting with ChatGPT")
        st.sidebar.header("Instructions")
        st.sidebar.info(
            '''This is a web application that allows you to interact with 
               the OpenAI API's implementation of the ChatGPT model.
               Enter a **query** in the **text box** and **press enter** to receive 
               a **response** from the ChatGPT
               '''
        )
        model_engine = "text-davinci-003"


        def main():
            '''
            This function gets the user input, pass it to ChatGPT function and
            displays the response
            '''
            # Get user input
            user_query = st.text_input("Enter query here, to exit enter :q", "what is Python?")
            if user_query != ":q" or user_query != "":
                # Pass the query to the ChatGPT function
                response = ChatGPT(user_query)
                return st.write(f"{response}")


        def ChatGPT(user_query):
            '''
            This function uses the OpenAI API to generate a response to the given
            user_query using the ChatGPT model
            '''
            # Use the OpenAI API to generate a response
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=user_query,
                max_tokens=1024,
                n=1,
                temperature=0.5,
            )
            response = completion.choices[0].text
            return response
        main()
        #lottie_twitter = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_oahjps8u.json")

#st_lottie(lottie_twitter,
          #key="twitter",
          #speed=1,
          #reverse=False,
          #loop=True,
          #quality="low",
          #height=100,
          #width=100,
          #)

#st.set_page_config(page_title="Our Webpage", page_icon=":four_leaf_clover:", layout="wide")



#lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_oahjps8u.json")

#img_furkan = Image.open("path")
#img_melih = Image.open("path")
#img_hatice = Image.open("path")

#https://assets1.lottiefiles.com/private_files/lf30_tgzwnxcf.json
elif choose == 'Project':
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.title(":blue[Twitter Sentiment Analysis] ")
            #st.title("Twitter Sentiment Analysis")
        with right_column:
            lottie_twitter_logo = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_c5e2icko.json")
            st_lottie(lottie_twitter_logo,
                      key="hello",
                      speed=1,
                      reverse=False,
                      loop=True,
                      quality="low",
                      height=None,
                      width=300,
                      )
    with st.container():
        st.write("---")

    with st.form("my_form"):
        text_input = st.text_input(":blue[User Name]")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            get_tweets(text_input, False)
            st.write("All Tweets Are Fetched")
            df = pd.read_csv(text_input + "_tweets.csv", sep='\t', delimiter=",")
            st.dataframe(df)
        
            st.bar_chart(df.groupby(["Status"]).agg({"Score":"mean"}))

            

elif choose == 'Who We Are':
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("Hatice.jpeg", caption=None, width=200, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        with right_column:
            st.write("I am currently working at Yılport Solventas as Business Analysis and Software Support. "
                     "I am a Junior Data Scientist with nearly 1 year of experience and statistics "
                     "background in using predictive modeling, data processing algorithms and A/B testing "
                     "to solve business problems. "
                     "I am passionate about deep learning and open to development.")
            st.write("[Linkedin](https://www.linkedin.com/in/hatice-yıldız/)")

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("melihsb1.jpeg", width=200,  channels="RGB", output_format="auto")
        with right_column:
            st.write("I am currently working at Litum Technology as Mechanical Design Engineer. "
                     "I am a Junior Data Scientist with nearly 1 year of experience and statistics "
                     "background in using predictive modeling, data processing algorithms and A/B testing "
                     "to solve business problems. "
                     "I am passionate about deep learning and open to development.")
            st.write("[Linkedin](https://www.linkedin.com/in/melih-%C3%B6znalbant-b62713208/)")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("furkan.jpeg", caption=None, width=200, use_column_width=None, clamp=False, channels="RGB",
                     output_format="auto")
        with right_column:
            st.write("I am currently working KolayBi' at as Business Analyst." 
                     "I am a Junior Data Scientist with nearly 1 year of experience and mathematics"
                     " background in using predictive modeling,"
                     " data processing algorithms and A/B testing "
                     "to solve business problems." 
                     "I am passionate about deep learning and open to development.")
            st.write("[Linktree](https://linktr.ee/furkandurmus)")


    with st.container():
        st.write("---")
        st.header(":blue[Get in Touch With Us!]")

        contact_form = """
        <form action="https://formsubmit.co/melih.oznalbant92@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="False>
            <input type="text" name="name"  placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name ="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)


            def local_css(file_name):
                with open(file_name) as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            local_css("style/style.css")
        with right_column:
            st.empty()


elif choose == 'Pomodoro':
    
    def pomodoro(value):
        m,s,mm = value.split(":")
        t_s = (int(m)*60 + int(s) + int(mm)/1000)
        return t_s

    val = st.time_input("Set Timer", value=time(0,0,0))

    if str(val) == ("00:00:00"):
        st.write("Please Sent Timer")
    else: 
        sec = pomodoro(str(val))
        print(sec)
        bar = st.progress(0)
        per = sec/100
        progress_status = st.empty()
        for i in range(100): 
            bar.progress(i+1)
            progress_status.write(str(i+1) + "%")
            ts.sleep(per)
