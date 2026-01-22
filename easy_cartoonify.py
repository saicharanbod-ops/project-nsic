import cv2
import os
import streamlit as st
from pathlib import Path
import numpy as np

st.set_page_config(page_title="Easy Cartoonify", layout="wide")
st.title("🎨 Easy Cartoonify")
st.write("Transform your images into cartoon style artwork!")

## This function looks for and finds the desired file. You can specify a parent directory for the fundtion to look for, however if you have no idea where a file is; this functio will find it for you, just slower. If you have no idea where a file is, just type "/".
def find_the_image(file_name, directory_name):
    files_found = []
    for path, subdirs, files in os.walk(directory_name):
        for name in files:
            if(file_name == name):
                file_path = os.path.join(path,name)
                files_found.append(file_path)
    
    if files_found:
        return files_found[0] ## Return the path.
    else:
        return None

# Streamlit UI
col1, col2 = st.columns(2)

with col1:
    st.subheader("Upload or Locate Image")
    upload_option = st.radio("Choose input method:", ["Upload File", "Search by Filename"])

color_image = None

if upload_option == "Upload File":
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        color_image = cv2.imdecode(file_bytes, 1)
else:
    image_name = st.text_input("Enter the image filename:")
    image_directory = st.text_input("Enter the directory to search in:", value="./")
    
    if image_name and image_directory:
        image_path = find_the_image(image_name, image_directory)
        if image_path:
            color_image = cv2.imread(image_path)
            st.success(f"Found image at: {image_path}")
        else:
            st.error(f"Image '{image_name}' not found in {image_directory}")

with col2:
    st.subheader("Cartoon Style Selection")
    cartoon_style_selection = st.radio("Choose a cartoon style:", ["Style 1 (Subtle)", "Style 2 (Bold)"])

# Process and display image
if color_image is not None:
    st.subheader("Results")
    
    col_original, col_cartoon = st.columns(2)
    
    with col_original:
        st.write("**Original Image**")
        st.image(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB), use_column_width=True)
    
    with col_cartoon:
        st.write("**Cartoonified Image**")
        
        if cartoon_style_selection == "Style 1 (Subtle)":
            cartoon_image = cv2.stylization(color_image, sigma_s=150, sigma_r=0.25)
        else:
            cartoon_image = cv2.stylization(color_image, sigma_s=60, sigma_r=0.5)
        
        st.image(cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2RGB), use_column_width=True)
        
        # Download button
        if st.button("💾 Download Cartoonified Image"):
            output_path = "cartoonified_image.png"
            cv2.imwrite(output_path, cartoon_image)
            with open(output_path, "rb") as file:
                st.download_button(
                    label="Click here to download",
                    data=file.read(),
                    file_name=output_path,
                    mime="image/png"
                )
