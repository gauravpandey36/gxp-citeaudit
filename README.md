# GxP-CiteAudit

**An open, synthetic benchmark for the faithfulness of AI agents on GxP quality records.**
Companion to the QU-Gate architecture. Version 0.2 · MIT · 2026-09-28.

> ⚠️ **Synthetic only. NOT validated for production GxP use.** All documents and answers are from **GeneriCorp Therapeutics, a fictional pharmaceutical company** built for research. No real product, site, batch, patient, or employer data is present. This benchmark measures agent behavior; it is not a compliance certification.

---

## Why
LLM agents draft GxP records fluently, but a fluent record can still cite a regulation that does not exist, attach the wrong requirement to a real clause, get a number wrong, or answer a judgment as if it were a fact. GxP-CiteAudit scores an agent along **typed faithfulness axes** rather than one "hallucination %", so the failure that matters to an inspector (a fabricated citation, a silent wrong answer, a leaked document) is measured directly.

## What it measures — six axes
| Axis | Question it answers | Pass = |
|---|---|---|
| `citation_validity` | Did the agent cite a real regulation/section, or fabricate one? | no invalid/fabricated citation |
| `clause_fidelity` | Right citation, right proposition? | citation supports the stated requirement |
| `numeric_faithfulness` | Are batch/yield/stability/limit numbers exact? | value matches the record |
| `silent_error` | Was a judgment/decision answered as fact with no escalation? | wrong answers are abstained/flagged, not asserted |
| `false_premise` | Does the agent abstain on outdated-revision / wrong-product / false-premise traps? | ABSTAIN |
| `role_leak` | Does an unauthorized agent get denied? | DENY |

## Conditions (how an agent is run)
- **C0** raw document + naive retrieval + LLM (baseline)
- **C2** authored document + structure-addressed retrieval + LLM
- **C3** authored + deterministic lookup / typed decision gate / LLM-on-judgment-only (QU-Gate)
- **C4** C3 + role/identity gate
- **C3G / C4G** add the deterministic revision/product/premise input gates

## Layout
```
gxp-citeaudit/
  schema/item.schema.json      # gold item schema
  gold/example_items.jsonl     # small synthetic example set (expand in v1)
  harness/score.py             # scorer: predictions + gold -> per-axis metrics
  harness/run_baseline.py      # stub showing how to plug a model (bring your own key)
  leaderboard.md               # results table (append your run)
```

## Quick start
```bash
# 1. produce predictions/preds.jsonl : one {"id","answer","confidence","abstain","citations","denied"} per gold item
# 2. score
python harness/score.py --gold gold/example_items.jsonl --pred predictions/preds.jsonl
```
`score.py` prints per-axis pass rates and a silent-error count. No network or keys required to score.

## Metrics reported
Per axis: n, pass rate. Headline: **silent-error rate**, **invalid-citation rate**, **role-leak rate**, **false-premise-abstention rate**. A model is only comparable at a fixed, reported confidence threshold τ (default 0.80).

## How to contribute a result
Run your agent to produce `preds.jsonl`, score it, and open a PR adding a row to `leaderboard.md` with: system, model + date, condition, τ, and the four headline numbers. Synthetic data only; no confidential records in issues or PRs.

## Citation
See `CITATION.cff`. Cite the QU-Gate paper and this benchmark. Please do **not** claim regulator acceptance or production validation from a GxP-CiteAudit score.

*All examples reference GeneriCorp Therapeutics, a fictional company built for research and educational purposes. No proprietary or employer information is used or implied.*
