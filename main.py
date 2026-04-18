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
# In LangGraph essentially, we will create a graph where each node represents a step in the process, and edges represent the flow of information between these steps. The graph will start with the user question and end with the final answer.
# Nodes in the graph are operations-functions.
    
    
    
graph_builder = StateGraph(State)
# You need to give a name to every node and point it to the function that performs the operation for that node. The graph will then use these functions to execute the steps in the process.
graph_builder.add_node("google_search", google_search) # Pointing to the function that performs Google search
graph_builder.add_node("bing_search", bing_search) # Pointing to the function that performs Bing search
graph_builder.add_node("reddit_search", reddit_search) # Pointing to the function that performs Reddit search
graph_builder.add_node("retrieve_reddit_posts", retrieve_reddit_posts) # Pointing to the function that retrieves Reddit post data
graph_builder.add_node("analyze_reddit_posts", analyze_reddit_posts) # Pointing to the function that performs Reddit post analysis
graph_builder.add_node("analyze_google_results", analyze_google_results) # Pointing to the function that performs Google results analysis
graph_builder.add_node("analyze_bing_results", analyze_bing_results) # Pointing to the function that performs Bing results analysis
graph_builder.add_node("analyze_reddit_results", analyze_reddit_results) # Pointing to the function that performs Reddit results analysis
graph_builder.add_node("synthesize_analyses", synthesize_analyses) # Pointing to the function that synthesizes the analyses


# The nodes exist now. But they are not connected. We need to connect them in the order they should be executed. For example, the Google search node should be connected to the Google results analysis node, and so on.
graph_builder.add_edge(START, end_key="google_search", edge_key="start_to_google_search")
graph_builder.add_edge(START, end_key="bing_search", edge_key="start_to_bing_search")
graph_builder.add_edge(START, end_key="reddit_search", edge_key="start_to_reddit_search")










print("Das Ende ist nah...")
