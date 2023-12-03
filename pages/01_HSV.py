import streamlit as st
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt


# Load image
img_rgb = cv2.imread('face_rgb.jpg')
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)

# Convert to HSV
img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)

col_left, col_center, col_right = st.columns([0.3,0.5,0.3])
with col_center:
    st.title('Modelo de Color HSV')
    st.write(" ")
    st.write(" ")
    st.write(" ")


# original image
col_left, col_center, col_right = st.columns([0.3,0.7,0.3])
with col_center:
    st.image(img_rgb, caption='Original', width=500)
    st.write(" ")
    st.write(" ")
    st.write(" ")

# split the channels
h, s, v = cv2.split(img_hsv)

# Normalize the channels
h_normalized = h / 179
s_normalized = s / 255
v_normalized = v / 255

# Covert the hue channel to degrees
h_degrees = np.degrees(h_normalized)

# Convert the saturation and value channels to percentages
s_percentage = s_normalized * 100
v_percentage = v_normalized * 100

print("Dimensiones de df_h:", h_degrees.shape)
print("Dimensiones de df_s:", s_percentage.shape)
print("Dimensiones de df_v:", v_percentage.shape)


# Create figures for each channel
fig_h, ax_h = plt.subplots()
cax_h = ax_h.imshow(h_degrees, cmap='hsv')
plt.axis('off')

fig_s, ax_s = plt.subplots()
cax_s = ax_s.imshow(s_percentage, cmap='gray')
plt.axis('off')

fig_v, ax_v = plt.subplots()
cax_v = ax_v.imshow(v_percentage, cmap='gray')
plt.axis('off')

# Display the figures
col1, col2, col3, col4, col5, col6 = st.columns([0.2, 1, 0.2, 1, 0.2, 0.2])
with col2:
    st.image(img_hsv, caption='HSV')
    st.pyplot(fig_s, clear_figure=True, use_container_width=True)
    st.markdown("<h5 style='text-align: center;'>Saturación</h5>", unsafe_allow_html=True)


with col4:
    st.pyplot(fig_h, clear_figure=True, use_container_width=True)
    st.markdown("<h5 style='text-align: center;'>Hue</h5>", unsafe_allow_html=True)
    st.pyplot(fig_v, clear_figure=True, use_container_width=True)
    st.markdown("<h5 style='text-align: center;'>Value</h5>", unsafe_allow_html=True)



