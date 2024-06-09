import re
import json

from pprint import pprint
from jinja2 import Template
from bs4 import BeautifulSoup as bs
from os.path import join as join_path

from helpers import query_list_of_dicts
import constants as c

# TODO: turn this into custom class instead of dict**2. Import properly from helpers
# I can pull some custom classes in from my project code to help with this.
languages = {
    'python3': {
        'function_line': 1,
        'function_pattern': '.*def (.*)\\(',
    }
}

def generate_problem_file_from_leetcode_data(data: dict, language: str = 'python3') -> dict:

    def get_code_snippet_data(data: dict, language: str) -> dict:
        """
        Get code snippet and function name from leetcode data for a given language.

        Args:
            data (dict): Leetcode data for a specific problem parsed from GraphQL. 
                - Must contain 'codeSnippets' (list[dict]), with each dict containing 'langSlug' key.
            language (str): Language for which code snippet needs to be obtained. Must be a key in the languages dictionary.

        Returns:
            A tuple containing two values:
                - code_snippet: A string containing the code snippet for the given language, or an empty string if no matching snippet was found.
                - function_name: A string containing the name of the function in the code snippet, or an empty string if no matching function was found.

        Raises:
            ValueError: If the language is not found in the languages dictionary or if there is no code snippet for the given language.
        """
        # Get code snippet by querying list of dictionaries for key value pair
        code_snippet: str = query_list_of_dicts(data['codeSnippets'], key='langSlug', value=language).get('code')
        if code_snippet is None: raise ValueError(f'Could not get code snippet for language "{language}."')

        # Obtain function name
        language_dict: dict = languages[language]  # TEST IF THIS WORKS
        match: re.Match = re.search(language_dict['function_pattern'], code_snippet.splitlines()[language_dict['function_line']])
        if match is None: raise ValueError(f'Could not get function name from provided code snippet.')
        function_name = match.group(1)

        return {'code_snippet': code_snippet, 'function_name': function_name}

    def process_description_text(data: dict) -> tuple[str, str, list[dict]]:
        """
        Process the description text to extract the introduction, constraints, inputs, outputs, and explanations.

        Args:
            data (dict): The data dictionary containing the description content.

        Returns:
            tuple[str, str, list[dict]]: A tuple containing the following:
                - introduction_text (str): The introduction text.
                - constraints_text (str): The constraints text.
                - examples_list (list[dict]): A list of dictionaries containing the input-output examples.
                    Each dictionary contains the following keys:
                        - inputs (dict): A dictionary of input values.
                        - output (str): The expected output value.

        """
        def generate_examples_list(examples: list[list]) -> list[dict]:
            """
            Generates a list of dictionaries containing examples for a given problem.

            Args:
                examples (list[list]): A list of lists, where each list contains three elements:
                    - input_list (list[tuple]): A list of tuples, where each tuple contains two elements:
                        - name (str): The name of the input.
                        - val (str): The value of the input.
                    - output (str): The expected output value.
                    - explanation (str): An optional explanation for the example.
            Returns:
                list[dict]: A list of dictionaries, where each dictionary contains an 'inputs' key
                    with a dictionary of input values, and an 'output' key with the expected output value.
            """
            # Handle inputs
            # Some inputs don't evaluate properly, so you have to map them. Can update as needed.
            eval_map = {
                'true': 'True',
                'false': 'False'
            }

            def replace_eval(eval_string: str):
                for key, value in eval_map.items():
                    eval_string = eval_string.replace(key, value)
                return eval(eval_string)
            
            examples_list = []
            for input_list, output, explanation in examples:
                example_dict = {'inputs': {}}
                for name, val in input_list: example_dict['inputs'][name] = replace_eval(val)
                example_dict['output'] = replace_eval(output)
                if len(explanation) > 0: example_dict['explanation'] = explanation[0]
                examples_list.append(example_dict)
            return examples_list
        
        # Get description content by parsing html within data dict, then filter out non-breaking spaces.
        if not data['content']: raise ValueError("Question content not found (check if Premium question)")
        full_desc_text = re.sub(r'\xa0', ' ', bs(data['content'], 'html.parser').get_text())

        # Get the introduction and constraints.
        introduction_text = re.search(r"^(.*?)Example", full_desc_text, re.DOTALL).group(1).strip()
        constraints_text = re.search(r"(Constraints:.*)", full_desc_text, re.DOTALL).group(1)
        constraints_text = re.sub(r'\n(\S+)', r'\n- \1', constraints_text).strip()

        # Split data into each Example
        # '\d+' matches to one or more (+) digits (\d)
        # '(.*?)' matches every character (.*) non-greedily (?), meaning shortest n_ characters until...
        # '?=Example \d+:' is a 'positive' lookahead (meaning it checks for chars without parsing them) for the next example
        # '|\Z' also matches the enx of the string
        examples_pattern = re.compile(r'Example \d+:(.*?)(?=Example \d+:|\Z)', re.DOTALL)  # compile pattern, DOTALL means dots cover newlines
        examples = examples_pattern.findall(full_desc_text)  # give us each match, split into a list

        formatted_examples = []
        for example in examples:
            input_line = re.compile(r'^Input:\s*(.*)', re.MULTILINE).findall(example)[0]
            output_line = re.compile(r'^Output:\s*(.*)', re.MULTILINE).findall(example)[0]
            expl_line = re.compile(r'^Explanation:\s*(.*)', re.MULTILINE).findall(example)

            # Sort into list of inputs, outputs, explanations
            input_pattern = r"(\w+) = ((?:.*?)(?=\n|, \w+ =|$))"
            formatted_examples.append([
                re.findall(input_pattern, input_line),
                output_line,
                expl_line
            ])
        examples_list = generate_examples_list(formatted_examples)
        return {'introduction_text': introduction_text, 'constraints_text': constraints_text, 'examples_list': examples_list}

    # Get the filename
    question_title_slug = data['titleSlug']
    output_filename = f"#{data['questionFrontendId']}-{question_title_slug}.py"

    # Handle tags (not in function bc very easy)
    tags = ', '.join(f"#{d['slug']}" for d in data['topicTags'])

    # Generate variables to populate template with
    template_variables = {
        'link': c.base_leetcode_url + question_title_slug + '/',
        'title': data['title'],
        'tags': tags
    }
    template_variables.update(process_description_text(data))
    template_variables.update(get_code_snippet_data(data, language))

    # Read and populate the template
    with open(join_path(c.templates_folderpath, c.python_template_filename), 'r') as file:
        template = Template(file.read())
    populated_file = template.render(**template_variables)

    # Save file
    with open(join_path(c.output_folder, output_filename), 'w') as file:
        file.write(populated_file)
        pprint('Wrote correctly!')