import re
import os
import sys
import helper
import webbrowser

def check_url(url):
    fuck_re = r"[^. ]*\.[^. ]"
    if url.startswith("https://www.youtube.com/") or url.startswith("http://www.youtube.com/") \
        and not (" " in url):
        newurl = url.split("//")[1]
        if not newurl.startswith(".") and len(newurl) > 0:
            if re.match(fuck_re, url) is not None:
                return True
    return False



def youtube():
    if len(sys.argv) < 2:
        helper.print_stderr("The site URL was not passed.")
    else:
        url = sys.argv[1]
        if check_url(url):
            helper.print_stdout(f"Opening the YouTube video at {url}.")
            try:
                webbrowser.open(url)
                helper.print_stdout(f"YouTube video opened.")
            except Exception as err:
                helper.print_stderr(err)
        else:
            helper.print_stderr("The URL is invalid.")



youtube()