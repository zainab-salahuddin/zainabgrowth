#streamlit
import streamlit as st 

st.set_page_config(page_title= "groth mindset project", project_icon="★")
st.title("Growth Mind Challange: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powred app helps you build a growth mindset with reflection, challenges, and achievements! ⭐")

#quote section
st.header("💡 Today's Growth Mindset Quote")
st.write("Sucess is not final, failure is not fatel: it is the courage to continue that counts.")

st.header("🔍 What's Your Challenge Today?")
user_input= st.text_input("Describe a challenge you're facing:")


#condition 
if user_input:
    st.sucess(f"💪🏻You're facing: {user_input}. Keep pushing forword toword your goals!🎯")
else: 
    st.warning("Tell us about your challenge to get started!")

#reflexing    
st.header("🧠Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.sucess(f"✨Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on your past experiance help you grow! Share your difficulties")

#achievements
st.header("🏆 Celebrate Your Wins!")    
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.sucess(f"🌠Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share on now😍")    


#footer 
st.write("- - -")    
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination!✨")
st.write("**⭐ Created by Zainab Salahuddin💖**")