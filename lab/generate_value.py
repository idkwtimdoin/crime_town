import yaml
import random

# Load the YAML data from the file
with open('data.yaml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

# Assuming the data is stored as a list under 'crimes'
crimes_list = data['crimes']

# Select a random value from the list
random_crime = random.choice(crimes_list)
print("Random Crime:", random_crime)
