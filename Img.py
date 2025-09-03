import streamlit as st
from PIL import Image, ImageFilter

# Title
st.title("🖼️ Simple Image Filter App")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open image
    image = Image.open(uploaded_file)

    # Show original image
    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    # Select filter
    option = st.selectbox(
        "Choose a filter",
        ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EMBOSS", "SHARPEN", "SMOOTH"]
    )

    # Apply filter
    if option == "BLUR":
        filtered_img = image.filter(ImageFilter.BLUR)
    elif option == "CONTOUR":
        filtered_img = image.filter(ImageFilter.CONTOUR)
    elif option == "DETAIL":
        filtered_img = image.filter(ImageFilter.DETAIL)
    elif option == "EDGE_ENHANCE":
        filtered_img = image.filter(ImageFilter.EDGE_ENHANCE)
    elif option == "EMBOSS":
        filtered_img = image.filter(ImageFilter.EMBOSS)
    elif option == "SHARPEN":
        filtered_img = image.filter(ImageFilter.SHARPEN)
    elif option == "SMOOTH":
        filtered_img = image.filter(ImageFilter.SMOOTH)

    # Show filtered image
    st.subheader(f"Filtered Image - {option}")
    st.image(filtered_img, use_container_width=True)

    # Download option
    st.download_button(
        label="Download filtered image",
        data=filtered_img.tobytes(),
        file_name="filtered_image.png",
        mime="image/png"
    )
