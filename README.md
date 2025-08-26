# Port Scanner Didattico (Python)
Mini scanner TCP multi-thread con output JSON e utilità di diff tra run.

## Uso
```bash
python3 scanner.py --targets 192.168.1.1,scanme.nmap.org --ports 1-1024 --threads 200 --timeout 0.5 --out results_run1.json
python3 scanner.py --targets 192.168.1.1 --ports 22,80,443 --out run2.json
python3 compare_json.py results_run1.json run2.json
