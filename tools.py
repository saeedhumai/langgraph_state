from graph import calculator

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
        return {"cal_mul": result}
    elif value == "div":
        x = input (f"enter the first number : ")
        y = input (f"enter the second number : ")
        result = print(f"the result of {x} / {y} is { int(x) / int(y) }")
        return {"cal_div": result}


