import random
import time

pv = 100
montres_vaincus = 0

print(f"Bienvenue, aventurier et aventurière ! 🏰 Tu commences avec {pv} PV. Il te faut vaincre 5 monstres.")
print("Le choix (q) te permet de quitter le jeu à tout moment.")


while pv > 0 and montres_vaincus < 5:
    print("\n--- Nouveau tour ---")
    print(f"PV : {pv} | Monstres vaincus : {montres_vaincus}")
    print("Tu avances dans la forêt sombre... 🌲")

    evenement = random.choice(["monstre", "monstre", "potion magique"])

    if evenement == "monstre":
        degats = random.randint(15, 25)
        fuite = random.randint(0, 5)
        print(f"😈 Un monstre surgit ! Il a une force équivalente à {degats} PV")
        action = input("Veux-tu le combattre (c) ou fuir (f) ? ")
        if action == "c":
            print(f"Tu combats vaillamment le monstre ! Tu ressors victorieux, mais perds {degats} PV.")
            pv -= degats
            montres_vaincus += 1
        elif action == "q":
            break
        else:
            print(f"Tu fuis et perds {fuite} PV en courant.")
            pv -= fuite

    elif evenement == "potion magique":
        gain = random.randint(-10, 15)
        action = input("🍷 Tu trouves une potion magique veux-tu la boire (o) ou non (n) ? ")
        if action == "o":
            print(f"Tu bois la potion et gagnes {gain} PV.")
        elif action == "q":
            break
        else:
            print("Tu choisis de ne pas boire la potion.")
            gain = 0
        pv += gain

    time.sleep(1)

if pv <= 0:
    print("\n☠️ Tu es mort dans l'aventure. Fin du jeu.")
elif montres_vaincus >= 5:
    print("\n🏆 Bravo ! Tu as vaincu 5 monstres et gagné l'aventure.")
else:
    print("Merci d'avoir joué ! À bientôt !")