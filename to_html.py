# Copyright (C) 2026 KevinCrrl
# SPDX-License-Identifier: Apache-2.0

import re
import urllib.request

import markdown


def inline_code(body: str) -> str:
    parts = re.split(r"(<pre>.*?</pre>)", body, flags=re.DOTALL)
    return "".join(
        part
        if part.startswith("<pre>")
        else part.replace("<code>", '<span class="code">').replace("</code>", "</span>")
        for part in parts
    )


def get_html(body: str, title: str = "KevinCrrl") -> str:
    return f'''<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="/KevinCrrl/static/css/styles.css">
    <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.12.0/styles/tokyo-night-dark.min.css">
    <script src="/KevinCrrl/static/js/lang.js"></script>
    <script src="/KevinCrrl/static/js/highlight/highlight11.js"></script>
    <script>hljs.highlightAll();</script>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
</head>

<body>
{inline_code(body)}
<a href="/KevinCrrl/index.html">Back to homepage</a>
<script>addTranslationLink("en", "/KevinCrrl/documentacion/pkgbuild_parser", "/KevinCrrl/documentation/pkgbuild_parser")</script>
</body>

</html>
'''.replace('<h1>pkgbuild_parser</h1>', '<h1 id="main_title">pkgbuild_parser</h1>').replace('language-python', 'python')


urllib.request.urlretrieve(
    "https://github.com/KevinCrrl/pkgbuild_parser/raw/refs/heads/main/README.md",
    "pp_readme.md",
)

with (
    open("documentation/pkgbuild_parser/index.html", "w", encoding="utf-8") as html,
    open("pp_readme.md", "r", encoding="utf-8") as md,
):
    html.write(get_html(markdown.markdown(md.read(), extensions=["tables", "fenced_code"]), "Pkgbuild Parser"))
