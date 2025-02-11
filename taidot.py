import apuhaut
import tulostus

def hae_taidot(cur):
    #Vaihtoehto 10
    
    id = input("Anna henkilön id ")
    print()

    if not apuhaut.loytyyko(cur, 1, id, 0):
    #if not loytyyko_henkilo(id):
        print("Henkilöä id:llä "+id+" ei löydy. Saat henkilön id:n hauilla 1, 2 tai 3.")

    else:
        nimi = apuhaut.hae_nimi(cur, id)
        
        if not apuhaut.loytyyko(cur, 3, id, 0):
        #if loytyyko_taidot(id):
            print("Henkilölle "+nimi+" ei ole vielä tallennettu taitoja.")
            print()

        else:
            print("Haetaan henkilön "+nimi+" taidot")
            print()
            taidot = cur.execute("SELECT taito FROM taidot WHERE id = ?", (id,)).fetchall()
            for taito in taidot:
                tulostus.tulosta_taito(cur, taito)

def lisaa_taito(cur):
    #Vaihtoehto 11
    #print("Toteutetaan taidon lisääminen henkilölle")
    
    id = input("Anna henkilön id. ")
    print()

    if not apuhaut.loytyyko(cur, 1, id, 0):
    #if not loytyyko_henkilo(id):
        print("Henkilöä id:llä "+id+" ei löydy. Saat henkilön id:n hauilla 1, 2 tai 3.")
        print()
        
    else:
        nimi = apuhaut.hae_nimi(cur, id)
        print("Lisätään henkilölle "+nimi+" taitoja")
        print()
        lisays = True
        while lisays:
            taito = input("Lisää uusi taito. Lopeta jättämällä syöte tyhjäksi ")
            print()
            if taito == "":
                print("Lopetetaan lisäys")
                lisays = False
            else:
                taitolisays = cur.execute("INSERT INTO taidot(id, taito) VALUES(?,?)", (id,taito))
                print("Taito lisätty")
                print()

def paivita_taito(cur):
    #Vaihtoehto 12
    #print("Toteutetaan henkilön yksittäisen taidon muokkaaminen")
    id = input("Anna henkilön id ")
    print()

    if not apuhaut.loytyyko(cur, 1, id, 0):
    #if not loytyyko_henkilo(id):
        print("Henkilöä id:llä "+id+" ei löydy. Saat henkilön id:n hauilla 1, 2 tai 3.")
        print()
        
    else:
        if not apuhaut.loytyyko(cur, 3, id, 0):
        #if not loytyyko_taidot(id):
            print("Henkilölle ei ole vielä lisätty taitoja")
            print()
            
        else:
            nimi = apuhaut.hae_nimi(cur,id)
            print("Muokataan henkilön "+nimi+" taitoja")
            print()
            print("Toteutetaan taitojen muokkaus")
            print()
            muokkaus = True
            while muokkaus:
                m = input("Anna muokattava taito. Jätä taito tyhjäksi, jos tahdot lopettaa muokkauksen. ")
                if m == "":
                    print("Lopetetaan taidon muokkaus.")
                    print()
                    muokkaus = False
                else:
                #lisätään tarkastus, onko taitoa
                    u = input("Anna uusi taito: ")
                    taitomuokkaus = cur.execute("UPDATE taidot SET taito = ? WHERE taito = ? AND id = ?", (u,m,id))
                    print("Taito on muutettu.")
                    print()

def taito_henkilot(cur):
    #Vaihtoehto 13
    #Haetaan henkilöt taidon mukaan
    taito = input("Minkä taidon mukaan etsit osaajia? ")
    print()
    print("Tehdään kysely taidolla "+taito)
    print()

    if not apuhaut.loytyyko(cur, 4, 0, taito):
    #if not loytyyko_osaajia(taito):
        print("Tällä taidolla ei vielä löydy osaajia")
        print()
    else:
        print("Etsitään taidon "+taito+" osaajat")
        print()
        osaajakys = cur.execute("SELECT etunimi, sukunimi FROM henkilot, taidot WHERE taito = ? AND henkilot.id = taidot.id", (taito,))
        for o in osaajakys:
            tulostus.tulosta_osaaja(cur, o)

def kaikki_taidot(cur):
    #Vaihtoehto 14
    #Haetaan kaikki tallennetut taidot
    if not apuhaut.loytyyko(cur, 5, 0, 0):
    #if not loytyyko_taitoja:
        print("Taitoja ei ole vielä tallennettu")
        print()
    else:
        print("Etsitään kaikki tallennetut taidot")
        print()
        taitokys = cur.execute("SELECT DISTINCT taito FROM taidot ORDER BY taito")
        for taito in taitokys:
            print(taito)
