""" File to scrape a leetcode problem from a link and populate a template, with a given set of formatting rules. """

# %%
import os

from setup import generate_problem_file_from_leetcode_data, get_problem_data_from_title_slug, get_problem_title_slug

# Set current working directory to directory of the script... (helps with running from parent directory)
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(script_dir)

data = get_problem_data_from_title_slug(get_problem_title_slug())
generate_problem_file_from_leetcode_data(data)

