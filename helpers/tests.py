""" File to run a standard set of tests. """

def run_tests(examples_list: list[dict], function):
    for i in range(len(examples_list)):
        example: dict = examples_list[i]
        ans = function(**example['inputs'])

        print(f"Example {i + 1}:")
        print(f"  inputs = {example['inputs']}\n  answer = {ans}\n  true answer = {example['output']}\n  correct = {ans == example['output']}\n")