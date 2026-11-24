<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:101827,100:0f766e&height=170&section=header&text=YAML%20Anchor%20Playground&fontSize=32&fontColor=ffffff&animation=fadeIn" width="100%" alt="Waving header"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&pause=900&color=14B8A6&center=true&vCenter=true&width=760&lines=Trace+YAML+anchors+and+aliases;See+merge+keys+resolve+into+data" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/yaml-anchor-playground)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/yaml-anchor-playground)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/yaml-anchor-playground?style=flat)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/yaml-anchor-playground)
<img src="assets/mark.svg" width="112" alt="YAML anchor illustration"/>
</div>

## 🧭 Overview
A safe local Python CLI that inventories YAML anchors, aliases, and merge keys, then shows the resolved data produced by PyYAML's safe loader.

## ✨ Features
- ⚓ List anchor declarations and alias references with line numbers.
- 🔀 Detect merge-key locations and show the resolved mapping.
- 🛡️ Parse with <code>safe_load</code>; never construct arbitrary Python objects.
- 📦 Print JSON for automation or review.

## 🎬 Demo
The repository includes <code>examples/anchors.yaml</code>. No hosted demo is provided.

## ⚡ Quick Start
Requires Python 3.10+.

~~~bash
python -m pip install -r requirements.txt
python yaml_anchor_lab.py examples/anchors.yaml
python yaml_anchor_lab.py examples/anchors.yaml --json
python -m unittest test_yaml_anchor_lab
~~~

## 🧰 Tech Stack
- Python 3.10+
- PyYAML 6+
- Python standard library

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
- [x] Anchor and alias inventory
- [x] Merge-key detection and safe resolved output
- [ ] Add nested example fixtures

## 🤝 Contributing
Issues and focused pull requests are welcome. Keep parsing safe, local-first, and compatible with PyYAML 6+.

## 📄 License
MIT License. See [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:101827&height=100&section=footer" width="100%" alt="Waving footer"/></div>
