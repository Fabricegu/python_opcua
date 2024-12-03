from opcua import Client
import time
import random

# Connexion au serveur
url = "opc.tcp://localhost:4840/freeopcua/server/"
client = Client(url)

try:
    client.connect()
    print("Éditeur connecté au serveur OPC UA")

    # Récupérer les nœuds des capteurs
    sensor_1 = client.get_node("ns=2;i=2")  # Adapter l'ID selon le serveur
    sensor_2 = client.get_node("ns=2;i=3")

    while True:
        # Simuler les niveaux d'eau aléatoires
        level_1 = random.uniform(0, 100)
        level_2 = random.uniform(0, 100)

        # Mettre à jour les valeurs sur le serveur
        sensor_1.set_value(level_1)
        sensor_2.set_value(level_2)

        print(f"Capteur 1 : {level_1}, Capteur 2 : {level_2}")
        time.sleep(5)  # Met à jour toutes les 2 secondes

finally:
    client.disconnect()
    print("Éditeur déconnecté")
