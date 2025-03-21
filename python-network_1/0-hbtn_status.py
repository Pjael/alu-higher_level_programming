#!/usr/bin/python3
"""fetches https://alu-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__name__":
    """fetches https://alu-intranet.hbtn.io/status"""
    with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as response:
        html = response.read()
        html_str = html.decode("utf-8")

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf-8 content: {}".format(html_str))