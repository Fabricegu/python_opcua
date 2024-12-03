from opcua import Client
from opcua import ua

# Création d'un gestionnaire (handler) avec la méthode datachange_notification
class SubHandler:
    def datachange_notification(self, node, val, data):
        print(f"Nœud {node} mis à jour : Nouvelle valeur = {val}")

# Connexion au serveur
url = "opc.tcp://localhost:4840/freeopcua/server/"
client = Client(url)

try:
    client.connect()
    print("Abonné connecté au serveur OPC UA")

    # Récupérer les nœuds des capteurs
    sensor_1 = client.get_node("ns=2;i=2")  # Adapter l'ID selon le serveur
    sensor_2 = client.get_node("ns=2;i=3")

    # S'abonner aux nœuds avec un gestionnaire
    handler = SubHandler()  # Utilisation de l'objet avec la méthode correcte
    subscription = client.create_subscription(500, handler)
    subscription.subscribe_data_change(sensor_1)
    subscription.subscribe_data_change(sensor_2)

    # Garder l'application en cours d'exécution
    print("Abonné en cours d'exécution...")
    while True:
        pass

finally:
    client.disconnect()
    print("Abonné déconnecté")
