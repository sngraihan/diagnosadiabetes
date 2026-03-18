import math

RULEBASE = [
    {"id":"L1","disease":"Diabetes Tipe 2","antecedents":["GDP:high"], "cf_each":[0.55], "note":"GDP >=126 -> indikasi T2 (CF moderat)"},
    {"id":"L2","disease":"Diabetes Tipe 2","antecedents":["GDS:high","E01","E02"], "cf_each":[0.75,0.85,0.80], "note":"GDS tinggi + triad -> dukung T2 (CF dikurangi)"},
    {"id":"T1_SUPER","disease":"Diabetes Tipe 1","antecedents":["GDS:high","E03"], "cf_each":[0.98,0.95], "note":"Prioritas tinggi untuk T1: GDS tinggi + polifagia"},
    {"id":"T1A","disease":"Diabetes Tipe 1","antecedents":["GDS:high","E03","E04"], "cf_each":[0.95,0.80,0.50], "note":"GDS tinggi + polifagia + lemas -> T1 kuat"},
    {"id":"T1B","disease":"Diabetes Tipe 1","antecedents":["GDS:high","GDP:low"], "cf_each":[0.90,0.70], "note":"GDS tinggi tapi GDP low -> ciri T1"},
    {"id":"P0","disease":"Prediabetes","antecedents":["GDP:medium","GDS:medium"], "cf_each":[0.75,0.75], "note":"Kedua medium -> pra-diabetes kuat"},
    {"id":"P1","disease":"Prediabetes","antecedents":["GDP:medium","E01"], "cf_each":[0.55,0.35], "note":"GDP medium + poliuria -> risiko"},
    {"id":"P2","disease":"Prediabetes","antecedents":["GDS:medium"], "cf_each":[0.70], "note":"GDS medium saja -> cukup dukung pra-diabetes"},
    {"id":"P3","disease":"Prediabetes","antecedents":["GDS:medium","count_gejala_lemah"], "cf_each":[0.75,0.75], "note":"GDS medium + gejala sedikit -> pra-diabetes"},
    {"id":"S1","disease":"Diabetes Tipe 2","antecedents":["E01","E02","E03"], "cf_each":[0.60,0.55,0.50], "note":"Triad klasik, dukung T2 tapi moderat"},
    {"id":"S2","disease":"Diabetes Tipe 1","antecedents":["E01","E03","E04"], "cf_each":[0.70,0.60,0.25], "note":"Ciri T1 (E04 tidak terlalu spesifik)"},
    {"id":"S3","disease":"Diabetes Tipe 2","antecedents":["E01","E05","E07"], "cf_each":[0.40,0.30,0.35], "note":"Komplikasi/neuropati, dukung T2 tapi dilemahkan"},
    {"id":"C1","disease":"Diabetes Tipe 2","antecedents":["GDP:high","E07"], "cf_each":[0.90,0.70], "note":"GDP tinggi + luka -> dukungan kuat T2"},
    {"id":"C2","disease":"Diabetes Tipe 2","antecedents":["GDP:high","E05"], "cf_each":[0.90,0.65], "note":"GDP tinggi + kesemutan -> dukung T2"},
    {"id":"G1","disease":"Diabetes Gestasional","antecedents":["PREG:ya","GDS:high"], "cf_each":[0.95,0.85], "note":"Ibu hamil + GDS high -> gestasional"},
    {"id":"G2","disease":"Diabetes Gestasional","antecedents":["PREG:ya","GDS:medium","E02"], "cf_each":[0.90,0.60,0.50], "note":"Ibu hamil + GDS medium + polidipsia"},
    {"id":"N1","disease":"Tidak Diabetes","antecedents":["GDP:low","GDS:low"], "cf_each":[0.95,0.95], "note":"Gula normal kedua -> kuat bukan diabetes"},
    {"id":"N2","disease":"Tidak Diabetes","antecedents":["GDP:low","count_gejala_lemah"], "cf_each":[0.85,0.80], "note":"GDP low + sedikit gejala -> bukan diabetes"},
    {"id":"N3","disease":"Tidak Diabetes","antecedents":["GDP:medium","count_gejala_lemah"], "cf_each":[0.60,0.60], "note":"GDP medium namun gejala sedikit -> cenderung tidak"},
    {"id":"N4","disease":"Tidak Diabetes","antecedents":["GDP:low","GDS:medium","count_gejala_lemah"], "cf_each":[0.75,0.55,0.55], "note":"GDP low + GDS medium + gejala sedikit -> prioritas bukan diabetes"},
]

GEJALA = {
    "E01":"Poliuria",
    "E02":"Polidipsia",
    "E03":"Polifagia",
    "E04":"Lemas",
    "E05":"Kesemutan",
    "E06":"Pandangan kabur",
    "E07":"Luka sulit sembuh"
}

PENYAKIT = ["Diabetes Tipe 1","Diabetes Tipe 2","Diabetes Gestasional","Prediabetes","Tidak Diabetes"]

def combine_two_cfs(cf1, cf2):
    return cf1 + cf2 * (1 - cf1)

def combine_cfs_list(cfs):
    if not cfs:
        return 0.0
    r = cfs[0]
    for c in cfs[1:]:
        r = combine_two_cfs(r, c)
    return r

def evidence_belief(val):
    if isinstance(val, (int,float)):
        v = float(val)
        return max(0.0, min(1.0, v))
    if isinstance(val, str):
        s = val.strip().lower()
        if s in ["ya", "y", "true", "1"]:
            return 1.0
        return 0.0
    return 0.0

def compute_rule_cf_partial(rule, evidence_map, user_certainty_map=None):
    user_certainty_map = user_certainty_map or {}
    ants = rule.get("antecedents",[])
    cf_each = rule.get("cf_each",[])
    cf_list = []
    for a, cf_pk in zip(ants, cf_each):
        if ":" in a:
            var, val = a.split(":",1)
            ev = evidence_map.get(var, "")
            if isinstance(ev, str) and ev.lower() == val.lower():
                user_belief = float(user_certainty_map.get(var,1.0))
                cf_list.append(user_belief * float(cf_pk))
            else:
                continue
        elif a == "count_gejala_lemah":
            v = evidence_map.get("count_gejala_lemah","tidak")
            if str(v).lower() in ["ya","y","true","1"]:
                user_belief = float(user_certainty_map.get(a,1.0))
                cf_list.append(user_belief * float(cf_pk))
            else:
                continue
        else:
            ev = evidence_map.get(a, 0.0)
            belief = evidence_belief(ev)
            user_belief = float(user_certainty_map.get(a, belief))
            final_belief = belief * user_belief
            if final_belief > 0:
                cf_list.append(final_belief * float(cf_pk))
    if not cf_list:
        return 0.0
    return combine_cfs_list(cf_list)

def infer_with_certainty(evidence_map, user_certainty_map=None, fallback_k=3, min_belief=0.2):
    user_certainty_map = user_certainty_map or {}
    disease_support = {}
    for r in RULEBASE:
        rc = compute_rule_cf_partial(r, evidence_map, user_certainty_map)
        if rc > 0:
            disease_support.setdefault(r["disease"], []).append((r["id"], rc))
            
    final = {}
    for disease, lst in disease_support.items():
        if lst:
            final[disease] = combine_cfs_list([x[1] for x in lst])

    if final:
        return final

    sym_beliefs = []
    for sym in ["E01","E02","E03","E04","E05","E06","E07"]:
        b = float(user_certainty_map.get(sym, evidence_belief(evidence_map.get(sym,0.0))))
        if b >= min_belief:
            sym_beliefs.append((sym, b))
            
    if not sym_beliefs:
        return final

    sym_beliefs.sort(key=lambda x: x[1], reverse=True)
    top_syms = sym_beliefs[:fallback_k]

    disease_contribs = {}
    for sym, bel in top_syms:
        for r in RULEBASE:
            for idx,a in enumerate(r.get("antecedents",[])):
                if a == sym:
                    pk = float(r.get("cf_each",[])[idx])
                    d = r["disease"]
                    local = bel * pk
                    disease_contribs.setdefault(d, []).append(local)

    if not disease_contribs:
        return final

    for d, arr in disease_contribs.items():
        if arr:
            final[d] = combine_cfs_list(arr)

    return final

def convert_glucose_to_cat(v, kind="GDP"):
    try:
        x = float(v)
    except:
        return ""
    if kind.upper()=="GDP":
        if x >= 126: return "high"
        if x >= 100: return "medium"
        return "low"
    else:
        if x >= 200: return "high"
        if x >= 140: return "medium"
        return "low"

def run_inference(gdp_val, gds_val, preg_val, gejala_vals):
    """
    gdp_val: str or float
    gds_val: str or float
    preg_val: boolean or "ya"/"tidak"
    gejala_vals: dict of symptom codes (E01-E07) to floats 0-1
    """
    gdp_cat = convert_glucose_to_cat(gdp_val, "GDP") if str(gdp_val).strip() else ""
    gds_cat = convert_glucose_to_cat(gds_val, "GDS") if str(gds_val).strip() else ""
    
    is_preg = "ya" if str(preg_val).lower() in ["ya", "y", "true", "1", "k"] else "tidak"
    if str(preg_val).strip() == "True" or preg_val is True: is_preg = "ya"
    
    evidence = {"GDP": gdp_cat, "GDS": gds_cat, "PREG": is_preg}
    user_cert = {}
    
    for code, val in gejala_vals.items():
        try:
            val_float = float(val)
        except:
            val_float = 0.0
        evidence[code] = val_float
        user_cert[code] = val_float
        
    count = sum(1 for v in user_cert.values() if v >= 0.5)
    evidence["count_gejala"] = count
    evidence["count_gejala_lemah"] = "ya" if count <= 1 else "tidak"
    
    res = infer_with_certainty(evidence, user_cert)
    
    if not res:
        disease_scores = {d: 0.0 for d in PENYAKIT}
    else:
        disease_scores = {d: float(res.get(d, 0.0)) for d in PENYAKIT}
        
    return disease_scores

if __name__ == "__main__":
    # Test execution
    gejala = {
        "E01": 0.5, "E02": 0.6, "E03": 0.1, 
        "E04": 0.0, "E05": 0.0, "E06": 0.0, "E07": 0.0
    }
    res = run_inference(110, 105, False, gejala)
    print("Test Diagnosis Scores:")
    for d, s in sorted(res.items(), key=lambda x: x[1], reverse=True):
         print(f"{d}: {s:.4f} ({s*100:.1f}%)")
