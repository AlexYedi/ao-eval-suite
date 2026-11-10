import json,glob,sys,os,statistics
d=sys.argv[1]; fs=sorted(glob.glob(os.path.join(d,"s[0-9]*.json")))
rs=[json.load(open(f)) for f in fs]
ok=[r for r in rs if r["ok"] and r["text"].strip()]
wall=int(open(f"{d}/t1").read())-int(open(f"{d}/t0").read())
secs=[r["secs"] for r in ok]
out={"n":len(rs),"retried":sum(1 for r in rs if r.get("attempts",1)>1),"ok":len(ok),"failed":len(rs)-len(ok),"wall_secs":wall,
 "samples_per_hour":round(len(ok)/wall*3600,1) if wall else None,
 "median_secs":statistics.median(secs) if secs else None,
 "p95_secs":sorted(secs)[max(0,int(len(secs)*.95)-1)] if secs else None,
 "input_tokens_median":statistics.median([ (r["usage"] or {}).get("input_tokens",0)+(r["usage"] or {}).get("cache_read_input_tokens",0)+(r["usage"] or {}).get("cache_creation_input_tokens",0) for r in ok]) if ok else None,
 "kill_gate_60_per_hour":"PASS" if wall and len(ok)/wall*3600>=60 else "FAIL"}
json.dump(out,open(f"{d}/summary.json","w"),indent=1); print(json.dumps(out,indent=1))
