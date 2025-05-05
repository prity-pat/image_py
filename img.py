import cv2
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

img = st.file_uploader('upload an image', type=["jpg", "jpeg","png"])
selected_option = st.selectbox("Select an option",["Pencil Sketch","Gray Scale Image"])
st.title("Image processing App")

if img is not None:
    image_bytes = img.read()
    np_image = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(np_image,cv2.IMREAD_COLOR)

    #CONVERT IMAGE FOR PENCIL SKETCH
    
    img1 = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    img_g = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img_inv = cv2.bitwise_not(img_g)
    img_sm = cv2.GaussianBlur(img_inv,(25,25),sigmaX=0,sigmaY=0)
    img_pencil = cv2.divide(img_g,255-img_sm,scale = 255)

    st.image(img_pencil,caption = 'pencil sketch')

    if selected_option == "Gray Scale Image":
        st.image(img_g,caption = "Gray Scale Image")
    elif selected_option == "Pencil Sketch":
        st.image(img_pencil, caption="Pencil Sketch")  


hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

