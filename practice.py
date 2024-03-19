#! /usr/bin/env python

import requests
import argparse


def send_get_requests(url_base, filename):
    """
    Sends GET requests to URLs formed by appending each line from a file to the base URL.

    Args:
        url_base: The base URL to which lines from the file will be appended.
        filename: The path to the file containing lines to be appended.
    """

    try:
        # Open the file
        with open(filename, 'r') as file:
            for line in file:
                # Remove trailing newline character from each line
                line = line.rstrip()

                # Construct the full URL
                full_url = f"{url_base}/{line}"

                # Send GET request using requests
                response = requests.get(full_url)
                # response.raise_for_status()  # Raise exception for non-200 status codes

                # Print basic information about the request
                print(f"GET request to {full_url} - Status Code: {response.status_code}")

    except FileNotFoundError as e:
        print(f"Error: File not found: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while making the request to {full_url}. {e}")


def main():
    """
    Main function for the script. Parses arguments and calls the send_get_requests function.
    """

    # Define argument parser
    parser = argparse.ArgumentParser(
        description="Send GET requests to URLs formed by appending lines from a file to a base URL.")
    parser.add_argument("-u", "--url_base", type=str, required=True,
                        help="The base URL to which lines from the file will be appended.")
    parser.add_argument("-f", "--filename", type=str, required=True,
                        help="The path to the file containing lines to be appended.")

    # Parse arguments
    args = parser.parse_args()

    # Call send_get_requests function with parsed arguments
    send_get_requests(args.url_base, args.filename)  # Corrected typo here


if __name__ == "__main__":
    main()
