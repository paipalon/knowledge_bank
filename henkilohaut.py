import tulostus

def hae(cur):
    #Vaihtoehto 1
    

    henkilot = cur.execute("SELECT * FROM henkilot ORDER BY sukunimi").fetchall()
    
    maarakys = cur.execute("SELECT COUNT(*) FROM henkilot")
    
    maaratulos = cur.fetchone()
    maara = (maaratulos[0])
    print("Henkilöitä: "+str(maara))
    print()
    
    if(maara == 0):
        print("Henkilöitä ei löydy vielä")
        
    else:
        for h in henkilot:
            tulostus.tulosta_henkilo(cur, h)

def hae_en(cur):
    #Vaihtoehto 2
    en = input("Anna etunimi ")
    print()
    
    maarakys = cur.execute("SELECT COUNT(*) FROM henkilot WHERE etunimi = ?", (en,))
    maaratulos = cur.fetchone()
    maara = (maaratulos[0])

    if(maara == 0):
        print("Henkilöitä etunimellä "+en+" ei löydy vielä")
    else:
        henkilot = cur.execute("SELECT * FROM henkilot WHERE etunimi = ?", (en,)).fetchall()
        
        print("Henkilöitä etunimellä "+en+": "+str(maara))
        print()
    
        for h in henkilot:
            tulostus.tulosta_henkilo(cur, h)

def hae_sn(cur):
    #Vaihtoehto 3
    sn = input("Anna sukunimi ")
    print()

    maarakys = cur.execute("SELECT COUNT(*) FROM henkilot WHERE sukunimi = ?", (sn,))
    maaratulos = cur.fetchone()
    maara = (maaratulos[0])

    if(maara == 0):
        print("Henkilöitä aukunimellä "+sn+" ei löydy vielä")
    else:
        henkilot = cur.execute("SELECT * FROM henkilot WHERE sukunimi = ?", (sn,)).fetchall()

        print("Henkilöitä sukunimellä "+sn+": "+str(maara))
        print()
    
        for h in henkilot:
            tulostus.tulosta_henkilo(cur, h)
