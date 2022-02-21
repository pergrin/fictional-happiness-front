import streamlit as st
import requests


def send_request(text, length):
    api_url = 'https://finished-fictional-happiness-pergrin.endpoint.ainize.ai/predict'
    data = {
        'base_text': (None, text),
        'length': (None, length),
    }
    response = requests.post(api_url, data=data)
    status_code = response.status_code

    return status_code, response


st.title("Joint Entity and Relation extraction")
st.header("Get Entities and Relations amongst ")

length_slider = st.sidebar.slider("Length", 0, 300)

base_story = st.text_input("Type Base Story", "\"In our current research into the design of cognitively well-motivated interfaces relying primarily on the display of graphical information, we have observed that graphical information alone does not provide sufficient support to users-particularly when situations arise that do not simply conform to the users' expectations. This can occur due to too much information being requested, too little, information of the wrong kind, etc.. To solve this problem, we are working towards the integration of natural language generation to augment the interaction\"")
if st.button("Submit"):
    if length_slider == 0:
        st.warning("Please define the length")
    else:
        status_code, response = send_request(base_story, length_slider)
        if status_code == 200:
            prediction = response.json()
            st.success(prediction["prediction"])
        else:
            st.error(str(status_code) + " Error")


