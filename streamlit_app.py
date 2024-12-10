# import streamlit as st
# import requests
# from gradio_client import Client, handle_file
# from PIL import Image
# import io
# import base64
# import random

# # Custom CSS for enhanced styling
# def set_custom_theme(theme_choice):
#     """
#     Set custom theme styles based on user selection
#     """
#     themes = {
#         "Ocean Breeze": """
#         <style>
#             .stApp {
#                 background-color: #e6f2ff;
#                 color: #2c3e50;
#             }
#             .stButton>button {
#                 background-color: #3498db;
#                 color: white;
#                 border-radius: 10px;
#                 transition: all 0.3s ease;
#             }
#             .stButton>button:hover {
#                 background-color: #2980b9;
#                 transform: scale(1.05);
#             }
#             .stSidebar {
#                 background-color: #f0f8ff;
#                 border-radius: 10px;
#             }
#         </style>
#         """,
#         "Sunset Glow": """
#         <style>
#             .stApp {
#                 background-color: #fff4e6;
#                 color: #4a4a4a;
#             }
#             .stButton>button {
#                 background-color: #e74c3c;
#                 color: white;
#                 border-radius: 10px;
#                 transition: all 0.3s ease;
#             }
#             .stButton>button:hover {
#                 background-color: #c0392b;
#                 transform: scale(1.05);
#             }
#             .stSidebar {
#                 background-color: #fef0e5;
#                 border-radius: 10px;
#             }
#         </style>
#         """,
#         "Forest Green": """
#         <style>
#             .stApp {
#                 background-color: #e8f5e9;
#                 color: #2c3e50;
#             }
#             .stButton>button {
#                 background-color: #2ecc71;
#                 color: white;
#                 border-radius: 10px;
#                 transition: all 0.3s ease;
#             }
#             .stButton>button:hover {
#                 background-color: #27ae60;
#                 transform: scale(1.05);
#             }
#             .stSidebar {
#                 background-color: #e0f2e0;
#                 border-radius: 10px;
#             }
#         </style>
#         """
#     }
#     st.markdown(themes.get(theme_choice, themes["Ocean Breeze"]), unsafe_allow_html=True)

# def display_image(image_source, is_url=True):
#     """
#     Load an image from a URL or file path.
    
#     Parameters:
#     - image_source (str): URL or file path of the image
#     - is_url (bool): Whether the source is a URL or a local file
    
#     Returns:
#     - PIL Image object
#     """
#     try:
#         if is_url:
#             response = requests.get(image_source)
#             response.raise_for_status()
#             img = Image.open(io.BytesIO(response.content))
#         else:
#             img = Image.open(image_source)
#         return img
#     except Exception as e:
#         st.error(f"Error loading image: {e}")
#         return None

# def test_predict_api(
#     client_id: str,
#     image_source,
#     resolution: int,
#     text_prompt: str,
#     is_url: bool = True,
#     hf_token: str = None
# ):
#     """
#     Test the OminiControl API prediction.
    
#     Parameters:
#     - Similar to the original function in the script
    
#     Returns:
#     - Processed image or None if error occurs
#     """
#     try:
#         # Initialize the client
#         if hf_token:
#             client = Client(client_id, hf_token=hf_token)
#         else:
#             client = Client(client_id)
        
#         # Prepare the image
#         if is_url:
#             image = handle_file(image_source)
#         else:
#             image = handle_file(image_source)
        
#         # Make API call
#         result = client.predict(
#             image=image,
#             resolution=resolution,
#             text=text_prompt,
#             api_name="/predict"
#         )
        
#         # Process the result
#         if isinstance(result, str):
#             # If result is a file path
#             return Image.open(result)
#         elif isinstance(result, dict):
#             # If result is a dictionary with image data
#             if 'output_image_url' in result:
#                 return display_image(result['output_image_url'], is_url=True)
#             elif 'output_image_base64' in result:
#                 image_data = base64.b64decode(result['output_image_base64'])
#                 return Image.open(io.BytesIO(image_data))
        
#         st.warning("Unexpected API response format")
#         return None
    
#     except Exception as e:
#         st.error(f"An error occurred: {e}")
#         return None

# # Predefined prompt templates
# PROMPT_TEMPLATES = [
#     "A beautiful {style} landscape painting",
#     "Romantic {style} scene with vibrant colors",
#     "Dreamy {style} sunset landscape",
#     "Serene {style} nature view",
#     "Artistic {style} interpretation of a peaceful moment"
# ]

# # Predefined styles
# STYLES = [
#     "Impressionist", "Watercolor", "Oil Painting", "Digital Art", 
#     "Abstract", "Minimalist", "Surreal", "Photorealistic"
# ]

# def main():
#     # Page configuration
#     st.set_page_config(
#         page_title="Holidate AI Image Generator", 
#         page_icon=":art:", 
#         layout="wide"
#     )
    
#     # Theme selection
#     theme_choice = st.sidebar.selectbox(
#         "Choose Theme", 
#         ["Ocean Breeze", "Sunset Glow", "Forest Green"]
#     )
    
#     # Apply custom theme
#     set_custom_theme(theme_choice)
    
#     # Main title with animation
#     st.markdown("""
#     <h1 style='text-align: center; color: #2c3e50; 
#     animation: fadeIn 2s ease-in-out;
#     @keyframes fadeIn {
#         from { opacity: 0; }
#         to { opacity: 1; }
#     }'>
#     🎨 Holidate AI Image Generation 🖌️
#     </h1>
#     """, unsafe_allow_html=True)
    
#     # Client ID (could be made configurable)
#     CLIENT_ID = "Yuanshi/OminiControl"
    
#     # Columns for layout
#     col1, col2 = st.columns([2, 1])
    
#     with col1:
#         # Image upload with drag and drop
#         uploaded_file = st.file_uploader(
#             "Choose an image", 
#             type=["png", "jpg", "jpeg"],
#             help="Upload an image to use as a base for transformation"
#         )
    
#     with col2:
#         # Style and resolution selection
#         selected_style = st.selectbox("Select Art Style", STYLES)
#         resolution = st.selectbox("Select Resolution", [512, 1024], index=0)
    
#     # Prompt generation
#     use_template = st.sidebar.checkbox("Use Prompt Template")
#     if use_template:
#         # Generate a random prompt template
#         template = random.choice(PROMPT_TEMPLATES)
#         text_prompt = template.format(style=selected_style)
#         st.sidebar.info(f"Generated Prompt: {text_prompt}")
#     else:
#         # Custom prompt input
#         text_prompt = st.text_input(
#             "Enter your prompt", 
#             f"A beautiful {selected_style} landscape painting"
#         )
    
#     # Additional sidebar options
#     st.sidebar.header("Advanced Options")
#     # Option for additional image processing or features could be added here
    
#     # Process button with animation
#     if st.button("Generate Magic Image"):
#         if uploaded_file is not None:
#             # Display input image
#             st.subheader("Input Image")
#             input_image = Image.open(uploaded_file)
#             st.image(input_image, caption="Uploaded Image", use_column_width=True)
            
#             # Generate image
#             st.subheader("Generated Image")
#             with st.spinner('Conjuring artistic magic...'):
#                 # Temporarily save uploaded file to use with Gradio client
#                 temp_path = "temp_uploaded_image.png"
#                 input_image.save(temp_path)
                
#                 # Call API
#                 output_image = test_predict_api(
#                     client_id=CLIENT_ID,
#                     image_source=temp_path,
#                     resolution=resolution,
#                     text_prompt=text_prompt,
#                     is_url=False
#                 )
                
#                 # Display output image
#                 if output_image:
#                     st.image(output_image, caption="Generated Artistic Image", use_column_width=True)
                    
#                     # Download button for generated image
#                     buffered = io.BytesIO()
#                     output_image.save(buffered, format="PNG")
#                     img_str = base64.b64encode(buffered.getvalue()).decode()
#                     href = f'<a href="data:image/png;base64,{img_str}" download="generated_image.png">Download Generated Image</a>'
#                     st.markdown(href, unsafe_allow_html=True)
#         else:
#             st.warning("Please upload an image first.")
    
#     # Footer with additional information
#     st.markdown("""
#     <div style='text-align: center; margin-top: 50px; color: #7f8c8d;'>
#     <p>✨ Transform your images into artistic masterpieces with AI magic ✨</p>
#     <p>Powered by OminiControl AI | Artistic Styles Galore!</p>
#     </div>
#     """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()


import streamlit as st
import requests
from gradio_client import Client, handle_file
from PIL import Image
import io
import base64
import random

# Custom CSS for enhanced styling
def set_custom_theme(theme_choice):
    """
    Set custom theme styles based on user selection
    """
    themes = {
        "Ocean Breeze": """
        <style>
            .stApp {
                background-color: #bcd3eb;
                color: #0a0f14;
            }
            .stButton>button {
                background-color: #3498db;
                color: black;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            .stButton>button:hover {
                background-color: #2980b9;
                transform: scale(1.05);
            }
            .stSidebar {
                background-color: #f0f8ff;
                border-radius: 10px;
            }
            .stMarkdown, .stText, .stHeader {
                color: #000000 !important;
            }
        </style>
        """,
        "Sunset Glow": """
        <style>
            .stApp {
                background-color: #cfc5b8;
                color: #000000;
            }
            .stButton>button {
                background-color: #e74c3c;
                color: white;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            .stButton>button:hover {
                background-color: #c0392b;
                transform: scale(1.05);
            }
            .stSidebar {
                background-color: #fef0e5;
                border-radius: 10px;
            }
            .stMarkdown, .stText, .stHeader {
                color: #000000 !important;
            }
        </style>
        """,
        "Forest Green": """
        <style>
            .stApp {
                background-color: #a1cca4;
                color: #000000;
            }
            .stButton>button {
                background-color: #2ecc71;
                color: white;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            .stButton>button:hover {
                background-color: #27ae60;
                transform: scale(1.05);
            }
            st.radio{
            background-color: #2ecc71;
            color: black !important;
            text-align: center;
            }
            .stSidebar {
                background-color: #e0f2e0;
                border-radius: 10px;
            }
            .stMarkdown, .stText, .stHeader {
                color: #000000 !important;
            }
        </style>
        """
    }
    st.markdown(themes.get(theme_choice, themes["Ocean Breeze"]), unsafe_allow_html=True)

def display_image(image_source, is_url=True):
    """
    Load an image from a URL or file path.
    
    Parameters:
    - image_source (str): URL or file path of the image
    - is_url (bool): Whether the source is a URL or a local file
    
    Returns:
    - PIL Image object
    """
    try:
        if is_url:
            response = requests.get(image_source)
            response.raise_for_status()
            img = Image.open(io.BytesIO(response.content))
        else:
            img = Image.open(image_source)
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

def test_predict_api(
    client_id: str,
    image_source,
    resolution: int,
    text_prompt: str,
    is_url: bool = True,
    hf_token: str = None
):
    """
    Test the OminiControl API prediction.
    
    Parameters:
    - Similar to the original function in the script
    
    Returns:
    - Processed image or None if error occurs
    """
    try:
        # Initialize the client
        if hf_token:
            client = Client(client_id, hf_token=hf_token)
        else:
            client = Client(client_id)
        
        # Prepare the image
        if is_url:
            image = handle_file(image_source)
        else:
            image = handle_file(image_source)
        
        # Make API call
        result = client.predict(
            image=image,
            resolution=resolution,
            text=text_prompt,
            api_name="/predict"
        )
        
        # Process the result
        if isinstance(result, str):
            # If result is a file path
            return Image.open(result)
        elif isinstance(result, dict):
            # If result is a dictionary with image data
            if 'output_image_url' in result:
                return display_image(result['output_image_url'], is_url=True)
            elif 'output_image_base64' in result:
                image_data = base64.b64decode(result['output_image_base64'])
                return Image.open(io.BytesIO(image_data))
        
        st.warning("Unexpected API response format")
        return None
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Predefined prompt templates
PROMPT_TEMPLATES = [
    "A beautiful {style} landscape painting",
    "Romantic {style} scene with vibrant colors",
    "Dreamy {style} sunset landscape",
    "Serene {style} nature view",
    "Artistic {style} interpretation of a peaceful moment"
]

# Predefined styles
STYLES = [
    "Impressionist", "Watercolor", "Oil Painting", "Digital Art", 
    "Abstract", "Minimalist", "Surreal", "Photorealistic"
]

def main():
    # Page configuration
    st.set_page_config(
        page_title="Holidate AI Image Generator", 
        page_icon=":art:", 
        layout="wide"
    )
    
    # Theme selection
    theme_choice = st.sidebar.selectbox(
        "Choose Theme", 
        ["Ocean Breeze", "Sunset Glow", "Forest Green"]
    )
    
    # Apply custom theme
    set_custom_theme(theme_choice)
    
    # Main title with animation
    st.markdown("""
    <h1 style='text-align: center; color: #000000; 
    animation: fadeIn 2s ease-in-out;
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }'>
    🎨 Holidate AI Image Generation 🖌️
    </h1>
    """, unsafe_allow_html=True)
    
    # Client ID (could be made configurable)
    CLIENT_ID = "Yuanshi/OminiControl"
    
    # Image input method selection
    input_method = st.radio("Choose Image Input Method", 
                             ["Upload Image", "Use Image URL"])
    
    # Columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if input_method == "Upload Image":
            # Image upload with drag and drop
            uploaded_file = st.file_uploader(
                "Choose an image", 
                type=["png", "jpg", "jpeg"],
                help="Upload an image to use as a base for transformation"
            )
            image_source = uploaded_file
            is_url = False
        else:
            # Image URL input
            image_url = st.text_input(
                "Enter Image URL", 
                help="Paste a direct link to an image"
            )
            image_source = image_url
            is_url = True
    
    with col2:
        # Style and resolution selection
        selected_style = st.selectbox("Select Art Style", STYLES)
        resolution = st.selectbox("Select Resolution", [512, 1024], index=0)
    
    # Prompt generation
    use_template = st.sidebar.checkbox("Use Prompt Template")
    if use_template:
        # Generate a random prompt template
        template = random.choice(PROMPT_TEMPLATES)
        text_prompt = template.format(style=selected_style)
        st.sidebar.info(f"Generated Prompt: {text_prompt}")
    else:
        # Custom prompt input
        text_prompt = st.text_input(
            "Enter your prompt", 
            f"A beautiful {selected_style} landscape painting"
        )
    
    # Additional sidebar options
    st.sidebar.header("Advanced Options")
    # Option for additional image processing or features could be added here
    
    # Process button with animation
    if st.button("Generate Magic Image"):
        try:
            # Handling image source based on input method
            if input_method == "Upload Image":
                if uploaded_file is not None:
                    # Display input image
                    st.subheader("Input Image")
                    input_image = Image.open(uploaded_file)
                    st.image(input_image, caption="Uploaded Image", use_column_width=True)
                    
                    # Temporarily save uploaded file to use with Gradio client
                    temp_path = "temp_uploaded_image.png"
                    input_image.save(temp_path)
                    image_source = temp_path
                    is_url = False
                else:
                    st.warning("Please upload an image first.")
                    return
            else:
                if image_url:
                    # Display input image from URL
                    st.subheader("Input Image")
                    input_image = display_image(image_url)
                    if input_image:
                        st.image(input_image, caption="Image from URL", use_column_width=True)
                    else:
                        st.warning("Could not load image from URL.")
                        return
                else:
                    st.warning("Please enter an image URL.")
                    return
            
            # Generate image
            st.subheader("Generated Image")
            with st.spinner('Conjuring artistic magic...'):
                # Call API
                output_image = test_predict_api(
                    client_id=CLIENT_ID,
                    image_source=image_source,
                    resolution=resolution,
                    text_prompt=text_prompt,
                    is_url=is_url
                )
                
                # Display output image
                if output_image:
                    st.image(output_image, caption="Generated Artistic Image", use_column_width=True)
                    
                    # Download button for generated image
                    buffered = io.BytesIO()
                    output_image.save(buffered, format="PNG")
                    img_str = base64.b64encode(buffered.getvalue()).decode()
                    href = f'<a href="data:image/png;base64,{img_str}" download="generated_image.png">Download Generated Image</a>'
                    st.markdown(href, unsafe_allow_html=True)
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    # Footer with additional information
    st.markdown("""
    <div style='text-align: center; margin-top: 50px; color: #000000;'>
    <p>✨ Transform your images into artistic masterpieces with AI magic ✨</p>
    <p>Powered by Holidate AI | Artistic Styles Galore!</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
