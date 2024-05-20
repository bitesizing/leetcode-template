# %%
import re
import requests

def make_post_request_from_query(request_url: str, query_filepath: str, json_variables: dict = {}) -> dict:
    """
        variables are additional variables to feed into the json!
    """

    # Read query from filepath
    with open(query_filepath, 'r') as file:
        graphql_query  = file.read()
    
    # Extract the name of the query
    operation_name_match = re.search(r'query\s+(\w+)', graphql_query)
    if not operation_name_match: raise ValueError("Couldn't extract operation name from provided graphql query. Check that query has a valid name.")
    operation_name = operation_name_match.group(1)

    # Compose headers and data
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "operationName": operation_name,
        "query": graphql_query,
        'variables': json_variables,
    }

    # Make response
    return make_post_request(request_url, headers, data)

def make_post_request(url: str, headers: dict, json: dict) -> dict:
    """ Note... this doesn't return properly when using interactive notebook in VScode. """
    try:
        r = requests.post(url, headers=headers, json=json)
        print(r.raise_for_status())
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    
    return r.json()  # Return valid json object

url = "https://leetcode.com/graphql"
query_filepath = "templates/problem-data.graphql"
json_variables = {
    'titleSlug': 'two-sum'
}
r = make_post_request_from_query(url, query_filepath, json_variables)
print(r)