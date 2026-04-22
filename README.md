# Port Scanner Didattico (Python)

Mini scanner TCP multi-thread con output JSON e utilita di confronto tra run.

## Obiettivo

Questo repository serve a mostrare un piccolo esempio di tooling difensivo e di scripting orientato a workflow ripetibili: scansione, salvataggio dei risultati e confronto tra esecuzioni successive.

## Cosa mostra

- automazione di base in Python
- scansione multi-target e multi-porta
- esportazione strutturata in JSON
- confronto tra risultati per evidenziare differenze tra run

## Uso

```bash
python3 scanner.py --targets 192.168.1.1,scanme.nmap.org --ports 1-1024 --threads 200 --timeout 0.5 --out results_run1.json
python3 scanner.py --targets 192.168.1.1 --ports 22,80,443 --out run2.json
python3 compare_json.py results_run1.json run2.json
```

## Contesto

Il repository e pensato per laboratorio, apprendimento e sperimentazione difensiva autorizzata. Non e progettato come sostituto di strumenti maturi come Nmap, ma come esempio compatto di scripting e analisi comparativa dei risultati.

## Portfolio

Per una vista piu ampia dei repository orientati a strumenti e workflow vedi:
- [Technical Tooling](https://github.com/AndrewG83-sdt/cerberussec-site/blob/main/TOOLING.md)
- [cerberussec-site](https://github.com/AndrewG83-sdt/cerberussec-site)
