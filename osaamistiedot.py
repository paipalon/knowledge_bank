import sqlite3

import henkilohaut
import henkilo_operaatiot
import top3
import taidot

db = sqlite3.connect('osaamiset.db')
db.isolation_level = None

def luo_taulut():
    cur = db.cursor()
    henkilot_luonti = cur.execute("CREATE TABLE IF NOT EXISTS henkilot (id INTEGER PRIMARY KEY AUTOINCREMENT, etunimi TEXT, sukunimi TEXT, sposti TEXT, li_sivu TEXT)")
    db.commit()
    top3_luonti = cur.execute("CREATE TABLE IF NOT EXISTS top3 (id INTEGER PRIMARY KEY, top_1 TEXT, top_2 TEXT, top_3 TEXT, lisatiedot TEXT)")
    db.commit()
    taidot_luonti = cur.execute("CREATE TABLE IF NOT EXISTS taidot (id INTEGER, taito TEXT)")
    db.commit()    

def toiminnot():
    print("HAE KAIKKI HENKILÖT 1   HAE ETUNIMELLA 2  HAE SUKUNIMELLÄ 3")
    print()
    print("LISÄÄ HENKILÖ 4   POISTA HENKILÖ 5   PÄIVITÄ HENKILÖTIETOJA 6")
    print()
    print("HAE TAIDOT TOP3 7   LISÄÄ TAIDOT TOP3 8   PÄIVITÄ TOP3 TAITOJA 9")
    print()
    print("HAE MUUT TAIDOT 10   LISÄÄ MUU TAITO 11   PÄIVITÄ MUITA TAITOJA 12")
    print()
    print("HAE TAIDON MUKAAN 13   HAE KAIKKI TAIDOT 14")
    print()
    print("LOPETA 15")
    print()
    print()
    
def vaihtoehdot():
    ve = int(input("Valitse toiminto "))
    print()
    return ve

def main():
    luo_taulut()
    jatko = True
    print("TERVETULOA OSAAMISTIETOPANKKIIN")
    print()
    print()
    cur = db.cursor()
    while jatko:
        toiminnot()
        toiminto = vaihtoehdot()
        if toiminto == 1:
            henkilohaut.hae(cur)
        elif toiminto == 2:
            henkilohaut.hae_en(cur)
        elif toiminto == 3:
            henkilohaut.hae_sn(cur)
        elif toiminto == 4:
            henkilo_operaatiot.lisaa(cur)
            db.commit()
        elif toiminto == 5:
            henkilo_operaatiot.poista(cur)
            db.commit()
        elif toiminto == 6:
            henkilo_operaatiot.paivita(cur)
            db.commit()
        elif toiminto == 7:
            top3.hae_top3(cur)
        elif toiminto == 8:
            top3.lisaa_top3(cur)
            db.commit()
        elif toiminto == 9:
            top3.paivita_top3(cur)
            db.commit()
        elif toiminto == 10:
            taidot.hae_taidot(cur)
        elif toiminto == 11:
            taidot.lisaa_taito(cur)
            db.commit()
        elif toiminto == 12:
            taidot.paivita_taito(cur)
            db.commit()
        elif toiminto == 13:
            taidot.taito_henkilot(cur)
        elif toiminto == 14:
            taidot.kaikki_taidot(cur)
        else:
            print("Lopetetaan. Hauskaa päivän jatkoa!")
            jatko = False
        print()
        print()

main()
