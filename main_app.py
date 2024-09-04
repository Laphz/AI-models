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


# Dynamically set the main directory to the root of the project
main_dir = os.path.dirname(os.path.abspath(__file__))

def run_model_app(model_directory):
    # Reset to the main directory
    os.chdir(main_dir)

    # Construct the full path to the model directory
    full_path = os.path.join(main_dir, model_directory)
    
    # Check if the directory exists before changing to it
    if os.path.exists(full_path):
        os.chdir(full_path)
        subprocess.run(["streamlit", "run", "app.py"])
        
        # Change back to the main directory after running the app
    os.chdir(main_dir)
  



   
# Create 5 columns
col1, col2, col3, col4, col5 = st.columns(5)

# Place the button in the middle column (col3)
with col3:
    
    if st.button("Go to model"):

        if selected_model == "Abalone": 
            model_dir = os.path.join(main_dir,"abalone") 
            run_model_app(model_dir)

        elif selected_model == "Amazon Product":
            model_dir = os.path.join(main_dir , "amazone_product")
            run_model_app(model_dir)

        elif selected_model == "Job Placement":
            model_dir = os.path.join(main_dir,"job_placement_data")
            run_model_app(model_dir)

        elif selected_model == "Keyword Extraction":
            model_dir = os.path.join(main_dir,"keyword_extraction")
            run_model_app(model_dir)

        elif selected_model == "Music Recommendation":
            model_dir = os.path.join(main_dir,"music_recommendation")
            run_model_app(model_dir)

        elif selected_model == "Resume Screening":
            model_dir = os.path.join(main_dir,"resume_screening")
            run_model_app(model_dir)



