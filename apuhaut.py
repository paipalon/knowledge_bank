#import osaamistiedot

def hae_nimi(cur,id):
    #import osaamistiedot
    
    en_kysely = cur.execute("SELECT etunimi FROM henkilot WHERE id = ?", (id, ))
    en_tulos = cur.fetchone()
    en = (en_tulos[0])
    
    sn_kysely = cur.execute("SELECT sukunimi FROM henkilot WHERE id = ?", (id, ))
    sn_tulos = cur.fetchone()
    sn = (sn_tulos[0])
    
    nimi = (en+" "+sn)
    return nimi

def loytyyko(cur, lause, id, taito):
    loytyy = True
    
    if lause == 1:
        #löytyykö henkilöä id:llä
        #poista, paivita, hae_top3, lisaa_top3, paivita_top3, hae_taidot, lisaa_taito, paivita_taito
        maarakys = cur.execute("SELECT COUNT(*) FROM henkilot WHERE id = ?", (id,))
    elif lause == 2:
        #löytyykö top3 tietuetta id:llä
        #hae_top3, lisaa_top3, paivita_top3
        maarakys = cur.execute("SELECT COUNT(*) FROM top3 WHERE id = ?", (id,))
    elif lause == 3:
        #löytyykö taitotietueita henkilön id:llä
        #hae_taidot, paivita_taito
        maarakys = cur.execute("SELECT COUNT(*) FROM taidot WHERE id = ?", (id,))
    elif lause == 4:
        #löytyyko taidolle osaajia
        #taito_henkilot
    
        maarakys = cur.execute("SELECT COUNT(*) FROM taidot WHERE taito = ?", (taito,))
    else:
        #löytyykö taitotietueita
        #kaikki_taidot
        maarakys = cur.execute("SELECT COUNT(*) FROM taidot")
    
    maaratulos = cur.fetchone()
    maara = (maaratulos[0])
    if maara == 0:
        loytyy = False
    return loytyy
