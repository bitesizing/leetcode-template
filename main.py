""" File to scrape a leetcode problem from a link and populate a template, with a given set of formatting rules. """

# %%
import os
if __name__ == "__main__": os.chdir(os.path.dirname(os.path.realpath(__file__)))  # Change current working directory to directory of this file
from setup import generate_problem_file_from_leetcode_data, get_problem_data_from_title_slug, get_problem_title_slug

# Generate file
data = get_problem_data_from_title_slug(get_problem_title_slug())
generate_problem_file_from_leetcode_data(data)