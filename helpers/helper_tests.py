""" File to run a standard set of tests. """
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
        print(f"  inputs = {example['inputs']}\n  answer = {ans}\n  true answer = {example['output']}\n  correct = {ans == example['output']}\n")