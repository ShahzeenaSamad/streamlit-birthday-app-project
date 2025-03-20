import streamlit as st
from PIL import Image
import random
from streamlit_lottie import st_lottie
import requests
from datetime import datetime
import base64
from io import BytesIO

# Load Lottie animations
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Random birthday quotes
def get_random_quote():
    quotes = [
        "May your birthday be filled with sunshine and smiles!",
        "Wishing you a day full of love, joy, and cake!",
        "Happy Birthday! May all your dreams come true!",
        "Cheers to another year of awesomeness!",
        "You're not getting older, you're getting better!",
        "Today is your day to shine! Happy Birthday!",
        "Another year older, wiser, and more fabulous!",
    ]
    return random.choice(quotes)

# Function to convert image to base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Set background image
def set_bg_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://th.bing.com/th/id/OIP.AbR8Zew7NNZqGRQGEyHYSgHaHa?rs=1&pid=ImgDetMain");
            background-size: cover;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Main function
def main():
    # Page configuration
    st.set_page_config(
        page_title="🎉 Ultimate Birthday Wishes App 🎂",
        page_icon="🎈",
        layout="centered",
    )

    # Set background image
    set_bg_image()

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        /* All text styling */
        h1, h2, h3, h4, h5, h6, .stTextInput label, .stTextArea label,
        .stFileUploader label, .stSlider label, .stColorPicker label,
        .stDateInput label, .stWrite, .stButton>button, .stSuccess,
        .stSelectbox label, .stSlider div, .stMarkdown {
            color: #F5F20B !important;  /* Bright yellow color */
            font-family: 'Pacifico', cursive !important;
        }

        /* Headings font size */
        h1 {
            font-size: 3rem !important;  /* Main title */
        }
        h2 {
            font-size: 2rem !important;  /* Subheaders */
        }
        h3, h4, h5, h6 {
            font-size: 1.5rem !important;  /* Other headings */
        }

        /* Input boxes styling */
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            background-color: rgba(255, 255, 255, 0.8) !important;  /* Semi-transparent white */
            color: #333333 !important;  /* Dark text color */
            border-radius: 10px !important;
            padding: 10px !important;
            border: 1px solid #70D8E8 !important;  /* Light blue border */
        }

        /* Buttons styling */
        .stButton>button {
            background-color: #70D8E8 !important;  /* Light blue background */
            color: white !important;  /* White text color */
            border-radius: 10px !important;
            padding: 10px 20px !important;
            font-size: 16px !important;
            border: none !important;
        }

        /* Success message styling */
        .stSuccess {
            background-color: #4caf50 !important;  /* Green background */
            color: white !important;  /* White text color */
            border-radius: 10px !important;
            padding: 10px !important;
        }

        /* Slider styling */
        .stSlider>div>div>div>div {
            background-color: #70D8E8 !important;  /* Light blue slider */
        }

        /* Color picker styling */
        .stColorPicker>div>div>div>div {
            border: 2px solid #70D8E8 !important;  /* Light blue border */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title and header
    st.title("🎉 Wishful Celebrations 🎂")
    st.markdown("---")

    # Theme selection
    theme = st.selectbox("🎨 Choose a theme:", ["Light", "Dark"])

    # User Input
    name = st.text_input("🎈 Enter the Birthday Person's Name:")
    message = st.text_area("💌 Write a special birthday message:")
    uploaded_image = st.file_uploader("📸 Upload an image (optional)", type=["jpg", "png", "jpeg"])

    # Add a slider for selecting the font size of the message
    font_size = st.slider("🔠 Select font size for your message:", 10, 50, 20)

    # Add a color picker for the message
    message_color = st.color_picker("🎨 Pick a color for your message:", "#70D8E8")

    # Countdown to birthday
    st.subheader("⏳ Countdown to Birthday")
    birthday_date = st.date_input("📅 Enter the birthday date:")
    today = datetime.now().date()
    if birthday_date:
        delta = (birthday_date - today).days
        if delta > 0:
            st.write(f"🎉 Only {delta} days left until the birthday!")
        elif delta == 0:
            st.write("🎂 Today is the birthday! 🎉")
        else:
            st.write("🎈 The birthday has already passed!")

    # Music player with a proper birthday song
    st.subheader("🎵 Birthday Music")
    # Path to the downloaded music file
    music_file_path = "music/happy_birthday.mp3"  # Relative path example

    # Check if music file exists and play it
    try:
        st.audio(music_file_path, format="audio/mp3", start_time=0)
    except FileNotFoundError:
        st.warning("Music file not found. Please ensure the file path is correct.")

    # Random Birthday Wishes Generator
    st.subheader("🎲 Random Birthday Wishes")
    if st.button("Generate Random Wish"):
        st.write(f"🎉 {get_random_quote()}")

    # Generate Birthday Card
    if st.button("🎁 Generate Birthday Card"):
        st.balloons()  # Celebration effect 🎈

        # Display birthday card
        st.subheader(f"🎈 Happy Birthday, {name}! 🎈")

        # Display uploaded image with custom height using CSS
        if uploaded_image:
            image = Image.open(uploaded_image)
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{image_to_base64(image)}" alt="Birthday Image" style="width: 300px; height: auto;">
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.caption(f"A special wish for {name}!")

        # Display the custom message or a random quote
        st.markdown(
            f"""
            <div style="font-size: {font_size}px; color: {message_color}; text-align: center;">
                ✨ **Your Special Birthday Message:**<br>
                {message if message else get_random_quote()}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Add a Lottie animation for extra fun
        lottie_animation = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_7yimwmpj.json")
        if lottie_animation:
            st_lottie(lottie_animation, height=300, key="birthday")

        # Add a confetti effect
        st.markdown(
            """
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.4.0/dist/confetti.browser.min.js"></script>
            <script>
            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });
            </script>
            """,
            unsafe_allow_html=True,
        )

# Run the app
if __name__ == "__main__":
    main()