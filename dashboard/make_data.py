# Builds the dashboard's data files from the project's own outputs (alignment and results tables).
import json, math, collections, csv, re, sys
D = sys.argv[1]  # the "Bioinformatics project data" folder
CORE = {"P99999", "P99998", "Q6WUX8", "Q5RFH4"}
HEME = {15: "Cys", 18: "Cys", 19: "His", 81: "Met"}  # human P99999 numbering, incl. initiator Met

recs, h, seq = [], None, ""
for line in open(f"{D}/data/cytc_aligned.fasta"):
    line = line.strip()
    if line.startswith(">"):
        if h: recs.append((h, seq))
        h, seq = line[1:], ""
    else:
        seq += line
recs.append((h, seq))
human = next(s for h, s in recs if "P99999" in h)

species = []
for h, s in recs:
    label, rest = h.split(" ", 1)
    organism, group = [x.strip() for x in rest.split("|")]
    acc = label.rsplit("_", 1)[1]
    pairs = [(a, b) for a, b in zip(human, s) if a != "-" and b != "-"]
    diff = sum(a != b for a, b in pairs)
    name = re.sub(r"\s*\(.*", "", organism)
    common = re.findall(r"\(([^)]*)\)", organism)
    species.append({"species": name, "common_name": common[0] if common else "", "group": group,
                    "accession": acc, "core_great_ape": "yes" if acc in CORE else "no",
                    "differences_from_human": diff, "identity_to_human_pct": round(100 * (1 - diff / len(pairs)), 1),
                    "aligned_sequence": s})

positions = []
pos_h = 0
for i in range(len(human)):
    col = [s[i] for _, s in recs]
    if human[i] != "-": pos_h += 1
    c = collections.Counter(x for x in col if x != "-"); n = sum(c.values())
    ent = -sum(v / n * math.log2(v / n) for v in c.values())
    positions.append({"column": i + 1, "human_position": pos_h, "human_residue": human[i],
                      "entropy_bits": round(ent + 0.0, 3), "distinct_residues": len(c),
                      "has_gap": "yes" if "-" in col else "no",
                      "invariant": "yes" if len(c) == 1 and "-" not in col else "no",
                      "heme_binding": HEME.get(pos_h, "") if human[i] != "-" else "",
                      "residues_seen": "".join(sorted(c))})

ml = []
for r in csv.DictReader(open(f"{D}/results/table_ml_results.csv")):
    ba, bsd = [float(x) for x in r["balanced_accuracy"].split("±")]
    f1, fsd = [float(x) for x in r["macro_F1"].split("±")]
    ml.append({"model": r["model"], "balanced_accuracy": ba, "balanced_accuracy_sd": bsd, "macro_f1": f1, "macro_f1_sd": fsd})

code = open(__file__).read()
meta = lambda inp: [{"label": "make_data.py", "value": code, "type": "code", "lang": "python"}, {"label": "Input", "value": inp}]
json.dump({"rows": species, "meta": meta("data/cytc_aligned.fasta (MAFFT alignment of the 76 species kept after QC)")}, open("species.json", "w"))
json.dump({"rows": positions, "meta": meta("data/cytc_aligned.fasta")}, open("positions.json", "w"))
json.dump({"rows": ml, "meta": meta("results/table_ml_results.csv")}, open("ml.json", "w"))
print(len(species), len(positions), sum(p["invariant"] == "yes" for p in positions), [p for p in positions if p["heme_binding"]])
