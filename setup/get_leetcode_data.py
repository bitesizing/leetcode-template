from os.path import join as join_path

from helpers import make_post_request_from_query, extract_question_title
import constants as c

def get_problem_data_from_title_slug(title_slug: str) -> dict:
    """
    Retrieves problem data from LeetCode API based on the given title slug.

    Args:
        title_slug (str): The title slug of the problem.

    Returns:
        dict: A dictionary containing the problem data retrieved from the LeetCode API.
    """
    # Now we make the post request for the question with our chosen slug
    json_variables = {'titleSlug': title_slug}
    query_filepath = join_path(c.templates_folderpath, c.problem_query_filename)
    r = make_post_request_from_query(c.graphql_url, query_filepath, json_variables)
    data = r['data']['question']
    return data

def get_problem_title_slug() -> str:
    """
    Retrieves the title slug of a problem from the LeetCode API.

    This function checks if the problem is a daily coding challenge question. If it is, it makes an additional post request to the LeetCode API to retrieve the title slug. Otherwise, it extracts the slug directly from the provided URL.

    Returns:
        str: The title slug of the problem.

    Raises:
        ValueError: If the daily coding challenge question title slug cannot be retrieved from the API.
    """
    # If daily question, we need to get the title_slug via an additional post request
    if c.is_daily:
        daily_query_filepath = join_path(c.templates_folderpath, c.daily_query_filename)
        r = make_post_request_from_query(c.graphql_url, daily_query_filepath)
        title_slug = r['data']['activeDailyCodingChallengeQuestion']['question']['titleSlug']

    # Otherwise we can extract the slug directly from the provided url
    else: 
        title_slug = extract_question_title(c.base_leetcode_url, c.question_link)
    
    return title_slug