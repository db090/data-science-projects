import streamlit as st
from streamlit_drawable_canvas import st_canvas
import pyautogui
from PIL import Image

st.title("Customizable Screenshot tool")

st.write("Draw a rectangle on the canvas to select the area for the screenshots")

canvas_result= st_canvas(
    fill_color="rgba(255,255,255,0)",
    stroke_width=3,
    stroke_color="red",
    background_color="white",
    height=400,
    width=600,
    drawing_mode="rect",
    key="canvas"
)

if st.button("Take Screenshot"):
    if canvas_result.json_data is not None:
        # Get rectangle coordinates from canvas
        objects=canvas_result.json_data["objects"]
        if len(objects) > 0:
            rect=objects[0]
            left=int(rect["left"])
            top=int(rect["top"])
            width=int(rect["width"])
            height=int(rect["height"])

            # Capture the full screen screenshot
            screenshot=pyautogui.screenshot()

            #crop the screenshot based on use selection
            cropped_screenshot=screenshot.crop((left,top,left+width,top+height))

            #Save the cropped screenshot
            cropped_screenshot.save("cropped_screenshot.png")

            st.success("Cropped screenshot saved as  cropped_screensht.png")

            #Display the cropped screenshot
            img=Image.open("cropped_screenshot.png")
            st.image(img,caption="Cropped Screenshot" , use_column_width=True)

        else:
            st.warning("Please draw a rectangle on the canvas bwfore taking a screenshot.")
    else:
        st.warning("Canvas is empty. Please draw a rectangle")

