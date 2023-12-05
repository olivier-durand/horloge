import time

heure_actuelle = (16, 30, 0)

def afficher_heure(heure_actuelle, nouvelle_heure):
    nouvelle_seconde = (heure_actuelle[2] + nouvelle_heure[2]) % 60
    nouvelle_minute = heure_actuelle[1] + nouvelle_heure[1] + (heure_actuelle[2] + nouvelle_heure[2]) // 60
    nouvelle_heure_result = (heure_actuelle[0] + nouvelle_heure[0] + nouvelle_minute // 60) % 24
    nouvelle_minute = nouvelle_minute % 60
    nouvelle_seconde = nouvelle_seconde % 60
    
    print(f"Nouvelle heure : {nouvelle_heure_result:02d}:{nouvelle_minute:02d}:{nouvelle_seconde:02d}")
    
    return (nouvelle_heure_result, nouvelle_minute, nouvelle_seconde)

def regler_alarme(nouvelle_heure_alarme):
    print("Alarme réglée à :", "{:02d}:{:02d}:{:02d}".format(*nouvelle_heure_alarme))
    return nouvelle_heure_alarme

def verifier_alarme(heure_actuelle, heure_alarme):
    if heure_actuelle == heure_alarme:
        print("Réveil ! L'heure de l'alarme est atteinte.")
        heure_alarme = regler_alarme((16, 31, 0))

heure_alarme = regler_alarme((16, 31, 0))
arreter_heure = False

while not arreter_heure:
    heure_actuelle = afficher_heure(heure_actuelle, (0, 0, 1))
    verifier_alarme(heure_actuelle, heure_alarme)
    time.sleep(1)
    

