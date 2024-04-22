import time
from geopy.geocoders import Nominatim


class SingletonSvc:
    _instance = None
    _derniere_requete = time.perf_counter() - 1.0

    def __init__(self):
        raise RuntimeError('Utiliser instance() à la place')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print("Création d'une nouvelle instance")
            cls._instance = cls.__new__(cls)
            # Mettre le code d'initialisation ici, similaire au constructeur
        return cls._instance

    @classmethod
    def get_address(cls, address):
        geolocator = Nominatim(user_agent="geopy test app")
        current_time = time.perf_counter()
        if current_time - cls._derniere_requete < 1:
            print("Attente de 1 seconde")
            time.sleep(1)
        location = geolocator.geocode(address)
        cls._derniere_requete = time.perf_counter()
        return location


singleton = SingletonSvc.instance()
# La même instance sera retournée
singleton2 = SingletonSvc.instance()

for i in range(0, 10):
    adresse = singleton.get_address("QC J2S 1H9")
    print(adresse)






