# Copyright (C) 2026 KevinCrrl
# SPDX-License-Identifier: Apache-2.0

import urllib.request

import markdown


def get_html(body: str, title: str = "KevinCrrl") -> str:
    return f'''<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="/KevinCrrl/estilos.css">
    <script src="/KevinCrrl/static/js/lang.js"></script>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
</head>

<body>
{body}
<a href="/KevinCrrl/index.html">Back to homepage</a>
<script>addTranslationLink("en");</script>
</body>

</html>
'''


urllib.request.urlretrieve(
    "https://github.com/KevinCrrl/pkgbuild_parser/raw/refs/heads/main/README.md",
    "pp_readme.md",
)

with (
    open("documentation/pkgbuild_parser/index.html", "w", encoding="utf-8") as html,
    open("pp_readme.md", "r", encoding="utf-8") as md,
):
    html.write(get_html(markdown.markdown(md.read(), extensions=["tables", "fenced_code"]), "Pkgbuild Parser"))
