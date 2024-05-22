from kink import di
from dotenv import load_dotenv

def bootstrap():
    load_dotenv()
    di["main_prompt"] = None
    di["main_llm"] = None