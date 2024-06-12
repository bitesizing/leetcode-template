""" File to run a standard set of tests. """
import textwrap
from typing import Optional, Union, get_args, get_origin, Callable
from . import TreeNode, to_tree

class Examples():
    def __init__(self, examples_list: list[dict], func_in: Callable):
        self.original_examples: list[dict] = examples_list
        self.input_names = examples_list[0]['inputs'].keys()
        self.check_legal_types(self.original_examples)  # convert input types to legal

        self.func_in: Callable = func_in
        self.added_examples = []
    
    @property
    def examples_list(self):
        return self.original_examples + self.added_examples

    def run_tests(self, added_only: bool = False):
        """ Parent function to run a list of examples, either just the added or all currently in the class. """
        examples_list = self.added_examples if added_only else self.examples_list
        self.run_and_print(examples_list)
    
    def run_and_print(self, examples_list: list[dict]):
        """ Runs a given list of examples and prints the result. """
        # Run tests and print result
        for i in range(len(examples_list)):
            example: dict = examples_list[i]
            ans = self.func_in(**example['inputs'])

            print(f"Example {i + 1}:")
            print(f"  inputs = {example['inputs']}")
            print(f"  answer = {ans}")
            print(f"  true answer = {example['output']}")
            if example.get('explanation') is not None: print(f"  explanation = {example['explanation']}")
            print(f"  correct = {ans == example['output']}\n")

    def add_example(self, *args):
        """ Appends an example to the added_examples dictionary. Also converts types. """

        added_example = [{
            'inputs': {input_name: input_val for input_name, input_val in zip(self.input_names, args[:-1])},
            'output': args[-1]
        }]
        self.check_legal_types(added_example)  # convert input types to legal
        self.added_examples.extend(added_example)  # add to added examples list

    def check_legal_types(self, examples_list: list[dict]):
        """ Checks if all type hints given in the input function are of a legal type, and converts if not. 
            Currently only supports TreeNodes.
        """
        # Check if values of function are special types and replace (currently only supports TreeNode)
        for input_type in self.input_names:
            param_type = self.func_in.__annotations__[input_type]

            # Convert TreeNode inputs to parsable format
            if (param_type is TreeNode) or (get_origin(param_type) is Union and TreeNode in get_args(param_type)):
                for d in examples_list:
                    d['inputs'][input_type] = to_tree(d['inputs'][input_type])