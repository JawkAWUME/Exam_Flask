from random import choice
from datetime import datetime
from sqlalchemy import and_, or_
import locale
from .model import *
categories_event_list = [
    CategorieEvent(name="Musique"),
    CategorieEvent(name="Sport"),
    CategorieEvent(name="Art"),
    CategorieEvent(name="Gastronomie"),
    CategorieEvent(name="Culture")
]

categories_salle_list = [
    CategorieSalle(name="Théatre"),
    CategorieSalle(name="Conférence"),
    CategorieSalle(name="Atelier"),
    CategorieSalle(name="Arène"),
]
salles_list = [
    # Paris
    Salle(name="Le Grand Palais Éphémère", capacite=4000, adresse="Place Joffre, 75007 Paris", salle_type_id=2),  # Conference
    Salle(name="La Seine Musicale", capacite=6000, adresse="Île Seguin, 92100 Boulogne-Billancourt", salle_type_id=3),  # Atelier
    Salle(name="Théâtre du Châtelet", capacite=2450, adresse="1 place du Châtelet, 75001 Paris", salle_type_id=1),  # Theatre

    # New York
    Salle(name="Madison Square Garden", capacite=18000, adresse="4 Pennsylvania Plaza, New York, NY 10001", salle_type_id=4),  # Arena
    Salle(name="Carnegie Hall", capacite=2804, adresse="881 7th Ave, New York, NY 10019", salle_type_id=3),  # Atelier
    Salle(name="Apollo Theater", capacite=1500, adresse="253 W 125th St, New York, NY 10027", salle_type_id=1),  # Theatre

    # Los Angeles
    Salle(name="Microsoft Theater", capacite=7000, adresse="777 Chick Hearn Ct, Los Angeles, CA 90014", salle_type_id=2),  # Conference
    Salle(name="Dolby Theatre", capacite=3400, adresse="6801 Hollywood Blvd, Los Angeles, CA 90028", salle_type_id=1),  # Theatre
    Salle(name="Staples Center", capacite=18118, adresse="1111 S Figueroa St, Los Angeles, CA 90015", salle_type_id=4),  # Arena

    # Dakar
    Salle(name="Grand Théâtre National", capacite=1800, adresse="Place de l'Indépendance, Dakar", salle_type_id=1),  # Theatre
    Salle(name="Institut Français Léopold Sédar Senghor", capacite=800, adresse="Corniche Ouest, Dakar", salle_type_id=2),  # Conference
    Salle(name="Salle du CICAD (Centre International du Commerce Extérieur)", capacite=1500, adresse="Route de l'aéroport, Dakar", salle_type_id=2),  # Conference

    # Lomé
    Salle(name="Palais des Congrès de Lomé", capacite=1500, adresse="Boulevard de la Marina, Lomé", salle_type_id=2),  # Conference
    Salle(name="Agora Senghor", capacite=700, adresse="Avenue Sylvanus Olympio, Lomé", salle_type_id=3),  # Atelier
    Salle(name="Canal Olympia Lomé", capacite=2000, adresse="Boulevard du Mono, Lomé", salle_type_id=3),  # Atelier

    # London
    Salle(name="O2 Arena", capacite=20000, adresse="Peninsula Square, London SE10 0DX", salle_type_id=4),  # Arena
    Salle(name="Royal Albert Hall", capacite=5272, adresse="Kensington Gore, London SW7 2AP", salle_type_id=3),  # Atelier
    Salle(name="Shakespeare's Globe", capacite=1500, adresse="Bankside, London SE1 9EU", salle_type_id=1),  # Theatre
]

categorie_places_list = [
    CategoriePlace(name="Standard"),
    CategoriePlace(name="Confort"),
    CategoriePlace(name="VIP"),
    CategoriePlace(name="Loge"),
    CategoriePlace(name="Accessible"),
]
tours_list = [
    Tour(name="Tour Parisien", description="Découvrez les événements les plus emblématiques de Paris"),
    Tour(name="Tour New Yorkais", description="Explorez les lieux culturels de New York"),
    Tour(name="Tour Londonien", description="Voyagez à travers la culture londonienne")
]
events_tours_list = [
    Event(name="Concert au Grand Palais Éphémère", date="2024-04-15T20:00", duration=3, description="Concert de musique pop", event_type_id=1, salle_id=1, nb_places_availables=3500, image="concert.jpg", note=4, etat="Confirmé", tour_id=1),
    Event(name="Théâtre au Théâtre du Châtelet", date="2024-04-20T19:30", duration=2, description="Pièce de théâtre classique", event_type_id=5, salle_id=3, nb_places_availables=2200, image="theatre.jpg", note=5, etat="Confirmé", tour_id=1),
    Event(name="Match au Stade de France", date="2024-04-25T15:00", duration=2.5, description="Match de football", event_type_id=2, salle_id=4, nb_places_availables=25000, image="football.jpg", note=4, etat="Confirmé", tour_id=1),
    Event(name="Concert à Madison Square Garden", date="2024-04-18T21:00", duration=4, description="Concert de rock", event_type_id=1, salle_id=4, nb_places_availables=15000, image="concert.jpg", note=4, etat="Confirmé", tour_id=2),
    Event(name="Atelier à Carnegie Hall", date="2024-04-22T14:00", duration=2, description="Atelier d'art plastique", event_type_id=3, salle_id=5, nb_places_availables=2500, image="art.jpg", note=4, etat="Confirmé", tour_id=2),
    Event(name="Spectacle à l'Apollo Theater", date="2024-04-28T20:30", duration=2.5, description="Spectacle de comédie", event_type_id=5, salle_id=6, nb_places_availables=1200, image="comedy.jpg", note=4, etat="Confirmé", tour_id=2),
    Event(name="Match à l'O2 Arena", date="2024-04-19T18:00", duration=3, description="Match de basket-ball", event_type_id=2, salle_id=7, nb_places_availables=18000, image="basketball.jpg", note=4, etat="Confirmé", tour_id=3),
    Event(name="Atelier au Royal Albert Hall", date="2024-04-24T16:00", duration=2.5, description="Atelier de danse contemporaine", event_type_id=3, salle_id=8, nb_places_availables=3000, image="dance.jpg", note=4, etat="Confirmé", tour_id=3),
    Event(name="Spectacle au Shakespeare's Globe", date="2024-04-30T19:45", duration=2, description="Représentation de théâtre shakespearien", event_type_id=5, salle_id=9, nb_places_availables=1400, image="shakespeare.jpg", note=4, etat="Confirmé", tour_id=3)
]

# Liste de cinq événements indépendants
independent_events_list = [
    Event(name="Exposition au Louvre", date="2024-05-05T10:00", duration=4, description="Exposition d'art moderne", event_type_id=3, salle_id=3, nb_places_availables=3000, image="art.jpg", note=4, etat="Confirmé"),
    Event(name="Conférence sur l'intelligence artificielle", date="2024-05-10T14:00", duration=2, description="Conférence sur les avancées en intelligence artificielle", event_type_id=2, salle_id=2, nb_places_availables=500, image="ai.jpg", note=4, etat="Confirmé"),
    Event(name="Soirée gastronomique au Ritz", date="2024-05-15T20:00", duration=3, description="Dîner gastronomique avec dégustation de vins", event_type_id=4, salle_id=1, nb_places_availables=100, image="gastronomy.jpg", note=4, etat="Confirmé"),
    Event(name="Spectacle de danse au Moulin Rouge", date="2024-05-20T21:30", duration=2.5, description="Spectacle de danse cabaret", event_type_id=5, salle_id=3, nb_places_availables=1200, image="dance.jpg", note=4, etat="Confirmé"),
    Event(name="Match de tennis à Roland-Garros", date="2024-05-25T15:00", duration=3, description="Match de tennis de haut niveau", event_type_id=2, salle_id=1, nb_places_availables=15000, image="tennis.jpg", note=4, etat="Confirmé")
]


event_id = 1 # Get the event ID

# Sample place data (you might have this information elsewhere)
place_numbers = range(1, 21)  # List of place numbers (1 to 20)
category_id = 1  # Replace with the actual category ID for these places

# Create a list to store Place objects
places = []
fixed_price_cfa = 10000 
for number in place_numbers:
  # Create a Place object
  place = Place(
      numero=number,
      salle_id=events_tours_list[0].salle_id,  # Inherit room ID from the event
      place_type_id=category_id,
      etat_place="En Vente",  # Set state to "En Vente"
      event_id=event_id,
      prix=fixed_price_cfa
  )
  places.append(place)

for event in independent_events_list:
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
    event.date = datetime.strptime(event.date, '%Y-%m-%dT%H:%M')
    
for event in events_tours_list:
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
    event.date = datetime.strptime(event.date, '%Y-%m-%dT%H:%M')
        
def load_events_categories():
    existing_categories_event = CategorieEvent.query.all() 
    return existing_categories_event
# def load_events_categories():
with app.app_context():
        session = db.session();event = session.query(Event).filter(Event.id == 1).first()
        event.image="""https://img.static-af.com/images/media/10575D3D-36C7-4459-85A64F80A75BD80F/"""
        event1 = session.query(Event).filter(Event.id == 2).first()
        event1.image="""https://www.evenement.com/wp-content/uploads/2019/09/samuel-pereira-uf2nnANWa8Q-unsplash-2.jpg"""
        event2 = session.query(Event).filter(Event.id == 3).first()
        event2.image="""https://www.leparisien.fr/resizer/JOpnO99ilbDC5apYqb_lzbPFHNQ=/1280x800/arc-anglerfish-eu-central-1-prod-leparisien.s3.amazonaws.com/public/GKGUOS5KA6ZKSUGSVHY7JVEYNY.jpg"""
        event3=session.query(Event).filter(Event.id == 4).first()
        event3.image="""https://th.bing.com/th/id/R.89ce10cfb2fa6ed8099b52da1e4c87bf?rik=SJ2uzLhEZLEceA&pid=ImgRaw&r=0"""
        event4=session.query(Event).filter(Event.id == 5).first()
        event4.image="""https://images.performgroup.com/di/library/sporting_news/6/ff/roland-garros051816-getty-ftrjpg_907kppywder615wnl2li1tb5s.jpg?t=-1001516756"""
        
        tour=session.query(Tour).filter(Tour.id == 1).first()
        tour.image="""https://img-4.linternaute.com/sAyE-UQi5SfRanXWfBO_g2PdAhI=/1500x/smart/d431309131cd40e98cc594af042a057b/ccmcms-linternaute/46189441.jpg"""
        tour2=session.query(Tour).filter(Tour.id == 2).first()
        tour2.image="""https://thepostarg.com/wp-content/uploads/2016/07/01nyskyline1536.jpg"""
        tour3=session.query(Tour).filter(Tour.id == 3).first()
        tour3.image="""https://www.voyageavecnous.fr/wp-content/uploads/2021/01/big-ben-londres.jpg"""      
        # existing_salles = Event.query.all() 
        # if len(existing_salles) ==0: 
        #      session.add_all(independent_events_list)
        #      session.add_all(events_tours_list)
        Place.query.delete()
        existing_places = Place.query.all() 
        if len(existing_places) ==0: 
             session.add_all(places)
        # existing_tours=Tour.query.all()
        # if(len(existing_tours)==0):
        #     session.add_all(tours_list)
        session.commit()
        
def load_tours_and_events():
    evenements = session.query(Event).filter(Event.tour_id == None).all()
    tours = Tour.query.all()
    l=[]
    l.extend(evenements)
    l.extend(tours)
    return l

def get_event(name:str):
    event = session.query(Event).filter(Event.name == name,Event.tour_id==None).first() 
    if event  is not None:
        return event
    event_1=session.query(Tour).filter(Tour.name == name).first()
    if event_1  is not None:
        return event_1
    return "Cet évenement n'existe pas"

def get_all_events_and_tours():
    events = Event.query.all()
    tours=Tour.query.all()
    events.extend(tours)
    return events




def get_research_tours_and_events(searchTerm):
    tours_events = db.session.query(Event).filter(
        or_(
            Event.name.ilike("%" + searchTerm + "%"),
            Event.description.ilike("%" + searchTerm + "%"),
            db.or_(
                # Search within related tables (salle, tour) using joins
                Event.salle.has(Salle.name.ilike("%" + searchTerm + "%")),
                Event.tour.has(Tour.name.ilike("%" + searchTerm + "%")),
            ),
        )
    ).all()
    return tours_events

def get_salle(id:int):
    salle= session.query(Salle).get(id)
    print(salle)
    if salle is not None:
        return salle
    return "La salle n'existe pas"

def load_salles_categories():
    existing_salles_event = CategorieSalle.query.all() 
    return existing_salles_event

def categories_place_event(id):
    event = Event.query.get(id)  # Assuming ID of Event id is id
# Get place categories for Event id
    place_categories = (
    db.session.query(CategoriePlace)
    .join(Place, and_(Place.event_id == event.id, Place.place_type_id == CategoriePlace.id))
    .distinct()
    .all())
    return place_categories

def categorie_place(ticket_type):
    cat =CategoriePlace.query.filter_by(name=ticket_type).first() 
    return cat

def place_by_cat(cat):
    return Place.query.filter_by(place_type=cat).first()

def len_available_places(event_id,categorie_place:CategoriePlace):
    return len(db.session.query(Place).filter(Place.event_id==event_id,Place.place_type == categorie_place, Place.etat_place == "En Vente").all())


def get_cart():
    return db.session.query(CartItem).all()

global data
data={}
if "panier" not in data:
    data["panier"]=[]
    


