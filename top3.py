import apuhaut
import tulostus

def hae_top3(cur):
    #Vaihtoehto 7
    id = input("Anna henkilön id ")
    print()
    
    if not apuhaut.loytyyko(cur, 1, id, 0):
    #if not loytyyko_henkilo(id):
        print("Henkilöä id:llä "+id+" ei löydy. Saat henkilön id:n hauilla 1, 2 tai 3.")
        print()
        
    else:
        if apuhaut.loytyyko (cur, 2, id, 0):
        #if loytyyko_top3(id):
            nimi = apuhaut.hae_nimi(cur, id)
            print("Haetaan henkilön "+nimi+" top3 taidot")
            print()
            top3 = cur.execute("SELECT top_1, top_2, top_3, lisatiedot FROM top3 WHERE id = ?", (id,)).fetchall()

            for top in top3:
                tulostus.tulosta_top3(cur, top)

def lisaa_top3(cur):
    #Vaihtoehto 8
    id = input("Anna henkilön id ")
    print()
    
    if not apuhaut.loytyyko(cur, 1, id, 0):
    #if not loytyyko_henkilo(id):
        print("Henkilöä id:llä "+id+" ei löydy. Saat henkilön id:n hauilla 1, 2 tai 3.")
        print()
        
    else:
        nimi = apuhaut.hae_nimi(cur, id)
        if not apuhaut.loytyyko(cur, 2, id, 0):
        #if not loytyyko_top3(id): 
            print("Lisätään henkilön "+nimi+" top 3 taidot")

            oikein = False
            while not oikein:
                t1 = input("Anna henkilön ensimmäinen taito")
                print()
                if len(t1) > 0:
                    oikein = True
                else:
                    print("Pakollinen tieto")
                    print()
            

            oikein = False
            while not oikein:
                t2 = input("Anna henkilön toinen taito ")
                print()
                if len(t2) > 0:
                   oikein = True
                else:
                    print("Pakollinen tieto")
                    print()        

            oikein = False
            while not oikein:        
                t3 = input("Anna henkilön kolmas taito ")
                print()
                if len(t3) > 0:
                   oikein = True
                else:
                    print("Pakollinen tieto")
                    print()   

                
                lt = input("Anna henkilön lisätiedot ")
                print()

                
            top3_lisays = cur.execute("INSERT INTO top3(id, top_1,top_2, top_3, lisatiedot) VALUES(?,?,?,?,?)", (id,t1,t2,t3,lt))
            print("Taidot lisätty")
            
        else:
            print("Henkilöllä "+nimi+" on jo top 3 taidot. Voit päivittää top 3 taidot valinnalla 9.")

def paivita_top3(cur):
    #Vaihtoehto 9
    id = input("Anna henkilön id ")
    print()

    if not apuhaut.loytyyko(cur, 1, id, 0):
    #if not loytyyko_henkilo(id):
        print("Henkilöä id:llä "+id+" ei löydy. Saat henkilön id:n hauilla 1, 2 tai 3.")

    else:
        nimi = apuhaut.hae_nimi(cur, id)
        if not apuhaut.loytyyko(cur, 2, id, 0):
        #if not loytyyko_top3(id):
            print("Henkilöltä "+nimi+" ei löydy vielä top 3 taitoja. Lisää taidot vaihtoehdolla 8")

        else:
            print("Päivitetään henkilön "+nimi+" top3 taitoja")
            print()
            
            muokkaus = True
            while muokkaus:
                print("Valitse päivitettävä kenttä. Jätä kenttä tyhjäksi, jos tahdot lopettaa.")
                print()
                valinta = input("Taito 1 E Taito 2 T Taito 3 K Lisätiedot L ")
                print()
            
                if valinta in ["e", "E"]:
                    oikein = False
                    while not oikein:
                        t1 = input("Anna uusi ensimmäinen top3 taito ")
                        print()
                        if len(t1) > 0:
                           oikein = True
                        else:
                            print("Pakollinen tieto")
                            print() 
                    print("Päivitetään top3 aito 1")
                    print()
                    paivitys = cur.execute("UPDATE top3 SET top_1 = ? WHERE id = ?", (t1,id))
                    
                elif valinta in ["t", "T"]:
                    oikein = False
                    while not oikein:
                        t2 = input("Anna uusi toinen top3 taito ")
                        print()
                        if len(t2) > 0:
                           oikein = True
                        else:
                            print("Pakollinen tieto")
                            print() 
                    print("Päivitetään top3 taito 2")
                    paivitys = cur.execute("UPDATE top3 SET top_2 = ? WHERE id = ?", (t2,id))
                    
                elif valinta in ["k", "K"]:
                    oikein = False
                    while not oikein:
                        t3 = input("Anna uusi kolmas top3 taito ")
                        print()
                        if len(t3) > 0:
                           oikein = True
                        else:
                            print("Pakollinen tieto")
                            print() 
                    print("Päivitetään top3 taito 3")
                    paivitys = cur.execute("UPDATE top3 SET top_3 = ? WHERE id = ?", (t3,id))
                    
                elif valinta in ["l", "L"]:
                    lt = input("Anna uudet lisätaidot ")
                    print()
                    print("Päivitetään lisätiedot")
                    paivitys = cur.execute("UPDATE top3 SET lisatiedot = ? WHERE id = ?", (lt,id))
                    
                else:
                    print("Lopetetaan muokkaus.")
                    print()
                    muokkaus = False


