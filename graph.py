from typing_extensions import TypedDict

from typing import Annotated

from langgraph.graph import StateGraph , Start , END


class StatA(TypedDict):
    a: int


def process_inpute(state: StatA) -> StatA:
    return {"a": state["a"] + 1}


workflow = StateGraph(StatA)

workflow.add_node("process_inpute", process_inpute)
workflow.add_edge(Start, "process_inpute")
workflow.add_edge("process_inpute", END)

graph = workflow.compile()








