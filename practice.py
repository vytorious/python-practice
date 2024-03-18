#! /usr/bin/env python

import requests

# Define the URL
url = "https://google.com"

# Send a GET request and handle the response
try:
  response = requests.get(url)
  response.raise_for_status()  # Raise an exception for non-200 status codes

  # Access the response content
  content = response.status_code

  # Print the response content (optional)
  print(content)

except requests.exceptions.RequestException as e:
  print(f"Error: An error occurred while making the request. {e}")