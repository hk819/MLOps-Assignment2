import json
import re

# load the extracted data from the JSON file
with open('articles.json', 'r') as file:
    extracted_data = json.load(file)

# function to preprocess text data
def preprocess_text(text):
    # remove special characters and extra whitespaces
    processed_text = re.sub(r'[^\w\s]', '', text)
    processed_text = re.sub(r'\s+', ' ', processed_text)
    # convert text to lowercase
    processed_text = processed_text.lower()
    return processed_text

# preprocess titles and descriptions
for source in extracted_data:
    for key in ['titles', 'descriptions']:
        extracted_data[source][key] = [preprocess_text(text) for text in extracted_data[source][key]]

# save the preprocessed data to the same JSON file
with open('articles2.json', 'w') as file:
    json.dump(extracted_data, file)