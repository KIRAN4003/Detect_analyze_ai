import streamlit as st 
# To import the functions to design the interface
import dotenv
from dotenv import load_dotenv # To load the environment variables from the .env file
import os # To access the environment variables
import google.generativeai as genai # To use the Google Generative AI API
load_dotenv()

from PIL import Image # pillow is used to load,save,convert the format and manipulate the image

st.set_page_config(page_title="Structural Defect Analysis using AI", page_icon=":streamlit:", layout="wide") # To set the page configuration

st.title("AI assisnt for structural defect analysis")
st.header(':blue[Prototype for automated structural defect analysis ]')
st.subheader('''Develop a web based app using Streamlit that allows users to upload image of a building structures and to analyze the defects using Gemini model.''')

with st.expander("About the applicationn"):
    st.markdown(f'''This is used to defect the structural defect in given images like cracks
                ,misallignments using ai system
                -***Defect Detection***
                -***Recommendations***
                -***Report Generation***''')
    
st.subheader('upload the image here✅')

input_image=st.file_uploader('clike here👉',type=['png','jpg','jpeg'])

img=''
if input_image:
    img=Image.open(input_image).convert('RGB')
    st.image(img, caption='Uploaded Image sucessfully✅')

prompt= f'''Act as a structural and civil engineer and provide the necessary dettails in
the proper bullet points in more precise way(maximum 3 points) for the following question:
1.Is there any structural defect such as cracks,bends, damages in the given image?
2.what is the probability of the detected defect?
3.what is the severity level of the defect like minor,moderate or major ?
4.what are the possible causes of the defect,considering the material damage,environment damage?
5.what are the possible recommendations to fix the defect?
6.suggest the remedies to repair the defect?
7. say whether the defect will cause any damage to the surronding and give probability for that?
8. say whether we need to monitor the defected area after repair or replacement?
9. Give the cost range to repair the defect or replace in Indian rupees.
10. Generate summary on the insights.''' 
key =os.getenv('GOOGLE_API_KEY') # To set the Google API key from the environment variable

genai.configure(api_key=key) # To configure the Google Generative AI API with the API key

def generate_results(prompt,img):
    model=genai.GenerativeModel('gemini-2.5-flash') # 'gemeni-1.5-pro','gemini-1.5-flash',
    results=model.generate_content(f'''Using the given prompt{prompt},
                                   analyze the given image{img} and generate the results based on the prompt''')
    return results.text
    
submit=st.button('Analyze the defect🚨')

if submit:
    with st.spinner('Analyzing ...🤔'):
        response=generate_results(prompt,img)
        
        st.markdown('## green:[Results💯]')
        st.write(response)