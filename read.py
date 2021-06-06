import requests
import argparse
import html_to_json
import json

# format_map() -> para dar formato al json

parser = argparse.ArgumentParser(description='Login through username and password')
parser.add_argument('--username', required=True, help='Username')
parser.add_argument('--password', required=True, help='Password')
args = parser.parse_args()

auth_data = {'username': args.username, 'password': args.password}
session = requests.session()
resp = session.post('https://test.unnax.com/login', data=auth_data)
resp_html = resp.text
json_html = html_to_json.convert(resp_html)

# resp_statement_1 = session.get('http://test.unnax.com/statements/1')

# print(resp_statement_1.text)