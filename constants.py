import toml

# Initialise variables, including reading from config
with open('config.toml', 'r') as file:
    configs = toml.loads(file.read())
question_link: str = configs['question_link']
output_folder: str = configs['output_folder']
is_daily: bool = (question_link.strip() == "")  # get daily if q. link is empty

# Filepath variables
base_leetcode_url: str = "https://leetcode.com/problems/"
graphql_url: str = "https://leetcode.com/graphql"
templates_folderpath: str = "templates"
daily_query_filename: str = "daily-question.graphql"
problem_query_filename: str = "problem-data.graphql"
python_template_filename: str = "python_template.txt"