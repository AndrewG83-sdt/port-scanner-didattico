#!/usr/bin/env python3
import json, sys

if len(sys.argv) < 3:
    print("Uso: python3 compare_json.py <old.json> <new.json>")
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    old = json.load(f)["results"]
with open(sys.argv[2], "r", encoding="utf-8") as f:
    new = json.load(f)["results"]

def set_of_open(res):
    s=set()
    for host, lst in res.items():
        for item in lst:
            if item["status"]=="open":
                s.add((host, item["port"]))
    return s

old_set = set_of_open(old)
new_set = set_of_open(new)

print("Porte nuove aperte:", sorted(list(new_set - old_set)))
print("Porte non più aperte:", sorted(list(old_set - new_set)))
