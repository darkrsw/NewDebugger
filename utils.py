from typing import List

INPUTS: List[str] = []

original_input = input

def input(prompt: str) -> str:
    given_input = None
    try:
        global INPUTS
        given_input = INPUTS[0]
        INPUTS = INPUTS[1:]
    except:
        pass

    if given_input:
        print(f"{prompt} {given_input}")
        return given_input

    return original_input(prompt)

def next_inputs(list: List[str] = []) -> List[str]:
    global INPUTS
    INPUTS += list
    return INPUTS

def clear_next_inputs():
    global INPUTS
    INPUTS = []
    return INPUTS
