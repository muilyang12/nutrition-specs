import re


def extract_headers(curl_command):
    headers = {}

    pattern = re.compile(r'-H\s+"([^:]+):\s+([^"]+)"')

    matches = pattern.findall(curl_command)
    for match in matches:
        headers[match[0]] = match[1]

    return headers
