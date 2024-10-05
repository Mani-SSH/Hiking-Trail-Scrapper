import requests
from bs4 import BeautifulSoup
import csv
import os

url = 'https://www.thirdrockadventures.com/blog/new-trekking-routes-in-nepal'
response = requests.get(url)

if response.status_code == 200:
    print("Successfully retrieved the webpage.")
    soup = BeautifulSoup(response.text, 'html.parser')

    trek_names = []
    trek_list_section = soup.find('div', class_='notecontent')

    if trek_list_section:
        print("Found the trek list section.")
        treks = trek_list_section.find_all('li')
        for trek in treks:
            trek_name = trek.text.strip()
            trek_names.append(trek_name)
    else:
        print("Could not find the trek list section.")

    # Set the file path relative to the current script
    file_path = f'{os.getcwd()}/Data/raw_data.csv'

    # Check and create the directory if it doesn't exist
    if not os.path.exists(os.path.dirname(file_path)):
        print("Directory does not exist. Creating now...")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Print current working directory
    print("Current Working Directory:", os.getcwd())

    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Trek Name'])
            for name in trek_names:
                writer.writerow([name])
        print(f'Successfully saved {len(trek_names)} trek names to {file_path}')
    except Exception as e:
        print("Error writing to the file:", e)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
