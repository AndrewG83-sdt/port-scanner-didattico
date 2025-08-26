### `scanner.py`
```python
#!/usr/bin/env python3
import socket, json, argparse, concurrent.futures, time

def parse_ports(s):
    res = set()
    for part in s.split(","):
        if "-" in part:
            a,b = part.split("-")
            res.update(range(int(a), int(b)+1))
        else:
            res.add(int(part))
    return sorted(res)

def scan_host_port(host, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            start = time.time()
            result = sock.connect_ex((host, port))
            elapsed = time.time() - start
            if result == 0:
                return {"host": host, "port": port, "status": "open", "rtt": round(elapsed, 4)}
            else:
                return {"host": host, "port": port, "status": "closed", "rtt": round(elapsed, 4)}
    except Exception as e:
        return {"host": host, "port": port, "status": f"error: {e}"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--targets", required=True, help="lista target separati da virgola")
    ap.add_argument("--ports", default="1-1024", help="es 1-1024 oppure 22,80,443")
    ap.add_argument("--threads", type=int, default=200)
    ap.add_argument("--timeout", type=float, default=0.5)
    ap.add_argument("--out", default="results.json")
    args = ap.parse_args()

    targets = [t.strip() for t in args.targets.split(",") if t.strip()]
    ports = parse_ports(args.ports)

    jobs = [(h, p) for h in targets for p in ports]
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as ex:
        futs = [ex.submit(scan_host_port, h, p, args.timeout) for h,p in jobs]
        for f in concurrent.futures.as_completed(futs):
            results.append(f.result())

    grouped = {}
    for r in results:
        grouped.setdefault(r["host"], []).append(r)
    for h in grouped:
        grouped[h] = sorted(grouped[h], key=lambda x: x["port"])

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump({"scanned_at": time.strftime("%Y-%m-%d %H:%M:%S"), "results": grouped}, f, indent=2)
    print(f"[+] Risultati salvati in {args.out}")

if __name__ == "__main__":
    main()
