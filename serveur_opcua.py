from opcua import Server
from datetime import datetime

# Création du serveur
server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

# Configuration du serveur
server.set_server_name("Serveur OPC UA - Broker")

# Ajout d'un espace de noms
uri = "http://waterlevels.org"
idx = server.register_namespace(uri)

# Création d'objets pour les niveaux d'eau
water_levels = server.nodes.objects.add_object(idx, "WaterLevels")
level_sensor_1 = water_levels.add_variable(idx, "Sensor1", 0.0)
level_sensor_2 = water_levels.add_variable(idx, "Sensor2", 0.0)

# Permettre l'écriture des valeurs
level_sensor_1.set_writable()
level_sensor_2.set_writable()

# Démarrer le serveur
server.start()
print("Serveur OPC UA démarré")

try:
    while True:
        # Mettre à jour une timestamp (optionnelle, pour surveiller le temps)
        now = datetime.now()
        #print(f"Serveur actif - {now}")
finally:
    server.stop()
    print("Serveur OPC UA arrêté")
