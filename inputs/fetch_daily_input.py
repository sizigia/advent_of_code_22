import requests
import os
import sys
from dotenv import load_dotenv
load_dotenv()

COOKIES = {'session': os.environ.get('AOC_SESSION')}


input_url = 'https://adventofcode.com/2022/day/{}/input'.format(sys.argv[1])
response = requests.get(input_url, cookies=COOKIES)
file_name = os.path.join('inputs/', 'input_d{}.txt'.format(sys.argv[1]))

if response.status_code and not os.path.exists(file_name):
    file = open(file_name, 'wb')
    file.write(response.content)
    file.close()