/*
@licstart  The following is the entire license notice for the JavaScript code in this file.

Script for my personal website
Copyright (C) 2026 KevinCrrl

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

@licend  The above is the entire license notice
for the JavaScript code in this file.
*/

let userLang = "en";

if (navigator.language.startsWith("es")) {
    userLang = "es";
}

function addTranslationLink(pageLang) {
    if (pageLang != userLang) {
        const linkDiv = document.createElement("div");
        const link = document.createElement("a");
        linkDiv.className = "aviso";
        let content = "";
        if (userLang == "es" && pageLang != "es") {
            content = document.createTextNode("Se detectó el idioma español en su navegador, ¿Desea cambiar a la traducción disponible? ");
            link.href = "/KevinCrrl/documentacion/pkgbuild_parser/";
            link.textContent = "Ir a traducción";
        } else if (userLang != "es" && pageLang == "es") {
            content = document.createTextNode("The language in your browser does not appear to be Spanish, ¿Go to the English translation?: ");
            link.href = "/KevinCrrl/documentation/pkgbuild_parser/";
            link.textContent = "Go to translation"
        }

        linkDiv.appendChild(content);
        linkDiv.appendChild(link);

        const title = document.getElementById("main_title");

        document.body.insertBefore(linkDiv, title);
    }
}
