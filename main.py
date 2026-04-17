# python -m uv init .
# python -m uv add langchain langgraph langchain-openai python-dotenv
#scaffolding:
from dotenv import load_dotenv
from typing import Annotated, List 
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from pydantic import BaseModel, Field

print("Loading environment variables...")
load_dotenv()

print("Initializing chat model...")
chat_model = init_chat_model("gpt-4o")

print("Chat model initialized.")


class State(TypedDict):
    messages: Annotated[list, add_messages]
    user_question: str | None
    google_results: str | None
    bing_results: str | None
    reddit_results: str | None
    selected_reddit_urls: list[str] | None
    reddit_post_data : list | None
    google_analysis: str | None
    bing_analysis: str | None
    reddit_analysis: str | None
    final_answer: str | None
    
print("Defining nodes for the graph...")


def google_search(state: State) -> str:
    # Placeholder for Google search implementation
    return 

def bing_search(state: State) -> str:
    # Placeholder for Bing search implementation
    return

def reddit_search(state: State) -> str:
    # Placeholder for Reddit search implementation
    return

def analyze_reddit_posts(state: State) -> str:
    # Placeholder for Reddit post analysis implementation
    return

def retrieve_reddit_posts(state: State) -> list:
    # Placeholder for retrieving Reddit post data implementation
    return
    
def analyze_google_results(state: State) -> str:
    # Placeholder for Google results analysis implementation
    return

def analyze_bing_results(state: State) -> str:
    # Placeholder for Bing results analysis implementation
    return

def analyze_reddit_results(state: State) -> str:
    # Placeholder for Reddit results analysis implementation
    return

def symthesize_analyses(state: State) -> str:
    # Placeholder for synthesizing analyses implementation
    return



print("Create graph to connect the above nodes...")
    
    
    
    
    
    
    

print("Das Ende ist nah...")
