# %%
from helpers import make_post_request_from_query

base_leetcode_url: str = "https://leetcode.com/problems/"
graphql_url: str = "https://leetcode.com/graphql"
problemset_query_filename: str = "templates/get-problemset.graphql"

a = make_post_request_from_query(graphql_url, problemset_query_filename, json_variables={"categorySlug": "", "skip": 0, "limit": -1, "filters": {}})['data']['problemsetQuestionList']


# Get all values for one entry in a list of dicationaries
dict_values = set()
for question in a['questions']:
    dict_values.add(question['paidOnly'])
