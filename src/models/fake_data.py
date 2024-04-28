from random import choice
from datetime import datetime
from tkinter import Variable
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
events_music = [
    Event(
        name="Symphonic Night with Beethoven",
        date=datetime(2024, 5, 10, 20, 00),  # Adjust date and time as needed
        duration=2.5,  # Duration in hours
        description="Immerse yourself in the timeless melodies of Beethoven's masterpieces performed by the City Philharmonic Orchestra.",
        event_type_id=1,  # Assuming "Musique" category has ID 1
        salle_id=2,  # Replace with actual Salle ID
        nb_places_availables=200,
        image="beethoven_symphony.jpg",
        note=4.8,
        etat="Disponible"
    ),
    Event(
        name="Rockin' the Night: The Rolling Stones Tribute",
        date=datetime(2024, 6, 1, 19, 00),
        duration=3.0,
        description="Relive the legendary energy of The Rolling Stones with a electrifying tribute performance. Get ready to sing along to classic hits!",
        event_type_id=1,
        salle_id=3,
        nb_places_availables=350,
        image="rolling_stones_tribute.jpg",
        note=4.5,
        etat="Disponible"
    ),
    Event(
        name="Jazz Night: Smooth Sounds with Sarah Jones",
        date=datetime(2024, 4, 30, 21, 00),  # Adjust date closer to current date
        duration=2.0,
        description="Unwind with the soulful and captivating melodies of renowned jazz vocalist Sarah Jones. Perfect for a relaxing evening.",
        event_type_id=1,
        salle_id=1,
        nb_places_availables=120,
        image="sarah_jones_jazz.jpg",
        note=4.9,
        etat="Disponible"
    ),
    Event(
        name="Global Beats: World Music Festival",
        date=datetime(2024, 7, 15, 16, 00),
        duration=8.0,  # Festival duration (adjust as needed)
        description="Embark on a journey around the world through music! This all-day festival features international artists representing diverse musical traditions.",
        event_type_id=1,
        salle_id=None,  # Festival might occur outdoors, adjust if needed
        nb_places_availables=0,  # Festival might not have limited capacity
        image="world_music_festival.jpg",
        note=0.0,  # No rating yet
        etat="Bientôt disponible"  # Coming soon
    ),
    Event(
        name="Up-and-Coming: Local Indie Showcase",
        date=datetime(2024, 5, 18, 18, 00),
        duration=4.0,
        description="Discover the next generation of musical talent! This showcase features performances from rising local indie bands.",
        event_type_id=1,
        salle_id=4,
        nb_places_availables=150,
        image="indie_showcase.jpg",
        note=0.0,  # No rating yet
        etat="Disponible"
    ), Event(
        name="Piano Prodigy: Recital by Young Maestro",
        date=datetime(2024, 8, 22, 19, 30),
        duration=1.5,
        description="Witness the exceptional talent of a rising young pianist as they perform a captivating recital.",
        event_type_id=1,
        salle_id=1,
        nb_places_availables=80,
        image="young_piano_prodigy.jpg",
        note=0.0,  # No rating yet
        etat="Bientôt disponible"
    ),
    Event(
        name="Vinyl Vibes: Classic Rock Night",
        date=datetime(2024, 6, 29, 22, 00),
        duration=3.0,
        description="Dust off your dancing shoes and relive the golden era of rock music with this vinyl DJ night.",
        event_type_id=1,
        salle_id=2,
        nb_places_availables=250,
        image="classic_rock_night.jpg",
        note=4.2,
        etat="Disponible"
    ),
    Event(
        name="Opera Extravaganza: La Traviata",
        date=datetime(2024, 9, 14, 20, 00),
        duration=3.5,
        description="Immerse yourself in the dramatic world of opera with a captivating performance of Verdi's La Traviata.",
        event_type_id=1,
        salle_id=3,
        nb_places_availables=400,
        image="la_traviata_opera.jpg",
        note=0.0,  # No rating yet
        etat="En vente"  # Tickets on sale
    ),
    Event(
        name="Groove Therapy: Funk and Soul Party",
        date=datetime(2024, 5, 25, 21, 00),
        duration=4.0,
        description="Get ready to groove and move to the infectious beats of funk and soul music. This party is guaranteed to get you dancing all night long!",
        event_type_id=1,
        salle_id=4,
        nb_places_availables=180,
        image="funk_soul_party.jpg",
        note=4.7,
        etat="Disponible"
    ),
    Event(
        name="Music for the Mind: Sound Healing Meditation",
        date=datetime(2024, 7, 7, 19, 00),
        duration=1.0,
        description="Experience a deeply relaxing and transformative sound healing meditation session, using music and vibrations to promote inner peace and well-being.",
        event_type_id=1,
        salle_id=5,  # Assuming there's a Salle with ID 5
        nb_places_availables=30,
        image="sound_healing_meditation.jpg",
        note=0.0,  # No rating yet
        etat="Bientôt disponible"
    )
]
events_sport=[
    Event(
        name="Championnat National de Football: Finale",  # National Football Championship: Final
        date=datetime(2024, 6, 15, 18, 00),
        duration=3.0,
        description="Don't miss the electrifying culmination of the National Football Championship as the top teams vie for the title!",
        event_type_id=2,  # Assuming "Sport" category has ID 2
        salle_id=1,  # Adjust Salle ID for the stadium
        nb_places_availables=50000,  # Large capacity for a stadium
        image="national_football_final.jpg",
        note=0.0,  # No rating yet
        etat="Bientôt disponible"  # Coming soon
    ),
    Event(
        name="Marathon International de Dakar",  # Dakar International Marathon
        date=datetime(2024, 12, 8, 7, 00),  # Adjust date for a cooler time
        duration=0,  # Marathon duration varies
        description="Challenge yourself and experience the beauty of Dakar on this prestigious international marathon course.",
        event_type_id=2,
        salle_id=None,  # Marathon is an outdoor event
        nb_places_availables=10000,  # Limited capacity for marathon registration
        image="dakar_marathon.jpg",
        note=4.3,  # Average rating from previous marathons
        etat="Inscriptions ouvertes"  # Registration open
    ),
    Event(
        name="Tournoi de Beach Volley: Ouvert à tous",  # Beach Volleyball Tournament: Open to All
        date=datetime(2024, 8, 10, 10, 00),
        duration=6.0,  # Tournament duration (adjust as needed)
        description="Grab your friends and join the fun at this open beach volleyball tournament! All skill levels welcome.",
        event_type_id=2,
        salle_id=None,  # Beach volleyball is an outdoor event
        nb_places_availables=48,  # Limited to 12 teams (4 players per team)
        image="beach_volleyball_tournament.jpg",
        note=0.0,  # No rating yet
        etat="Inscriptions ouvertes"  # Registration open
    ),
    Event(
        name="Gala de Boxe Professionnelle",  # Professional Boxing Gala
        date=datetime(2024, 7, 20, 20, 00),
        duration=3.0,
        description="Witness the power and skill of professional boxers at this thrilling gala event.",
        event_type_id=2,
        salle_id=3,  # Adjust Salle ID for the boxing arena
        nb_places_availables=3000,  # Capacity of the boxing arena
        image="boxing_gala.jpg",
        note=4.8,  # High rating from previous events
        etat="En vente"  # Tickets on sale
    ),
    Event(
        name="Cours de Yoga en Plein Air",  # Outdoor Yoga Class
        date=datetime(2024, 5, 12, 9, 00),  # Adjust date for pleasant weather
        duration=1.5,
        description="Unwind and reconnect with your inner self in this relaxing outdoor yoga class. All levels welcome.",
        event_type_id=2,  # Sport can include fitness activities
        salle_id=None,  # Outdoor yoga class
        nb_places_availables=25,  # Limited space for a comfortable class
        image="outdoor_yoga_class.jpg",
        note=4.9,  # High rating from previous participants
        etat="Disponible"  # Open spots available
    ), Event(
        name="Match de Basketball NBA: Raptors vs. Celtics",
        date=datetime(2024, 5, 23, 20, 00),
        duration=2.5,  # Duration of a basketball game
        description="Experience the electrifying rivalry between the Toronto Raptors and the Boston Celtics in this NBA game.",
        event_type_id=2,
        salle_id=2,  # Assuming the arena is Salle ID 2
        nb_places_availables=18000,  # Capacity of the basketball arena
        image="nba_raptors_celtics.jpg",
        note=4.7,  # High rating for a popular matchup
        etat="En vente"  # Tickets on sale
    ),
    Event(
        name="Tournoi d'Echecs International: Grand Maître Challenge",
        date=datetime(2024, 6, 3, 10, 00),
        duration=0,  # Chess tournaments can vary in length
        description="Witness the strategic minds of Grand Masters clash in this international chess tournament.",
        event_type_id=2,
        salle_id=4,  # Adjust Salle ID for the chess venue
        nb_places_availables=100,  # Limited spectator spots
        image="chess_grandmaster_tournament.jpg",
        note=0.0,  # No rating yet for this new tournament
        etat="Bientôt disponible"  # Coming soon
    ),
    Event(
        name="Cours de Zumba: Danse et Fitness",
        date=datetime(2024, 7, 17, 18, 30),
        duration=1.0,  # Duration of a typical Zumba class
        description="Get your heart pumping and have fun with this energetic Zumba dance fitness class.",
        event_type_id=2,  # Sport can include fitness activities
        salle_id=5,  # Assuming there's a Salle with ID 5
        nb_places_availables=20,  # Limited class size for a personalized experience
        image="zumba_dance_fitness.jpg",
        note=4.9,  # High rating from previous participants
        etat="Disponible"  # Open spots available
    ),
    Event(
        name="Escalade Sportive: Mur Artificiel",
        date=datetime(2024, 8, 24, 14, 00),
        duration=0,  # Climbing duration depends on individual pace
        description="Challenge yourself and conquer new heights on our indoor climbing wall. All levels welcome.",
        event_type_id=2,
        salle_id=6,  # Assuming there's a Salle with ID 6 for the climbing gym
        nb_places_availables=12,  # Limited capacity for safety reasons
        image="indoor_climbing_gym.jpg",
        note=4.6,  # Positive rating from previous climbers
        etat="Disponible"  # Open spots available
    ),
    Event(
        name="Cours de Natation pour Adultes",
        date=datetime(2024, 5, 16, 19, 00),
        duration=1.0,  # Duration of a typical adult swimming lesson
        description="Improve your swimming skills or learn to swim in this group lesson for adults.",
        event_type_id=2,  # Sport can include aquatic activities
        salle_id=1,  # Assuming the pool is part of Salle ID 1
        nb_places_availables=8,  # Limited class size for effective instruction
        image="adult_swimming_lessons.jpg",
        note=4.5,  # Positive rating from previous students
        etat="Inscriptions ouvertes"  # Registration open
    )]
events_art=[
     Event(
        name="Exposition d'Art Moderne: Couleurs et Formes",  # Modern Art Exhibition: Colors and Shapes
        date=datetime(2024, 6, 8, 11, 00),
        duration=3.0,  # Typical duration for an art exhibition
        description="Immerse yourself in a vibrant world of colors and shapes at this modern art exhibition.",
        event_type_id=3,  # Assuming "Art" category has ID 3
        salle_id=4,  # Adjust Salle ID for the art gallery
        nb_places_availables=0,  # Art exhibitions may not have limited capacity
        image="modern_art_exhibition.jpg",
        note=4.8,  # High rating from previous exhibitions
        etat="En cours"  # Exhibition is ongoing
    ),
    Event(
        name="Spectacle de Danse Contemporaine: Mouvement et Émotion",  # Contemporary Dance Performance: Movement and Emotion
        date=datetime(2024, 7, 19, 20, 00),
        duration=1.5,  # Typical duration for a contemporary dance performance
        description="Experience the captivating power of movement and emotion in this contemporary dance performance.",
        event_type_id=3,
        salle_id=2,  # Adjust Salle ID for the theater
        nb_places_availables=500,  # Capacity of the theater
        image="contemporary_dance_performance.jpg",
        note=4.9,  # High rating from previous performances
        etat="En vente"  # Tickets on sale
    ),
    Event(
        name="Atelier de Sculpture: Création en Argile",  # Sculpture Workshop: Clay Creation
        date=datetime(2024, 5, 25, 14, 00),
        duration=2.0,  # Typical duration for a sculpture workshop
        description="Unleash your creativity and learn the art of sculpting with clay in this hands-on workshop.",
        event_type_id=3,
        salle_id=5,  # Assuming there's a Salle with ID 5 for the workshop
        nb_places_availables=15,  # Limited class size for personalized instruction
        image="clay_sculpture_workshop.jpg",
        note=0.0,  # No rating yet for this new workshop
        etat="Inscriptions ouvertes"  # Registration open
    ),
    Event(
        name="Visite Guidée du Musée d'Histoire",  # Guided Museum Tour: History Museum
        date=datetime(2024, 8, 12, 15, 00),
        duration=1.5,  # Typical duration for a guided museum tour
        description="Embark on a journey through time and discover fascinating artifacts and stories at this guided museum tour.",
        event_type_id=3,
        salle_id=6,  # Assuming there's a Salle with ID 6 for the museum
        nb_places_availables=25,  # Limited tour group size for a personalized experience
        image="history_museum_guided_tour.jpg",
        note=4.7,  # Positive rating from previous tours
        etat="Disponible"  # Open spots available
    ),
    Event(
        name="Concert de Musique Classique: Orchestre Symphonique",  # Classical Music Concert: Symphony Orchestra
        date=datetime(2024, 5, 30, 19, 30),
        duration=2.0,  # Typical duration for a classical music concert
        description="Experience the timeless beauty of classical music performed by a renowned symphony orchestra.",
        event_type_id=3,  # Art can also include music events
        salle_id=1,  # Adjust Salle ID for the concert hall
        nb_places_availables=800,  # Capacity of the concert hall
        image="symphony_orchestra_concert.jpg",
        note=5.0,  # Perfect rating from previous concerts
        etat="En vente"),
    Event(
        name="Concert de Jazz: Soirée Improvisation",  # Jazz Concert: Improvisation Night
        date=datetime(2024, 11, 21, 21, 00),
        duration=0,  # Jazz improvisation sessions can vary in length
        description="Experience the thrill of spontaneous creativity at this captivating jazz improvisation night.",
        event_type_id=3,
        salle_id=2,  # Adjust Salle ID for the jazz club
        nb_places_availables=150,  # Capacity of the jazz club
        image="jazz_concert_improvisation_night.jpg",
        note=4.9,  # High rating from previous improvisation nights
        etat="En vente"  # Tickets on sale
    ),
    Event(
        name="Festival des Arts de Rue: Spectacles et Animations",  # Street Art Festival: Performances and Entertainment
        date=datetime(2024, 9, 8, 14, 00),
        duration=8.0,  # Duration of a street art festival (adjust as needed)
        description="Immerse yourself in a vibrant celebration of street art with performances, music, and interactive activities.",
        event_type_id=3,
        salle_id=None,  # Street art festival takes place outdoors
        nb_places_availables=0,  # Free outdoor event
        image="street_art_festival_performances.jpg",
        note=0.0,  # No rating yet for this new festival
        etat="Bientôt disponible"  # Coming soon
    ),
    Event(
        name="Cours de Calligraphie: Art de l'Écriture",  # Calligraphy Class: Art of Writing
        date=datetime(2024, 10, 11, 10, 00),
        duration=2.5,  # Duration of a typical calligraphy class
        description="Discover the meditative art of calligraphy and learn to create beautiful handwritten works in this beginner's class.",
        event_type_id=3,
        salle_id=5,  # Assuming there's a Salle with ID 5 for the art studio
        nb_places_availables=8,  # Limited class size for personalized instruction
        image="calligraphy_class_art_writing.jpg",
        note=4.7,  # Positive rating from previous participants
        etat="Inscriptions ouvertes"  # Registration open
    ),
    Event(
        name="Visite Guidée: Architecture et Patrimoine",  # Guided Tour: Architecture and Heritage
        date=datetime(2024, 8, 3, 11, 00),
        duration=2.0,  # Typical duration for a guided architecture tour
        description="Explore the rich architectural heritage of the city on this captivating guided tour.",
        event_type_id=3,
        salle_id=None,  # Guided tour takes place outdoors
        nb_places_availables=20,  # Limited tour group size for a personalized experience
        image="guided_architecture_tour.jpg",
        note=4.9,  # High rating from previous tours
        etat="Disponible"  # Open spots available
    ),
    Event(
        name="Atelier de Création de Bijoux: Techniques Artisanales",  # Jewelry Making Workshop: Artisan Techniques
        date=datetime(2024, 6, 21, 15, 00),
        duration=3.0,  # Duration of a typical jewelry making workshop
        description="Unleash your creativity and learn the art of jewelry making using traditional artisan techniques in this hands-on workshop.",
        event_type_id=3,
        salle_id=4,  # Assuming there's a Salle with ID 4 for the workshop space
        nb_places_availables=12,  # Limited class size for personalized instruction
        image="jewelry_making_workshop_artisan_techniques.jpg",
        note=4.5,  # Positive rating from previous participants
        etat="Inscriptions ouvertes"  # Registration open
    )
]
events_gastro=[
    Event(
        name="Dîner Gastronomique: Saveurs du Monde",  # Gastronomic Dinner: Flavors of the World
        date=datetime(2024, 9, 15, 20, 00),
        duration=3.0,  # Typical duration for a fine dining experience
        description="Embark on a culinary journey around the world with a carefully crafted tasting menu by our renowned chef.",
        event_type_id=4,  # Assuming "Gastronomy" category has ID 4
        salle_id=1,  # Adjust Salle ID for the restaurant
        nb_places_availables=15,  # Limited seating for an intimate dining experience
        image="gastronomic_dinner_flavors_world.jpg",
        note=4.9,  # High rating from previous dinners
        etat="En vente"  # Tickets on sale
    ),
    Event(
        name="Cours de Cuisine: Plats Italiens Authentiques",  # Cooking Class: Authentic Italian Dishes
        date=datetime(2024, 10, 3, 18, 30),
        duration=2.5,  # Duration of a typical cooking class
        description="Learn the secrets of authentic Italian cuisine and master the art of making homemade pasta, sauces, and desserts in this hands-on cooking class.",
        event_type_id=4,
        salle_id=5,  # Assuming there's a Salle with ID 5 for the cooking space
        nb_places_availables=10,  # Limited class size for personalized instruction
        image="italian_cooking_class_authentic_dishes.jpg",
        note=4.7,  # Positive rating from previous participants
        etat="Inscriptions ouvertes"  # Registration open
    ),
    Event(
        name="Festival Gastronomique: Street Food du Monde",  # Food Festival: Street Food from Around the World
        date=datetime(2024, 11, 22, 11, 00),
        duration=10.0,  # Duration of a food festival (adjust as needed)
        description="Indulge in a tantalizing array of street food flavors from diverse cultures at this international food festival.",
        event_type_id=4,
        salle_id=None,  # Food festival takes place outdoors
        nb_places_availables=0,  # Free outdoor event
        image="street_food_festival_world.jpg",
        note=0.0,  # No rating yet for this new festival
        etat="Bientôt disponible"  # Coming soon
    ),
    Event(
        name="Dégustation de Vins: Découverte et Accords Mets & Vins",  # Wine Tasting: Discovery and Food & Wine Pairings
        date=datetime(2024, 8, 29, 19, 00),
        duration=2.0,  # Typical duration for a wine tasting event
        description="Expand your wine knowledge and discover the art of food and wine pairing in this guided wine tasting experience.",
        event_type_id=4,
        salle_id=2,  # Adjust Salle ID for the wine bar or tasting venue
        nb_places_availables=25,  # Limited group size for an intimate tasting experience
        image="wine_tasting_discovery_food_wine_pairings.jpg",
        note=4.8,  # High rating from previous tastings
        etat="Disponible"  # Open spots available
    ), Event(
        name="Cours de Cuisine: Cuisine Végétarienne Délicieuse",  # Cooking Class: Delicious Vegetarian Cuisine
        date=datetime(2024, 12, 6, 18, 00),
        duration=2.5,  # Duration of a typical cooking class
        description="Explore the vibrant world of vegetarian cuisine and learn how to prepare healthy, flavorful dishes in this hands-on cooking class.",
        event_type_id=4,
        salle_id=5,  # Assuming there's a Salle with ID 5 for the cooking space
        nb_places_availables=8,  # Limited class size for personalized instruction
        image="vegetarian_cooking_class_delicious_dishes.jpg",
        note=0.0,  # No rating yet for this new class
        etat="Inscriptions ouvertes"  # Registration open
    ),
    Event(
        name="Atelier Brunch: Saveurs du Matin",  # Brunch Workshop: Morning Flavors
        date=datetime(2024, 10, 26, 10, 30),
        duration=2.5,  # Typical duration for a brunch workshop
        description="Create a delightful brunch spread and learn the art of plating and presentation in this fun and interactive workshop.",
        event_type_id=4,
        salle_id=1,  # Adjust Salle ID for the workshop space (e.g., restaurant or cafe)
        nb_places_availables=12,  # Limited class size for a personalized experience
        image="brunch_workshop_morning_flavors.jpg",
        note=0.0,  # No rating yet for this new workshop
        etat="Bientôt disponible"  # Coming soon
    ),
    Event(
        name="Conférence: Alimentation et Nutrition",  # Lecture: Food and Nutrition
        date=datetime(2024, 9, 20, 14, 00),
        duration=1.5,  # Typical duration for a lecture on food and nutrition
        description="Gain valuable insights into healthy eating habits and learn how to make informed food choices in this informative lecture.",
        event_type_id=4,
        salle_id=3,  # Assuming there's a Salle with ID 3 for the lecture hall
        nb_places_availables=40,  # Accommodate a larger audience for the lecture
        image="food_and_nutrition_lecture.jpg",
        note=0.0,  # No rating yet for this new lecture
        etat="Disponible"  # Open spots available
    ),
    Event(
        name="Marché de Produits Locaux: Frais et Bio",  # Local Farmers Market: Fresh and Organic
        date=datetime(2024, 11, 9, 9, 00),
        duration=5.0,  # Typical duration for a farmers market
        description="Support local farmers and enjoy the freshest seasonal produce, artisan goods, and prepared foods at this weekly farmers market.",
        event_type_id=4,
        salle_id=None,  # Farmers market takes place outdoors
        nb_places_availables=0,  # Free outdoor event
        image="local_farmers_market_fresh_organic.jpg",
        note=4.9,  # High rating from previous markets
        etat="En cours"  # Ongoing event (every week)
    ),
    Event(
        name="Soirée Dégustation de Chocolat: Saveurs du Monde",  # Chocolate Tasting Night: Flavors of the World
        date=datetime(2024, 8, 2, 19, 30),
        duration=2.0,  # Typical duration for a chocolate tasting event
        description="Embark on a delightful journey through the world of chocolate as you sample a variety of fine chocolates from different regions.",
        event_type_id=4,
        salle_id=2,  # Adjust Salle ID for the chocolate shop or tasting venue
        nb_places_availables=20,  # Limited group size for an intimate tasting experience
        image="chocolate_tasting_night_flavors_world.jpg",
        note=4,
         etat="En vente")
]
events_culture=[
    Event(
        name="Conférence: L'Histoire de l'Art Moderne",  # Lecture: History of Modern Ardatetime(2024, 9, 10, 18, 00),
        duration=1.5,  # Typical duration for an art history lecture
        description="Delve into the fascinating world of modern art with this captivating lecture by a renowned art historian.",
        event_type_id=5,  # Assuming "Culture" category has ID 5
        salle_id=3,  # Assuming there's a Salle with ID 3 for the lecture hall
        nb_places_availables=80,  # Limited seating for the lecture
        image="modern_art_lecture_history.jpg",
        note=4.6,  # Positive rating from previous lectures
        etat="Disponible"  # Open spots available
    ),
    Event(
        name="Visite Guidée: Musée d'Histoire Naturelle",  # Guided Tour: Natural History Museudatetime(2024, 10, 17, 11, 30),
        duration=2.0,  # Typical duration for a guided museum tour
        description="Explore the wonders of the natural world and discover fascinating exhibits about plants, animals, and dinosaurs on this captivating guided tour.",
        event_type_id=5,
        salle_id=None,  # Museum tour takes place indoors
        nb_places_availables=30,  # Limited tour group size for a personalized experience
        image="natural_history_museum_guided_tour.jpg",
        note=4.9,  # High rating from previous tours
        etat="En vente"  # Tickets on sale
    ),
    Event(
        name="Festival Interculturel: Musique, Danses et Traditions",  # Intercultural Festival: Music, Dance, and Traditiondatetime(2024, 11, 24, 14, 00),
        duration=8.0,  # Duration of a cultural festival (adjust as needed)
        description="Celebrate the richness of diverse cultures through captivating performances, music, and traditional activities at this vibrant intercultural festival.",
        event_type_id=5,
        salle_id=None,  # Festival takes place outdoors
        nb_places_availables=0,  # Free outdoor event
        image="intercultural_festival_music_dance_traditions.jpg",
        note=0.0,  # No rating yet for this new festival
        etat="Bientôt disponible"  # Coming soon
    ),
    Event(
        name="Atelier de Théâtre: Initiation au Jeu d'Acteur",  # Theater Workshop: Introduction to Actindatetime(2024, 8, 2, 16, 00),
        duration=2.5,  # Duration of a typical theater workshop
        description="Discover the fundamentals of acting and explore your creativity in this beginner's theater workshop.",
        event_type_id=5,
        salle_id=4,  # Assuming there's a Salle with ID 4 for the theater space
        nb_places_availables=12,  # Limited class size for personalized instruction
        image="theater_workshop_introduction_acting.jpg",
        note=4.7,  # Positive rating from previous participants
        etat="Inscriptions ouvertes"  # Registration open
    ),
    Event(
        name="Club de Lecture: Découverte Littéraire",  # Book Club: Literary Discoverdatetime(2024, 6, 20, 19, 30),
        duration=2.0,  # Typical duration for a book club meeting
        description="Join us for a lively discussion and share your thoughts on a selected book in this welcoming book club.",
        event_type_id=5,
        salle_id=2,  # Assuming there's a Salle with ID 2 for the book club meeting
        nb_places_availables=15,  # Limited group size for a more intimate discussion
        image="book_club_literary_discovery.jpg",
        note=4.8,  # High rating from previous book club meetings
        etat="Disponible")
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
    Event(name="Conférence sur l'intelligence artificielle", date="2024-05-10T14:00", duration=2, description="Conférence sur les avancées en intelligence artificielle", event_type_id=5, salle_id=2, nb_places_availables=500, image="ai.jpg", note=4, etat="Confirmé"),
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

def load_events_by_categorie(categorie:str):
    category = session.query(CategorieEvent).filter_by(name=categorie).first()
    # If the category exists, retrieve the corresponding events
    if category:
        events=session.query(Event).filter(Event.event_type_id == category.id).all()
        return events
    else:
        return None
     
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
        existing_places = Event.query.all() 
        
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
    


