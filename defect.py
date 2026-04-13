import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
from PIL import Image

st.set_page_config('DefectAI',page_icon='🧠',layout='wide')

st.title('AI-POWERED ANALYZER 😭🤑🎮🕹️👾')
st.header(':blue[Prototype of automated structural defect analyzer using AI]👨🏾‍💻')
st.subheader(''':red[AI powered structural defect analysis using Streamlit that allows users to upload the image of the defect and get an analysis of the defect. The app uses Google Generative AI to analyze the image and provide insights about the defect.☕]''')


with st.expander('About the App:'):
    st.markdown('''this app helps to detect the defects like cracks, missalignment etc and provide 
                - **Defect Detection**
                - **Recommendations**
                - **Suggestions for improvement**''')
    
import os

key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=key)

input_image = st.file_uploader('Upload your file here⚐',type=['jpg','jpeg','png'])

img = ''

if input_image:
    
    img = Image.open(input_image).convert('RGB')
    st.image(img, caption='Uploaded Successfully', use_column_width=True) 
    
    prompt = f'''You are an expert structural engineer and defect inspector. Analyze the uploaded image and provide a clear, professional assessment.
    
    1. What type of defect is it?
    2. What are the possible causes of this defect?
    3. how severe is this defect?
    4. Would this defect affect the structural integrity of the building? If yes, how?
    5. What are the potential consequences of this defect?
    6. What are the recommended actions to address this defect?
    7. How to avoid this defect in the future?
    8. what are the repair methods for this defect?
    9. What are the suggestions for improvement?
    10. What are the best practices for maintaining structural integrity and preventing defects in the future?'''
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    def generate_results(prompt, img):
        
        result = model.generate_content(f''' using the given {prompt} and given image {img} analyze the image and give the results in a clear and concise manner''')
        return result.text 
    
    
    submit = st.button('Analyze the image😭')
    
    if submit:
        with st.spinner('Analyzing the image...'):
            response = generate_results(prompt, img)
            st.markdown(f'''## :green[Analysis Results]👨🏾‍🔬''')
            st.write(response)
        
        
        
