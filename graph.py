import logging
from typing_extensions import TypedDict

from typing import Annotated

from langgraph.graph import StateGraph , START , END

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StatA(TypedDict):
    cal_add : str 
    cal_sub : str
    cal_mul : str
    cal_div : str


def process_inpute(state: StatA) -> StatA:
    value = state["input"]
    if value == "add":
        x = input (f"enter the first number")
        y = input (f"enter the second number")
        result = x + y
        return {"cal_add": result}
    
    elif value == "sub":
        x = input (f"enter the first number")
        y = input (f"enter the second number")
        result = x - y
        return {"cal_sub": result}
    elif value == "mul":
        x = input (f"enter the first number")
        y = input (f"enter the second number")
        result = x * y




workflow = StateGraph(StatA)

workflow.add_node("process_inpute", process_inpute)
workflow.add_edge(START, "process_inpute")
workflow.add_edge("process_inpute", END)

graph = workflow.compile()

logger.info("Starting workflow execution")
graph.invoke({"input": "add"})  # or "sub", "mul", "div"
logger.info("Workflow execution completed")


