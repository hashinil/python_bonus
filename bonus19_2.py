import streamlit as st
from PIL import Image

#Upload Image
upload_image = st.file_uploader("Upload Image")

if upload_image:
    # Create a pillow instance
    img_u = Image.open(upload_image)

    #convert camera image to gray scale
    gray_u_img = img_u.convert("L")

    #render the gray scale image on the web page
    st.image(gray_u_img)

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