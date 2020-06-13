# Encoding Issues When Reading From STDIN:
# 
# INPUT:
#     
#   <p>What to write down when you&#8217;re reading to learn &#8211; Aceso Under Glass</p>
#   <p>  – </p>
# 
# CODE 1:
#     sys.stdout.reconfigure(encoding='utf-8')
#     ...
#     print(soup)   
# OUTPUT 1:
#     <p>What to write down when you’re reading to learn – Aceso Under Glass</p>
#     <p> â€” â€“ </p>
#
# CODE 2:
#     # sys.stdout.reconfigure(encoding='utf-8')
#     ...
#     print(soup)
# OUTPUT 2:
#     <p>What to write down when youre reading to learn  Aceso Under Glass</p>
#     <p> â â </p>

import sys
import argparse

from bs4 import BeautifulSoup
import bs4
soup = ""
preserve_attrs = ["href", "src"]

# with open("sans_serif.html", "r") as f:
#     file_contents = f.read().decode("utf-8")
def read_pipe_or_file():
    stream_is_interactive = sys.stdin.isatty()
    if stream_is_interactive:
        parser = argparse.ArgumentParser(description="Removes attributes from a HTML file")
        parser.add_argument("input_filename")
        args = parser.parse_args()
        with open(args.input_filename, "rb") as f:
            file_contents = f.read().decode("utf-8")
    else:
        # sys.stdout.reconfigure(encoding='utf-8')
        input_stream = sys.stdin
        file_contents = input_stream.read()
    return file_contents


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
    # print("---------- sys.stdout.buffer.write(str(soup).encode(\"utf-8\")) ----------------")
    # sys.stdout.buffer.write(str(soup).encode("utf-8"))
    # sys.stdout.flush()

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
    # print("---------- sys.stdout.buffer.write(str(soup).encode(\"utf-8\")) ----------------")
    # sys.stdout.buffer.write(str(soup).encode("utf-8"))
    # sys.stdout.flush()


        

file_contents = read_pipe_or_file()
soup = BeautifulSoup(file_contents, "html.parser")

sys.exit(1)

for child in soup.body.descendants:
    if type(child) != bs4.element.Tag:
        continue
    del_attrs = []
    for attr in child.attrs:
        if attr not in preserve_attrs:
            del_attrs.append(attr)
    for attr in del_attrs:
        del child[attr]

print(soup.encode("utf-8").decode("utf-8"))

# html_string = str(soup.prettify()).split("\n") 
# for line in html_string:
#     print(line)
