""" File to run a standard set of tests. """
import textwrap
from typing import Optional, Union, get_args, get_origin
from . import TreeNode, to_tree

def run_tests(examples_list: list[dict], func_in):

    # Check if values of function are TreeNodes and replace
    for input_type in examples_list[0]['inputs'].keys():
        param_type = func_in.__annotations__[input_type]
        if (param_type is TreeNode) or (get_origin(param_type) is Union and TreeNode in get_args(param_type)):
            for d in examples_list:
                d['inputs'][input_type] = to_tree(d['inputs'][input_type])

    # Run tests
    for i in range(len(examples_list)):
        example: dict = examples_list[i]
        ans = func_in(**example['inputs'])

        print(f"Example {i + 1}:")
        print(f"  inputs = {example['inputs']}")
        print(f"  answer = {ans}")
        print(f"  true answer = {example['output']}")
        if example.get('explanation') is not None: print(f"  explanation = {example['explanation']}")
        print(f"  correct = {ans == example['output']}\n")

def add_example(examples_list: list[dict], *args):
    """ Modifies examples_list inplace. """
    
    # Read inputs 
    input_names = examples_list[0]['inputs'].keys()
    input_vals, output_val = args[:-1], args[-1]

    # Populate the dictionary by modifying inplace
    examples_list.append({
        'inputs': {input_name: input_val for input_name, input_val in zip(input_names, input_vals)},
        'output': output_val
    })