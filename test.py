# %%
import toml

with open('templates/config_template.toml', 'r') as file:
    toml_data = file.read()

# Parse the TOML data
parsed_data = toml.loads(toml_data)