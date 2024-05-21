import re

def extract_question_title(base_leetcode_url: str, link: str) -> str:
    """
    Extracts the question title from a leetcode problem link.

    Args:
        base_leetcode_url (str): The base URL of leetcode.
        link (str): The link to the problem.

    Returns:
        str: The title of the problem.

    Raises:
        ValueError: If the link cannot be parsed.
    """
    re_search = base_leetcode_url + '(.*?)/.*'
    match = re.search(re_search, link)
    if not match: raise ValueError("Couldn't extract question title from provided leetcode link. Check if the link is in the correct format.")
    return match.group(1)

def query_list_of_dicts(list_of_dicts: list[dict], key: str, value) -> dict:
    """Searches a list of dictionaries for a dictionary with a specified key-value pair.

    Args:
        list_of_dicts (list[dict]): The list of dictionaries to search.
        key (str): The key to search for.
        value: The value to search for.

    Returns:
        dict: The dictionary containing the key-value pair, or an empty dictionary if no match is found.
    """

    for d in list_of_dicts:
        if d.get(key) == value: return d

def write_pretty_json(r: dict) -> str:
    prettified_data = json.dumps(r, indent=4)
    # Write the prettified data to a file
    with open('output.json', 'w') as file:
        file.write(prettified_data)
