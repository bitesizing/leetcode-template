""" File to scrape a leetcode problem from a link and populate a template, with a given set of formatting rules. """

# %%
import os
import re
import json
import toml
import requests
from pprint import pprint
from jinja2 import Template
from bs4 import BeautifulSoup as bs

# Import configs from .toml file as dictionary
with open('config.toml', 'r') as file:
    configs = toml.loads(file.read())
question_link, output_folder, templates_folder = configs['question_link'], configs['output_folder'], configs['templates_folder']


""" CODE. """
# 1. Extract link
def extract_question_title(link: str) -> str:
    re_search = 'https://leetcode\\.com/problems/(.*)/.*'
    match = re.search(re_search, link)
    if not match: raise ValueError('No match:(')
    return match.group(1)
question_title = extract_question_title(question_link)


# 2. Write the request:)
# Get the .json query by importing - template for request
with open(templates_folder + '/query.json', 'r') as file:
    json_request = json.load(file)

# Get the graphql query - i.e., what information are we going to request
with open(templates_folder + '/problem-data.graphql', 'r') as file:
    graphql_query  = file.read()

# Populate the .json query
json_request['query'] = graphql_query
json_request['variables']['titleSlug'] = question_title


# 3. Make the request
r = requests.post('https://leetcode.com/graphql', json = json_request).json()['data']['question']

# 4. Extract data

# Get the code snippet 
def query_list_of_dicts(list_of_dicts: list[dict], key: str, value) -> dict:
    """ Returns the dictionary matching a key value pair in a given list of dictionaries. Returns empty dictionary if no match found. """
    for d in list_of_dicts:
        if d.get(key) == value: return d

code_snippets = r['codeSnippets']
python_snippet = query_list_of_dicts(code_snippets, 'langSlug', 'python3')
if python_snippet.get('code') is None: raise ValueError('No match:(')
python_code_snippet: str = python_snippet.get('code')

# Pull out the name of the function
function_line = python_code_snippet.splitlines()[-2]
function_name = re.search('.*def (.*)\\(', function_line).group(1)


# Get the description in just text
description = r['content']
soup = bs(description, 'html.parser')
text_content = soup.get_text()

# Filter out the examples from the text
description_pattern = r"^(.*?)Example"
initial_description = re.search(description_pattern, text_content, re.DOTALL).group(1)
initial_description = re.sub(r'^\s*\n', '', initial_description, flags=re.MULTILINE)

constraints_pattern =  r"(Constraints:.*)"
constraints_onwards = re.search(constraints_pattern, text_content, re.DOTALL).group(1)
constraints_onwards = re.sub(r'\n(\S+)', r'\n- \1', constraints_onwards)
constraints_onwards = re.sub(r'^\s*\n', '', constraints_onwards, flags=re.MULTILINE)

# Get the inputs, outputs and explanations
input_line_pattern = r".*Input:.*"
input_pattern = r"(\w+) = ((?:.*?)(?=\n|, \w+ =|$))"
input_lines = re.findall(input_line_pattern, text_content)
inputs = [re.findall(input_pattern, line) for line in input_lines]

output_pattern = r"Output: (.*?)(?=\n|$)"
outputs = re.findall(output_pattern, text_content)

explanation_pattern = r"Explanation: (.*?)(?=\n|$)"
explanation = re.findall(explanation_pattern, text_content)

def parse_examples(input_lists: list[list[tuple[str, str]]], output_lists: list[str]) -> list[dict]:
    # Handle inputs
    examples_list = []
    for input_list, output in zip(input_lists, output_lists):
        examples_list.append({'inputs': {}})
        for name, val in input_list: examples_list[-1]['inputs'][name] = eval(val)
        examples_list[-1]['output'] = eval(output)
    return examples_list

examples_list = parse_examples(inputs, outputs)
    

# Extract tags (NOT IMPLEMENTED YET)
tags = []
for tag_dict in r['topicTags']:
    tags.append(tag_dict['slug'])

# Get the filename
question_number = r['questionFrontendId']
question_title_slug = r['titleSlug']
filename = f'#{question_number}-{question_title_slug}.py'

# Populate the template
with open(templates_folder + '/template.txt', 'r') as file:
    template_string = file.read()

template = Template(template_string)
populated_file = template.render(
    title = r['title'],
    description = initial_description,
    constraints = constraints_onwards,
    code_snippet=python_code_snippet,
    function_name=function_name,
    examples_list=examples_list,
)

# Save file
with open(output_folder + '/' + filename, 'w') as file:
    file.write(populated_file)


def write_pretty_json(r: dict) -> str:
    prettified_data = json.dumps(r, indent=4)
    # Write the prettified data to a file
    with open('output.json', 'w') as file:
        file.write(prettified_data)

