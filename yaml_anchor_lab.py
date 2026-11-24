#!/usr/bin/env python3
"""Inspect YAML anchors, aliases, merge keys, and safe-load output."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any
import yaml
from yaml.tokens import AliasToken, AnchorToken, ScalarToken

def inspect_yaml(text: str) -> dict[str, Any]:
    anchors, aliases, merges = [], [], []
    for token in yaml.scan(text):
        line = token.start_mark.line + 1
        if isinstance(token, AnchorToken):
            anchors.append({"name": token.value, "line": line})
        elif isinstance(token, AliasToken):
            aliases.append({"name": token.value, "line": line})
        elif isinstance(token, ScalarToken) and token.value == "<<":
            merges.append({"line": line})
    resolved = yaml.safe_load(text)
    return {"anchors": anchors, "aliases": aliases, "merge_keys": merges, "resolved": resolved}

def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect YAML anchors and aliases safely.")
    parser.add_argument("file", type=Path, help="YAML file to inspect")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = parser.parse_args()
    try:
        report = inspect_yaml(args.file.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return
    print(f"File: {args.file}")
    for label in ("anchors", "aliases", "merge_keys"):
        print(f"{label.replace('_', ' ').title()}: {len(report[label])}")
        for item in report[label]:
            print(f"  line {item['line']}: {item.get('name', '<<')}")
    print("\nResolved data:")
    print(json.dumps(report["resolved"], indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
