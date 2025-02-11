import apuhaut

def lisaa(cur):
    #Vaihtoehto 4
    oikein = False
    while not oikein:
        en = input("Anna etunimi ")
        print()
        if len(en) > 0:
            oikein = True
        else:
            print("Etunimi on pakollinen")
            print()

    oikein = False
    while not oikein:
        sn = input("Anna sukunimi ")
        print()
        if len(sn) > 0:
            oikein = True
        else:
            print("Sukunimi on pakollinen")
            print()
            
    oikein = False
    #Sähköpostiosoitteen varsinainen tarkastus lisätään myöhemmin
    while not oikein:
        spo = input("Anna sähköpostiosoite ")
        print()
        if len(spo) > 0:
            oikein = True
        else:
            print("Sähköpostiosoite on pakollinen")
            print()
            
    li_s = input("Anna LinkedIn-sivun osoite ")
    print()
    
    print("Lisätään henkilö "+en+" "+sn)
    print()
    lisays = cur.execute("INSERT INTO henkilot(etunimi,sukunimi, sposti, li_sivu) VALUES(?,?,?,?)", (en,sn,spo,li_s))
    print()

def poista(cur):
    #Vaihtoehto 5
    id = input("Anna poistettavan henkilön id: ")
    print()
    if not apuhaut.loytyyko(cur, 1, id, 0):
    #if not loytyyko_henkilo(id):
        print("Henkilöä id:llä "+id+" ei löydy. Saat henkilön id:n hauilla 1, 2 tai 3.")
    else:
        print("Henkilö löytyy")
        nimi = apuhaut.hae_nimi(cur, id)
        vahvistus = input("Poistetaanko henkilö "+nimi+"? Kyllä k Ei e ")
        print()
        if (vahvistus in ["K","k"]):
            id = int(id)
            
            poisto = cur.execute("DELETE FROM henkilot WHERE id = ?", (id,))
            print("Henkilö poistettiin")
            print()

            poista_top3 = cur.execute("DELETE FROM top3 WHERE id = ?", (id,))
            print("Henkilön top 3 tiedot poistettiin")
            print()
            
            #Lisättävä poisto myös top3 taulusta

            poista_taidot = cur.execute("DELETE FROM taidot WHERE id = ?", (id,))
            print("Henkilön taidot poistettiin")
            print()
            
            #Lisättävä poisto myös taidot taulusta
        else:
            print("Poisto peruutetaan")

def paivita(cur):
    #Vaihtoehto 6
    id = input("Anna henkilön id ")
    print()
    
    #löytyykö henkilö
    if not apuhaut.loytyyko(cur, 1, id, 0):
    #if not loytyyko_henkilo(id):
        print("Henkilöä id:llä "+id+" ei löydy. Saat henkilön id:n hauilla 1, 2 tai 3.")
        
    else:
        nimi = apuhaut.hae_nimi(cur, id)
        print("Päivitetään henkilön "+nimi+" tietoja.")
        print()
        muokkaus = True
        
        while muokkaus:
            print("Valitse päivitettävä arvo. Kun haluat lopettaa, jätä syöte tyhjäksi.")
            print()
            valinta = input("Etunimi e Sukunimi s Sähköposti p LinkedIn-sivun osoite l ")
            print()
            if valinta in ["e", "E"]:
                en = input("Anna uusi etunimi ")
                print()
                print("Päivitetään etunimi")
                print()
                paivitys = cur.execute("UPDATE henkilot SET etunimi = ? WHERE id = ?", (en,id))
            elif valinta in ["s", "S"]:
                sn = input("Anna uusi sukunimi ")
                print()
                print("Päivitetään Sukunimi")
                print()
                paivitys = cur.execute("UPDATE henkilot SET sukunimi = ? WHERE id = ?", (sn,id))
            elif valinta in ["p", "P"]:
                sp = input("Anna uusi sähköpostiosoite ")
                print()
                print("Päivitetään sähköpostiosoite")
                print()
                paivitys = cur.execute("UPDATE henkilot SET sposti = ? WHERE id = ?", (sp,id))
            elif valinta in ["l", "L"]:
                li = input("Anna uusi LinkedIn-sivun osoite ")
                print()
                print("Päivitetään LinkedIn-sivun osoite")
                print()
                paivitys = cur.execute("UPDATE henkilot SET li_sivu = ? WHERE id = ?", (li,id))
            else:
                print("Lopetetaan muokkaus.")
                muokkaus = False


