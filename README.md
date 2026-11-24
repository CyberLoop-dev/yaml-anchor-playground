<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:101827,100:0f766e&height=170&section=header&text=YAML%20Anchor%20Playground&fontSize=32&fontColor=ffffff&animation=fadeIn" width="100%" alt="Waving header"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&pause=900&color=14B8A6&center=true&vCenter=true&width=760&lines=A%20safe%20local%20Python%20CLI%20that%20inventories%20YAML%20anchors%2C%20aliases%2C%20and%20merge%20k" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/yaml-anchor-playground)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/yaml-anchor-playground)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/yaml-anchor-playground?style=flat)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/yaml-anchor-playground)
<img src="assets/mark.svg" width="112" alt="YAML Anchor Playground illustration"/>
</div>

## 🧭 Overview

A safe local Python CLI that inventories YAML anchors, aliases, and merge keys, then shows the resolved data produced by PyYAML's safe loader.

## ✨ Features

- ⚓ List anchor declarations and alias references with line numbers.
- 🔀 Detect merge-key locations and show the resolved mapping.
- 🛡️ Parse with safe_load; never construct arbitrary Python objects.
- 📦 Print JSON for automation or review.

## 🎬 Demo

No hosted demo is provided. Run the local example with the command below.

## ⚡ Quick Start

~~~bash
python yaml_anchor_lab.py examples/anchors.yaml
~~~

## 🧰 Tech Stack

- Python 3.10+ · PyYAML
- Local-first execution; no external API calls

## 🗂️ Folder Structure

~~~text
yaml-anchor-playground/
├── yaml_anchor_lab.py
├── requirements.txt
├── examples/anchors.yaml
├── test_yaml_anchor_lab.py
├── assets/mark.svg
├── .gitignore
├── LICENSE
└── README.md
~~~

## 🗺️ Roadmap

- [x] Core behavior and local examples
- [x] Custom SVG and setup documentation
- [ ] Add more guided exercises from community feedback

## 🤝 Contributing

Issues and focused pull requests are welcome. Keep examples reproducible and within the documented scope.

## 📄 License

MIT License. See [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:101827&height=100&section=footer" width="100%" alt="Waving footer"/></div>
