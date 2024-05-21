# %%
from helpers import make_post_request_from_query

base_leetcode_url: str = "https://leetcode.com/problems/"
graphql_url: str = "https://leetcode.com/graphql"
problemset_query_filename: str = "templates/get-problemset.graphql"

make_post_request_from_query(graphql_url, problemset_query_filename, json_variables={"categorySlug": "", "skip": 0, "limit": 50, "filters": {}})
