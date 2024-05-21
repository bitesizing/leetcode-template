""" File to scrape a leetcode problem from a link and populate a template, with a given set of formatting rules. """

# %%
import os
import toml

from pprint import pprint
from os.path import join as join_url

from helpers import extract_question_title, make_post_request_from_query
import constants as c
from setup import generate_problem_file_from_leetcode_data

# Set current working directory to directory of the script... (helps with running from parent directory)
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(script_dir)

# If daily question, we need to get the title_slug via an additional post request
if c.is_daily:
    daily_query_filepath = join_url(c.templates_folderpath, c.daily_query_filename)
    r = make_post_request_from_query(c.graphql_url, daily_query_filepath)
    title_slug = r['data']['activeDailyCodingChallengeQuestion']['question']['titleSlug']

# Otherwise we can extract the slug directly from the provided url
else: 
    title_slug = extract_question_title(c.base_leetcode_url, c.question_link)

# Now we make the post request for the question with our chosen slug
json_variables = {'titleSlug': title_slug}
query_filepath = join_url(c.templates_folderpath, c.problem_query_filename)
r = make_post_request_from_query(c.graphql_url, query_filepath, json_variables)
data = r['data']['question']

generate_problem_file_from_leetcode_data(data)

