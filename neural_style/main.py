import streamlit as st
from PIL import Image

import style

st.title('Pytorch style transfer ')

img = st.sidebar.selectbox(

 		'Select Image', 
 		('amber.jpg', 'cat.png')
 		)

style_name = st.sidebar.selectbox(

 		'Select Style', 
 		('candy', 'rain-princess', 'mosaic', 'udnie')
 		)
model = "saved_models/" + style_name + '.pth'
input_image = 'images/content-images/' + img
output_image = 'images/output-image/' + style_name + '-' + img

st.write('### Source Image:')
image = Image.open(input_image)
st.image(image, width=200)

clicked = st.button('Stilize')

if clicked:
	model = style.load_model(model)
	style.stylize(model, input_image, output_image)


	st.write('### Output Image:')

	image = Image.open(output_image)

	st.image(output_image)
