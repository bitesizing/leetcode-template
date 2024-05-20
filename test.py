# %%
question_link = """

"""
print(question_link.strip() == "")

# %%


url = "https://leetcode.com/graphql"
query_filepath = "templates/problem-data.graphql"
json_variables = {
    'titleSlug': 'two-sum'
}
r = make_post_request_from_query(url, query_filepath, json_variables)
print(r)