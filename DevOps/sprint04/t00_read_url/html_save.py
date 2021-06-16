import re
import requests as req
import helper


def check_url(url):
    fuck_re = r"[^. ]*\.[^. ]"
    if url.startswith("https://") or url.startswith("http://") \
        and not (" " in url):
        newurl = url.split("//")[1]
        if not newurl.startswith(".") and len(newurl) > 0:
            if re.match(fuck_re, url) is not None:
                return True
    return False
                

def html_save(url, path):
    if check_url(url):
        helper.print_stdout(f"Sending the request to the '{url}'.")
        try:
            data_r = req.get(url)
            helper.print_stdout(f"Request to the '{url}' has been sent.")
            if data_r.status_code == 200:
                helper.print_stdout(str(data_r) + '.')
                helper.print_stdout("Parsing page data.")
                helper.print_stdout("Page data has been parsed.")
                helper.print_stdout(f"Saving page data to '{path}'.")
                with open(path, "w") as file:
                    file.write(data_r.text)
                helper.print_stdout("Page data has been saved.")
            else:
                helper.print_stderr(str(data_r))
        except Exception as err:
            helper.print_stderr(err)
    else:
        helper.print_stderr("The site URL format is invalid.")
                

    # print(resp)


html_save("https://ucode.world/","df")