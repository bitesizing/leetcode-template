import re
import requests

def make_post_request_from_query(request_url: str, query_filepath: str, json_variables: dict = {}) -> dict:
    """
    Makes a POST request to the specified GraphQL endpoint with the given query and variables.

    Args:
        request_url (str): URL of the GraphQL endpoint.
        query_filepath (str): Path to the GraphQL query file.
        json_variables (dict, optional): Additional variables to feed into
            the JSON request. Defaults to {}.

    Raises:
        ValueError: If the operation name in the query cannot be extracted.
        requests.exceptions.HTTPError: If the request fails due to an HTTP
            error.
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
    """
    Makes a POST request to the specified URL with the given headers and JSON data.

    Args:
        url (str): URL of the request.
        headers (dict): Headers of the request.
        json (dict): JSON data of the request.

    Raises:
        requests.exceptions.HTTPError: If the request fails due to an HTTP
            error.
    """
    try:
        r = requests.post(url, headers=headers, json=json)
        r.raise_for_status()  # raise HTTPError if status code is 4xx or 5xx
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    
    return r.json()  # Return valid json object