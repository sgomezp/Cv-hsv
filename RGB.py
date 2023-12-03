import numpy as np
import pandas as pd
import streamlit as st
import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# Page Configuration
st.set_page_config(
    page_title="Color Model examples",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'About': 'Sandra Gómez S.'
    }
)

def reconstruct(r,g,b):
    # Stack the red, green and blue channels to get the original image
    out = np.dstack((r,g,b))
    return out

# Load image
img_rgb = cv2.imread('face_rgb.jpg')
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)

# Separate the channels RGB
r, g, b = cv2.split(img_rgb)


col_left, col_center, col_right = st.columns([0.4,0.5,0.3])
with col_center:
    st.title('Modelos de Color')
    st.write(" ")
    st.write(" ")
    st.write(" ")


# original image
col_left, col_center, col_right = st.columns([0.5,0.7,0.5])
with col_center:
    st.image(img_rgb, caption='Original', width=500)
    st.write(" ")
    st.write(" ")
    st.write(" ")
    

# channel values for pixel [0,0]
col1, col2, col3, col4, col5, col6 = st.columns([0.1,0.5, 0.5,0.5, 0.1,0.1])
with col2:
    st.write(f'<span style="font-size:25px; color:red"> Pixel [0,0] Red value: {img_rgb[0, 0, 0]}</span>', unsafe_allow_html=True)
    st.dataframe(r, hide_index=False)
with col3:
    st.write(f'<span style="font-size:25px; color:green"> Pixel [0,0] Green value: {img_rgb[0, 0, 1]}</span>', unsafe_allow_html=True)
    st.dataframe(g, hide_index=False)
with col4:
    st.write(f'<span style="font-size:25px; color:blue"> Pixel [0,0]bBlue value: {img_rgb[0, 0, 2]}</span>', unsafe_allow_html=True)
    st.dataframe(b, hide_index=False)

st.write(" ")
st.write(" ")
st.write(" ")
"---"
col_left, col_center, col_right = st.columns([0.4,0.5,0.2])
with col_center:
    st.write(" ")
    st.write(" ")
    st.title('Modelo de color RGB')
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")


# separate the channels
r= img_rgb[:, :, 0] #red channel values
g= img_rgb[:, :, 1] #green channel values
b= img_rgb[:, :, 2] #blue channel values

col1, col2, col3, col4, col5, col6 = st.columns([0.01,0.55, 0.15,0.55, 0.01,0.01])
with col2:
    st.image(img_rgb, caption='Original', width= 500)
    st.image(g, caption='Green', width= 500)
with col4:
    st.image(r, caption='Red', width= 500)
    st.image(b, caption='Blue', width= 500)

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

"---"
col_left, col_center, col_right = st.columns([0.2,0.5,0.2])
with col_center:
    st.title('Reconstrucción de la imagen')
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

# reconstruct the image
col_left, col_center, col_right = st.columns([0.3,0.7,0.3])
with col_center:
    st.image(reconstruct(r,g,b), caption='Imagen Reconstruida', width=500)
    st.write(" ")
    st.write(" ")
    st.write(" ")





