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

from web_operations import serp_search 

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
    user_question = state.get("user_question")
    print(f"Performing Google search for: {user_question}")
    
    google_results = serp_search(user_question, engine="google")
    print(f"Google search results: {google_results}")
    print("Google search completed.")
    print("*"*40)
    
    return {"google_results": google_results}

def bing_search(state: State) -> str:
    user_question = state.get("user_question")
    print(f"Performing Bing search for: {user_question}") 
    
    bing_results = serp_search(user_question, engine="bing")
    print(f"Bing search results: {bing_results}")
    print("Bing search completed.")
    print("*"*40)
    return {"bing_results": bing_results}

def reddit_search(state: State) -> str:
    user_question = state.get("user_question")
    print(f"Performing Reddit search for: {user_question}")
    
    reddit_results = []
    return {"reddit_results": reddit_results}

def analyze_reddit_posts(state: State) -> str:
    #
    return {"Selected_reddit_urls": []}

def retrieve_reddit_posts(state: State) -> list:
    # 
    return {"reddit_post_data": []}
    
def analyze_google_results(state: State) -> str:
    # 
    return {"google_analysis": ""}

def analyze_bing_results(state: State) -> str:
    #
    return {"bing_analysis": ""}

def analyze_reddit_results(state: State) -> str:
    # 
    return {"reddit_analysis": ""}

def synthesize_analyses(state: State) -> str:
    # 
    return {"final_answer": ""}



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
graph_builder.add_edge(START, end_key="google_search")
graph_builder.add_edge(START, end_key="bing_search")
graph_builder.add_edge(START, end_key="reddit_search")


graph_builder.add_edge("google_search", end_key="analyze_reddit_posts")
graph_builder.add_edge("bing_search", end_key="analyze_reddit_posts")
graph_builder.add_edge("reddit_search", end_key="analyze_reddit_posts")
graph_builder.add_edge(start_key="analyze_reddit_posts", end_key="retrieve_reddit_posts")

graph_builder.add_edge(start_key="retrieve_reddit_posts", end_key="analyze_google_results")
graph_builder.add_edge(start_key="retrieve_reddit_posts", end_key="analyze_bing_results")
graph_builder.add_edge(start_key="retrieve_reddit_posts", end_key="analyze_reddit_results")

graph_builder.add_edge(start_key="analyze_google_results", end_key="synthesize_analyses") 
graph_builder.add_edge(start_key="analyze_bing_results", end_key="synthesize_analyses") 
graph_builder.add_edge(start_key="analyze_reddit_results", end_key="synthesize_analyses")

graph_builder.add_edge(start_key="synthesize_analyses", end_key=END)

graph = graph_builder.compile() 


def run_chatbot():
    print("Multi-source Research Agent is running...")
    print("Type 'exit to quit.\n' ")  
    while True:
        user_input = input("Ask me anything: ")
        if user_input.lower() == "exit":
            print("Bis Spater Alligator!\n")
            break 
        state = {
            "messages": [{"role": "user", "content": user_input}],
            "user_question": user_input,
            "google_results": None,
            "bing_results": None,
            "reddit_results": None,
            "selected_reddit_urls": None,
            "reddit_post_data": None,
            "google_analysis": None,
            "bing_analysis": None,
            "reddit_analysis": None,
            "final_answer": None

        }
        
        print("\n Starting Parallel research across Google, Bing, and Reddit...\n")
        print("Launching Google, Bing, and Reddit search nodes in parallel...\n")
        final_state = graph.invoke(state)
        
        if final_state.get("final_answer"):
            print(f"\nFinal Answer:\n{final_state.get('final_answer')}\n")
            
        
        print("-"*80)
        
        
if __name__ == "__main__":
    run_chatbot()





print("Das Ende ist nah...")
