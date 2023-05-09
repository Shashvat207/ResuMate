import streamlit as st
from PIL import Image
img2 =Image.open(r"C:\Users\shash\OneDrive\Documents\Black and White Minimalist Modern Clean Technology Logo .png")
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #845AFF;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #4200FF;
    color:#ffffff;
    }
</style>""", unsafe_allow_html=True)
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
elif resume:
    st.write("this is resume builder page")
elif cover_letter:
    st.write("This is cover letter page")
elif analyzer:
    st.write("this is analyzer page")
elif job_board:
    st.write("this is job board page")
