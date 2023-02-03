import sys
import subprocess
from bs4 import BeautifulSoup, Comment
import bs4


from html_helper_functions import read_pipe_or_file

# Encoding Print Alternatives {{{
def print_string_as_bytes(string):
    string_bytes = string.encode("utf-8")
        # sys.stdout.reconfigure(encoding='utf-8')
    sys.stdout.buffer.write(string_bytes)
    sys.stdout.flush()

def test_stdin_print_variations_on_soup(soup):
        # BEFORE RECONFIGURATION
    print("BEFORE RECONFIGURATION")
    print("---------- print(soup) ----------------")
    print(soup)
    print("---------- print(str(soup)) ----------------")
    print(str(soup))
    print("---------- print(soup.encode(\"utf-8\").decode(\"utf-8\")) ----------------")
    print(soup.encode("utf-8").decode("utf-8"))
    print("---------- print(str(soup).encode(\"utf-8\").decode(\"utf-8\")) ----------------")
    print(str(soup).encode("utf-8").decode("utf-8"))

    print("AFTER RECONFIGURATION")
    sys.stdout.reconfigure(encoding='utf-8')
    print("---------- print(soup) ----------------")
    print(soup)
    print("---------- print(str(soup)) ----------------")
    print(str(soup))
    print("---------- print(soup.encode(\"utf-8\").decode(\"utf-8\")) ----------------")
    print(soup.encode("utf-8").decode("utf-8"))
    print("---------- print(str(soup).encode(\"utf-8\").decode(\"utf-8\")) ----------------")
    print(str(soup).encode("utf-8").decode("utf-8"))
# }}}

def clean_soup(soup, add_style=True):
    original_title_string = soup.title.string

    # Clean the <head> tag
    custom_head_tag = soup.new_tag("head")
    custom_head_tag.append(soup.new_tag("title"))
    custom_head_tag.title.string = original_title_string
    if soup.head:
        soup.head.extract()
    if soup.title:
        soup.title.extract()
    soup.html.insert(0, custom_head_tag)



    # Remove all <script> <style> tags
    tags = soup.select("script, style")
    for tag in tags:
        tag.extract()

    # Remove all comments
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    preserve_attrs = ["href", "src", "id"]
    for child in soup.descendants:
        if type(child) != bs4.element.Tag:
            continue
        del_attrs = []
        for attr in child.attrs:
            if attr not in preserve_attrs:
                del_attrs.append(attr)
        for attr in del_attrs:
            del child[attr]

    with open(r"C:\Users\vivek\Desktop\website\template.html", "rb") as f:
        template_contents = f.read().decode("utf-8")
    template_soup = BeautifulSoup(template_contents, "html.parser")
    soup.head.replace_with(template_soup.head)
    soup.title.string = original_title_string

    return soup

if __name__ == "__main__":
    tidy_command = "tidy -indent --indent-spaces 4 -quiet --show-errors 0 --wrap-attributes no --wrap 0  "

# READ

    input_stream = sys.stdin

    soup = BeautifulSoup(input_stream.read(), "html.parser")

    soup = clean_soup(soup)
    for d in soup.select("div, span"):
        d.unwrap()
    print(soup.prettify())
    sys.exit(1)
# file_contents = read_pipe_or_file()


# PIPE
    tidy_command = "tidy -indent --indent-spaces 4 -quiet --show-errors 0 --wrap-attributes no --wrap 0"
    stdout = subprocess.run(tidy_command, input=file_contents_binary, capture_output=True).stdout

    soup = BeautifulSoup(stdout.decode("utf-8"), "html.parser")
    soup = clean_soup(soup)
    soup_binary = soup.prettify(formatter="html").encode("utf-8")

# PIPE
    stdout = subprocess.run(tidy_command, input=soup_binary, capture_output=True).stdout

# PRINT
    sys.stdout.buffer.write(stdout)
    sys.stdout.flush()

# sys.stdout.reconfigure(encoding='utf-8')
# print(soup)                                        # OPTION 1
# print(str(soup))                                 # OPTION 2
# print(soup.encode("utf-8").decode("utf-8"))      # OPTION 3
# print(str(soup).encode("utf-8").decode("utf-8")) # OPTION 4
