import streamlit as st

video = 'Detecting Color HSV.mp4'

col_left, col_center, col_right = st.columns([0.3,0.5,0.3])
with col_center:
    st.title('Detección de Color usando HSV')

    st.write(" ")
    st.write(" ")
    st.write(" ")

st.markdown(
        "<h4 style='text-align: center;'"
        ">Ejemplo práctico: reconocer el color amarillo usando el espacio de color HSV y openCV</h4>",
        unsafe_allow_html=True)
st.write(" ")
st.write(" ")
st.write(" ")
col1, col2, col3 = st.columns([0.1,0.6,0.1])
with col2:
    st.video(video, start_time=0)