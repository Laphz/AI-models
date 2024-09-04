import streamlit as st
import subprocess
import os
from PIL import Image

# Define your model directories and names
models = {
    "Keyword Extraction": "keyword_extraction",
    "Amazon Product": "amazone_product",
    "Job Placement": "job_placement_data",
    "Music Recommendation": "music_recommendation",
    "Resume Screening": "resume_screening",
    "Abalone" :"abalone"
}

# Sidebar navigation
st.title("AI Models")
img = Image.open('main.jpeg')
img = img.resize((700,400))
st.image(img)
selected_model = st.selectbox("Select the Model", list(models.keys()))

# Path to the root directory
main_dir = "/home/chinu/Data/Projects/Python/AI-models/"

# Run the selected model app
def run_model_app(model_directory):
    os.chdir(model_directory)
    subprocess.run(["streamlit", "run", "app.py"])

# Create 5 columns
col1, col2, col3, col4, col5 = st.columns(5)

# Place the button in the middle column (col3)
with col3:
    
    if st.button("Go to model"):

        if selected_model == "Abalone":
            os.chdir(main_dir)
            print(os.getcwd())
            model_dir = os.path.join(main_dir,"abalone")
            run_model_app(model_dir)

        elif selected_model == "Amazon Product":
            os.chdir(main_dir)
            model_dir = os.path.join(main_dir,"amazone_product")
            run_model_app(model_dir)

        elif selected_model == "Job Placement":
            os.chdir(main_dir)
            model_dir = os.path.join(main_dir,"job_placement_data")
            run_model_app(model_dir)

        elif selected_model == "Keyword Extraction":
            os.chdir(main_dir)
            model_dir = os.path.join(main_dir,"keyword_extraction")
            run_model_app(model_dir)

        elif selected_model == "Music Recommendation":
            os.chdir(main_dir)
            model_dir = os.path.join(main_dir,"music_recommendation")
            run_model_app(model_dir)

        elif selected_model == "Resume Screening":
            os.chdir(main_dir)
            model_dir = os.path.join(main_dir,"resume_screening")
            run_model_app(model_dir)


