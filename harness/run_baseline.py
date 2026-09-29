#!/usr/bin/env python3
"""GxP-CiteAudit baseline runner STUB. Bring your own model/key.
Reads gold questions, calls YOUR agent, writes predictions/preds.jsonl in the scored schema.
This stub only shows the contract; it does not ship a model or a key."""
import json, argparse, pathlib
def your_agent(question, doc_id):
    # TODO: plug your agent here. Must return:
    #   {"answer": str, "confidence": float, "abstain": bool, "citations": [str], "denied": bool}
    raise NotImplementedError("Plug your agent into your_agent().")
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--gold",required=True); ap.add_argument("--out",default="predictions/preds.jsonl")
    a=ap.parse_args(); out=pathlib.Path(a.out); out.parent.mkdir(exist_ok=True)
    with open(out,"w") as f:
        for l in open(a.gold):
            if not l.strip(): continue
            g=json.loads(l); r=your_agent(g["question"], g.get("doc_id",""))
            f.write(json.dumps({"id":g["id"],**r})+"\n")
    print("wrote",out)
if __name__=="__main__": main()
