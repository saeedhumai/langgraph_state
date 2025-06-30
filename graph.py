import logging
from graphschema import calculator
from tools import process_inpute
from langgraph.graph import StateGraph , START , END

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

workflow = StateGraph(calculator)
workflow.add_node("process_inpute", process_inpute)
workflow.add_edge(START, "process_inpute")
workflow.add_edge("process_inpute", END)

graph = workflow.compile()

logger.info("Starting workflow execution")
graph.invoke({"input": "add"})  # or "sub", "mul", "div"
graph.invoke({"input": "sub"})  # or "sub", "mul", "div"
graph.invoke({"input": "mul"})  # or "sub", "mul", "div"
graph.invoke({"input": "div"})  # or "sub", "mul", "div"
logger.info("Workflow execution completed")





