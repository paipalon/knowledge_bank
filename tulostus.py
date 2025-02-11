def tulosta_henkilo(cur, h):
    id = str(h[0])
    en = h[1]
    sn = h[2]
    email = h[3]
    li_sivu = h[4]
    print(id+" "+en+" "+sn+" "+email+" "+li_sivu)
    print()

def tulosta_top3(cur, top):
    top_1 = str(top[0])
    top_2 = top[1]
    top_3 = top[2]
    lisatiedot = top[3]
    #lisatiedot = top[4]
    print(top_1+" "+top_2+" "+top_3)
    print()
    print(lisatiedot)
    print()

def tulosta_taito(cur, taito):
    t = taito[0]
    print(t)

def tulosta_osaaja(cur, o):
    en = o[0]
    sn = o[1]
    print(en+" "+sn)
    print()
