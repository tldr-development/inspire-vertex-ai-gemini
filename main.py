import vertexai
from vertexai.preview.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models

from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def hc():
    return "ok"

# get prediction from post data
@app.post("/generate")
def predict(data: dict):
    # check security
    token = data.get("token")
    # get environment variable
    if token != os.environ.get("TOKEN"):
        return {"data": "token error"}
    promt = data.get("promt")
    # promt is json to string
    if type(promt) == dict:
        promt = str(promt)

    data = generate(promt)
    return data

def generate(promt):
  vertexai.init(project="etcd-389303", location="asia-northeast3")
  model = GenerativeModel("gemini-1.0-pro-001")
  responses = model.generate_content(
    promt,
    generation_config={
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1
    },
    safety_settings={
          generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
    # stream=True,
  )
  return responses.candidates[0].content.parts[0].text

