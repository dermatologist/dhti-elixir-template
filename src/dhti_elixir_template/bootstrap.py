# Define default variables here
# Can be overridden by the user in the server

from kink import di
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_community.llms.fake import FakeListLLM

def bootstrap():
    di["fhir_access_token"] = "YWRtaW46QWRtaW4xMjM="  # admin:Admin123 in base64
    di["fhir_base_url"] = "http://backend:8080/openmrs/ws/fhir2/R4"
    # Check if google api key is set in the environment
    if os.environ.get("GOOGLE_API_KEY"):
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    # Check id openai api key is set in the environment
    elif os.environ.get("OPENAI_API_KEY"):
        llm = ChatOpenAI(model="gpt-4o", temperature=0)
    else:
        llm = FakeListLLM(responses=["I am a fake LLM", "I don't know"])
    di["template_main_llm"] = llm
