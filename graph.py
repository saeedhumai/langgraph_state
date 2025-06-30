import logging
from typing_extensions import TypedDict

from typing import Annotated

from langgraph.graph import StateGraph , START , END

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class calculator(TypedDict):
    cal_add : int
    cal_sub : int
    cal_mul : int
    cal_div : int
    input : str


def process_inpute(state: calculator) -> calculator:
    value = state["input"]
    if value == "add":
        x = input (f"enter the first number : ")
        y = input (f"enter the second number : ")
        result = print(f"the result of {x} + {y} is { int(x) + int(y) }")
        return {"cal_add": result}
    
    elif value == "sub":
        x = input (f"enter the first number : ")
        y = input (f"enter the second number : ")
        result = print(f"the result of {x} - {y} is { int(x) - int(y) }")
        return {"cal_sub": result}
    elif value == "mul":
        x = input (f"enter the first number : ")
        y = input (f"enter the second number : ")
        result = print(f"the result of {x} * {y} is { int(x) * int(y) }")



workflow = StateGraph(calculator)
workflow.add_node("process_inpute", process_inpute)
workflow.add_edge(START, "process_inpute")
workflow.add_edge("process_inpute", END)

graph = workflow.compile()

logger.info("Starting workflow execution")
graph.invoke({"input": "add"})  # or "sub", "mul", "div"
logger.info("Workflow execution completed")


