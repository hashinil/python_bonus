import streamlit as st
from PIL import Image

#Start the camera
with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    #Create a pillow instance
    img = Image.open(camera_image)

    #convert camera image to gray scale
    gray_img = img.convert("L")

    #render the gray scale image on the web page
    st.image(gray_img)