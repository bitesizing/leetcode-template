""" File to scrape a leetcode problem from a link and populate a template, with a given set of formatting rules. """

# %%
import os
import re
import json
import toml

from pprint import pprint
from jinja2 import Template
from bs4 import BeautifulSoup as bs
from os.path import join as join_url

from helpers import extract_question_title, make_post_request_from_query, query_list_of_dicts

# Set current working directory to directory of the script... (helps with running from parent directory)
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(script_dir)

# Initialise variables, including reading from config
with open('config.toml', 'r') as file:
    configs = toml.loads(file.read())
question_link: str = configs['question_link']
output_folder: str = configs['output_folder']
is_daily: bool = (question_link.strip() == "")  # get daily if q. link is empty

# Filepath variables
base_leetcode_url: str = "https://leetcode.com/problems/"
graphql_url: str = "https://leetcode.com/graphql"
templates_folderpath: str = "templates"
daily_query_filename: str = "daily-question.graphql"
problem_query_filename: str = "problem-data.graphql"
python_template_filename: str = "python_template.txt"


""" CODE. """
# 1. Make post request for data

# If daily question, we need to get the title_slug via an additional post request
if is_daily:
    daily_query_filepath = join_url(templates_folderpath, daily_query_filename)
    r = make_post_request_from_query(graphql_url, daily_query_filepath)
    title_slug = r['data']['activeDailyCodingChallengeQuestion']['question']['titleSlug']

# Otherwise we can extract the slug directly from the provided url
else: 
    title_slug = extract_question_title(base_leetcode_url, question_link)

# Now we make the post request for the question with our chosen slug
json_variables = {'titleSlug': title_slug}
query_filepath = join_url(templates_folderpath, problem_query_filename)
r = make_post_request_from_query(graphql_url, query_filepath, json_variables)
data = r['data']['question']


# TODO: turn this into custom class instead of dict**2. Import properly from helpers
# I can pull some custom classes in from my project code to help with this.
languages = {
    'python3': {
        'function_line': 1,
        'function_pattern': '.*def (.*)\\(',
    }
}

# 2. Extract code
def generate_template_from_leetcode_data(data: dict, language: str = 'python3') -> str:

    def get_code_snippet_data(data: dict, language: str) -> tuple[str, str]:
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

        return code_snippet, function_name

    def process_description_text(data: dict) -> tuple[str, str, list[dict]]:
        def generate_examples_list(input_lists: list[list[tuple[str, str]]], output_lists: list[str]) -> list[dict]:
            # Handle inputs
            examples_list = []
            for input_list, output in zip(input_lists, output_lists):
                examples_list.append({'inputs': {}})
                for name, val in input_list: examples_list[-1]['inputs'][name] = eval(val)
                examples_list[-1]['output'] = eval(output)
            return examples_list
        
        # Get description content by parsing html within data dict, then filter out non-breaking spaces.
        full_desc_text = re.sub(r'\xa0', ' ', bs(data['content'], 'html.parser').get_text())

        # Get the introduction and constraints.
        introduction_text = re.search(r"^(.*?)Example", full_desc_text, re.DOTALL).group(1)
        introduction_text = re.sub(r'^\s*\n', '', introduction_text, flags=re.MULTILINE)

        constraints_text = re.search(r"(Constraints:.*)", full_desc_text, re.DOTALL).group(1)
        constraints_text = re.sub(r'\n(\S+)', r'\n- \1', constraints_text)
        constraints_text = re.sub(r'^\s*\n', '', constraints_text, flags=re.MULTILINE)

        # Get the inputs, outputs and explanations
        input_line_pattern = r".*Input:.*"
        input_pattern = r"(\w+) = ((?:.*?)(?=\n|, \w+ =|$))"
        input_lines = re.findall(input_line_pattern, full_desc_text)
        inputs = [re.findall(input_pattern, line) for line in input_lines]

        output_pattern = r"Output: (.*?)(?=\n|$)"
        outputs = re.findall(output_pattern, full_desc_text)
        examples_list = generate_examples_list(inputs, outputs)

        explanation_pattern = r"Explanation: (.*?)(?=\n|$)"
        explanation = re.findall(explanation_pattern, full_desc_text)

        return introduction_text, constraints_text, examples_list

    # Get the description in just text
    code_snippet, function_name = get_code_snippet_data(data, language)
    introduction_text, constraints_text, examples_list = process_description_text(data)

    # Extract tags (NOT IMPLEMENTED YET)
    tags = []
    for tag_dict in data['topicTags']:
        tags.append(tag_dict['slug'])

    # Get the filename
    question_number = data['questionFrontendId']
    question_title_slug = data['titleSlug']
    output_filename = f'#{question_number}-{question_title_slug}.py'

    # Populate the template
    with open(join_url(templates_folderpath, python_template_filename), 'r') as file:
        template = Template(file.read())
    
    populated_file = template.render(
        link = base_leetcode_url + question_title_slug + '/',
        title = data['title'],
        description = introduction_text,
        constraints = constraints_text,
        code_snippet = code_snippet,
        function_name = function_name,
        examples_list = examples_list,
    )

    # Save file
    with open(join_url(output_folder, output_filename), 'w') as file:
        file.write(populated_file)
        pprint('Wrote correctly!')

generate_template_from_leetcode_data(data)

def write_pretty_json(r: dict) -> str:
    prettified_data = json.dumps(r, indent=4)
    # Write the prettified data to a file
    with open('output.json', 'w') as file:
        file.write(prettified_data)

