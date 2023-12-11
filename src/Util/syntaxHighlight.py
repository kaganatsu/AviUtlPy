import subprocess

import bs4
from bs4 import BeautifulSoup


def html2avi_utl_format(html: str):
    tag = "<{0}>{1}<#>"
    color_dict = dict(keyword="#cc7832",
                      title="#cc7832",
                      title_class_="#a9b7c6",
                      title_function_="#ffc66d",
                      function="#ffc66d",
                      built_in="#9876aa",
                      params="#a9b7c6",
                      literal="#cc7832",
                      number="#6897bb",
                      string="#6a8759",
                      comment="#808080")
    default_color = "#a9b7c6"
    texts = []
    soup = BeautifulSoup(html, "html.parser")
    for item in soup:
        if type(item) is bs4.element.Tag:
            class_ = "_".join(item["class"])
            texts.append(tag.format(color_dict[class_[5:]], item.text))
        else:
            texts.append(tag.format(default_color, item))
    return "".join(texts)


def highlight(code: str) -> str:
    ret = subprocess.run(["node", "../script/syntaxHighlight.js", code], capture_output=True, text=True, encoding="utf-8")
    return html2avi_utl_format(ret.stdout.rstrip("\n"))
