import streamlit as st
from PIL import Image
import time
from datetime import datetime
img2 =Image.open(r"C:\Users\shash\OneDrive\Documents\Black and White Minimalist Modern Clean Technology Logo .png")
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #845AFF;
    color:#ffffff;
}
div.stButton > button:hover {`
    background-color: #4200FF;
    color:#ffffff;
    }
</style>""", unsafe_allow_html=True)
def eentry():
    st.text_input("Enter Title")
    st.text_area("Enter Description")
def pred_tab0():
    st.write("CHOOSE TEMPLATE")
def pred_tab2():
    st.markdown(
        "<h2 style='text-align: left; color: black;'>Education</h2>",
        unsafe_allow_html=True)
    a1, a2 = st.columns(2)
    with a2:
        img = Image.open(r"C:\Users\shash\Downloads\Resume\logo\Black White Minimalist CV Resume.png")
        st.image(img, use_column_width=True)
    with a1:
        st.text_input("Education",key=999999)
        w1,w2=st.columns(2)
        with w1:
            st.text_input("School/College/university",key=98765432)
        with w2:
            st.text_input("City",key=23456789)
        w1, w2 = st.columns(2)
        with w1:
            st.write("Start Date")
            year = st.selectbox('Year', range(1990, 2030),key=7777)
            month = st.selectbox('Month', range(1, 13),key=7654)
        with w2:
            st.write("End Date")
            year = st.selectbox('Year', range(1990, 2030), key=2312)
            month = st.selectbox('Month', range(1, 13),key=6323)
        st.text_area("Enter Description",key=7867)
def pred_tab3():
    st.markdown(
        "<h2 style='text-align: left; color: black;'>Experience</h2>",
        unsafe_allow_html=True)
    a1, a2 = st.columns(2)
    with a2:
        img = Image.open(r"C:\Users\shash\Downloads\Resume\logo\Black White Minimalist CV Resume.png")
        st.image(img, use_column_width=True)
    with a1:
        st.text_input("Enter position", key=9876)
        w1, w2 = st.columns(2)
        with w1:
            st.text_input("Company/Organisation", key=44)
        with w2:
            st.text_input("City", key=98)
        w1, w2 = st.columns(2)
        with w1:
            st.write("Start Date")
            year = st.selectbox('Year', range(1990, 2030), key=999)
            month = st.selectbox('Month', range(1, 13), key=123434)
        with w2:
            st.write("End Date")
            year = st.selectbox('Year', range(1990, 2030), key=73)
            month = st.selectbox('Month', range(1, 13), key=6)
        st.text_area("Enter Description", key=27)
def pred_tab1():
    st.markdown(
        "<h2 style='text-align: left; color: black;'>Personal Details</h2>",
        unsafe_allow_html=True)
    with st.form(" ", clear_on_submit=False):
        a1, a2 = st.columns([2, 2])
        with a1:
            s1, s2 = st.columns(2)
            with s1:
                name = st.text_input("Given Name")
            with s2:
                fname = st.text_input("Family Name")
            st.text_input("Enter Email")
            st.text_input("Headline")
            st.text_input("Phone Number")
            st.text_input("Enter Linkedin")
            st.text_input("Any other link   GITHUB/PORTFOLIO etc")
        with a2:
            img = Image.open(r"C:\Users\shash\Downloads\Resume\logo\Black White Minimalist CV Resume.png")
            st.image(img, use_column_width=True)
        next = st.form_submit_button("Next")
        if (next):
            pred_tab2()
def pred_tab4():
    st.markdown(
        "<h2 style='text-align: left; color: black;'>Skills</h2>",
        unsafe_allow_html=True)
    a1, a2 = st.columns(2)
    with a2:
        img = Image.open(r"C:\Users\shash\Downloads\Resume\logo\Black White Minimalist CV Resume.png")
        st.image(img, use_column_width=True)
    with a1:
        st.multiselect("Enter Skills",["Java", "C++", "Python","Agile", "Scrum", "Waterfall","HTML", "CSS", "JavaScript", "React", "Angular", "Vue.js","MySQL", "MongoDB", "PostgreSQL", "Oracle", "AWS", "Azure", "Google Cloud Platform","Git", "Subversion"," JUnit"," pytest","Data structures"," algorithms","Problem-solving skills","Analytical skills","Communication and collaboration skills","Object-oriented programming","Mobile app development (iOS, Android)","Artificial Intelligence and Machine Learning","Natural Language Processing (NLP)","Big Data Analytics","Computer Networks and Security","Operating Systems and System Administration","Software Architecture and Design","Debugging and Troubleshooting","Continuous Integration and Deployment (CI/CD) tools and processes.","express.js","mern","mean","angular","vanilla.js","node","ruby","flask","django","Vue.js","Firebase","wordpress","drupal","Docker","Kubernetes","Materialize","Bootsrap","Bulma","PHP","GraphQl","Restful API","Google Analytics","Mixmanel","Selenium","Cypress","Jest","Blockchain","Etherium","Replit","Smart Copntracts"])
def pred_tab6():
    st.markdown(
        "<h2 style='text-align: left; color: black;'>Extra Curricular</h2>",
        unsafe_allow_html=True)
    a1, a2 = st.columns(2)
    with a2:
        img = Image.open(r"C:\Users\shash\Downloads\Resume\logo\Black White Minimalist CV Resume.png")
        st.image(img, use_column_width=True)
    with a1:
        st.text_input("Enter Title", key=3)
        st.text_area("Enter Description", key=4)
        st.write("\n")
        st.text_input("Enter Title *(optional)*")
        st.text_area("Enter Description *(optional)*")


def pred_tab5():
    st.markdown(
        "<h2 style='text-align: left; color: black;'>Projects</h2>",
        unsafe_allow_html=True)
    a1, a2 = st.columns(2)
    with a2:
        img = Image.open(r"C:\Users\shash\Downloads\Resume\logo\Black White Minimalist CV Resume.png")
        st.image(img, use_column_width=True)
    with a1:
        st.text_input("Enter Title", key=1)
        st.text_area("Enter Description", key=2)
        st.text_input("Enter Title *(optional)*",key=7)
        st.text_area("Enter Description *(optional)*",key=8)

st.sidebar.image(img2,use_column_width=True)
home=st.sidebar.button("Home",use_container_width=True,type="primary")
resume=st.sidebar.button("Resume Builder",use_container_width=True)
cover_letter=st.sidebar.button("Cover Letter",use_container_width=True)
analyzer=st.sidebar.button("Resume Analyzer",use_container_width=True)
job_board=st.sidebar.button("Job Board",use_container_width=True)
if (home):
    st.markdown("<h1 style='text-align: center; color: black;'>ResuMate</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: blue;'><i>Only 2% of resumes make it past the first round. Be in the top 2%</i></h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'>Use professional field-tested resume templates that follow the exact ‘resume rules’ employers look for. Easy to use and done within minutes - try now for free!</h4>", unsafe_allow_html=True)
    st.write("\n")
    st.write("\n")
    c1,c2,c3=st.columns(3)

    img3 = Image.open(r"C:\Users\shash\Downloads\Resume\logo\5 Free Horizontal Resume Templates for Job Seeker.jfif")
    st.image(img3, width=750)
    st.write("\n")
    st.markdown("<h2 style='text-align: center; color: black;'>Effortlessly make a job-worthy resume and cover letter that gets you hired faster</h2>", unsafe_allow_html=True)
    st.write("\n")
    m1, m2 = st.columns(2)
    with m2:
        img = Image.open(r"C:\Users\shash\Downloads\Resume\th (3).jfif")
        st.image(img, width=300)
    with m1:
        st.markdown("<h2 style='text-align: left; color: black;'>Create perfect resumes for the modern job market</h2>",unsafe_allow_html=True)
        st.write("Creating a resume has never been this easy! In three simple steps, create the perfect document to impress hiring managers and employers. Minimum time, maximum professional quality.")
    st.write("\n")
    col1,col2=st.columns(2)
    with col2:
        st.markdown("<h2 style='text-align: left; color: black;'>Use the best resume maker as your guide</h2>", unsafe_allow_html=True)
        st.write("Getting that dream job can seem like an impossible task. We’re here to change that. Give yourself a real advantage with the best online resume maker: created by experts, improved by data, trusted by millions of professionals.")
    with col1:
        img4=Image.open(r"C:\Users\shash\Downloads\Resume\logo\th (3).jfif")
        st.image(img4,use_column_width=True)
    st.write("\n")
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("<h2 style='text-align: left; color: black;'>Create a professional story in minutes. Use our cover letter maker.</h2>",
                    unsafe_allow_html=True)
        st.write(
            "Our cover letter maker allows you to write amazing professional pitches in minutes rather than hours. No more writer’s block, no more searching for the convincing phrases or agonizing over formatting. Be persuasive without effort!")
    with col4:
        img4 = Image.open(r"C:\Users\shash\Downloads\Resume\logo\th3.png")
        st.image(img4, use_column_width=True)
    st.write("\n")
    d1,d2=st.columns(2)
    with d1:
        img=Image.open(r"C:\Users\shash\Downloads\Resume\logo\analyzer.jfif")
        st.image(img,use_column_width=True)
    with d2:
        st.markdown(
            "<h2 style='text-align: left; color: black;'>Resume Checker: Review & Score Your Resume Online Now</h2>",
            unsafe_allow_html=True)
        st.write("Get instant grade and feedback on how to improve your resume to be as effective as possible.")
    st.write("\n")
    d3, d4 = st.columns(2)
    with d4:
        img = Image.open(r"C:\Users\shash\Downloads\Resume\logo\job.jfif")
        st.image(img, width=400)
    with d3:
        st.markdown(
            "<h2 style='text-align: left; color: black;'>Job Tracking</h2>",
            unsafe_allow_html=True)

        st.write("An AI-based job recommender analyzes a job seeker's skills, experience, and preferences to suggest suitable job opportunities. It uses machine learning algorithms to match job seekers with relevant job openings, helping to streamline the hiring process for employers and increase job satisfaction for employees.")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.markdown(
        "<h4 style='text-align: center; color: brown;'><i>Let our AI-powered platform help you craft a professional resume that stands out from the crowd. Build your resume today and land your dream job!</i1></h4>",
        unsafe_allow_html=True)
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success('Done!')
    st.snow()
elif resume:
    st.header("Create your Resume with :blue[_ResuMate_]")

    tab1,tab2, tab3, tab4,tab5,tab6,tab7 = st.tabs(["CHOOSE TEMPLATE","PERSONAL DETAILS", "EDUCATION", "EXPERIENCE","SKILLS","PROJECTS","EXTRA CURRICULAR"])
    with tab1:
        pred_tab0()
    with tab2:
        pred_tab1()
    with tab3:
        pred_tab2()
    with tab4:
        pred_tab3()
    with tab5:
        pred_tab4()
    with tab6:
        pred_tab5()
    with tab7:
        pred_tab6()

elif cover_letter:
    st.write("This is cover letter page")

elif analyzer:
    st.write("this is analyzer page")

elif job_board:
    st.write("this is job board page")

