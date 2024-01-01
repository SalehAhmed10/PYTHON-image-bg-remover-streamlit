import streamlit as st
import glob
import os
from rembg import remove
import random


import base64

# take image from user and remove background and display it 
st.title("Remove Background")
img = st.file_uploader("Upload an image" , key="bg-remover")
if img is not None:
    st.image(img, width=250, caption="Your Image")
    input_img = img.read()
    output = remove(input_img)
    st.image(output, width=250, caption="Your Image without Background")

    # Generate a random 5-digit number
    random_number = random.randint(10000, 99999)

    # Create a download button for the output image
    st.download_button(
        label="Download Image",
        data=output,
        file_name=f'bg-remove_{random_number}.png',
        mime='image/png'
    )

# # take image from user and remove background and display it 
# st.title("Remove Background")
# img = st.file_uploader("Upload an image" , key="bg-remover")
# if img is not None:
#     st.image(img, width=250, caption="Your Image")
#     input_img = img.read()
#     output = remove(input_img)
#     st.image(output, width=250, caption="Your Image")
    






# add href link
st.markdown(":orange[Project of [Saleh Ahmed](https://github.com/SalehAhmed10)]")


