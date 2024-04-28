from flask import *
# from flask_login import LoginManager,login_user,login_required,current_user
from ..models.fake_data import *

@app.route("/")
def home_admin():
    global data
    events=load_tours_and_events()
    print(events)
    return render_template("admin/home.html", categories_type=load_events_categories(),events=events)


@login_manager.user_loader
def load_user(user_id):
        """Flask-Login callback to load a user from the database."""
        return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))  # Redirect to your home page

    if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()

            if user and user.verify_password(password):
                login_user(user, remember=request.form.get('remember_me'))
                return redirect(url_for('home'))  # Redirect to your home page
            else:
                flash('Invalid username or password.')

    return render_template('security/login.html')

# Signup function
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html', title='Create an Account')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('signup'))

        user = User(username=username, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

        flash('Account created successfully!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route("/event/<categorie>")
def event_detail(categorie):
    categorie=str.capitalize(categorie)
    events=load_events_by_categorie(categorie)
    return render_template("admin/vue_detail_categorie.html",categorie=categorie,events=events)


@app.route("/event/plan/<name>")
def event_plan(name):
    global data
    event=get_event(name)
    salle=get_salle(event.salle_id)
    categories_place=categories_place_event(event.id)
    print(event.id)
    data["event"]=event
    return render_template("admin/event_planning.html",
        event=event,salle=salle,categories_place = categories_place,cart=data["panier"])


@app.route('/get_ticket_price', methods=['POST'])
def get_ticket_price():
    ticket_type = request.form['ticket_type']
    cat=categorie_place(ticket_type)
    place=place_by_cat(cat)
    places_dispo=len_available_places(event_id,cat)
    if place is not None:
        ticket_price = place.prix  # Access price only if a place is found
        response = {
            'price': ticket_price,
            'places_dispo':places_dispo
        }
        return jsonify(response)
    else:
        # Handle case where no place is found for the ticket type
        return jsonify({'error': 'Ticket type not found'}), 404  # Example error response

def has_ticket_type(key,categorie_type):
  for item in data["panier"]:
    if item[key] == categorie_type:
      return (True,item)
  return (False,None)

@app.route('/add_ticket',methods=['POST']) 
def add_ticket():
    global data
    print(data)
    ticket_type = request.form['ticket_type']
    quantity = int(request.form['quantity'])
    price = float(request.form['ticket_price'])
    total_price =float(request.form['ticket_total_price'])
    cart= get_cart()
    items=[]
    new_item = CartItem(
        ticket_type=ticket_type,
        quantity=quantity,
        price=price,
        total_price=total_price
    )
    bool,item=has_ticket_type("ticket_type", ticket_type)
    if bool:
       data["panier"][item["id"]-1]["quantity"]+=new_item.quantity   
       data["panier"][item["id"]-1]["total_price"]+=new_item.total_price 
       cart_item = session.query(CartItem).get(len(data["panier"]))
       cart_item.quantity= data["panier"][item["id"]-1]["quantity"]
       cart_item.total_price= data["panier"][item["id"]-1]["total_price"]
    else:  
      data["panier"].append({
            "id":len(data["panier"])+1,
            "ticket_type":new_item.ticket_type,
            "quantity":new_item.quantity,
            "price":new_item.price,
            "total_price":new_item.total_price,
            "event": data["event"].name
            
    })
      db.session.add(new_item) 
    # Add new item to the database session
    db.session.commit()
    return redirect(url_for('event_plan',name=data["event"].name))


@app.route("/search", methods=["POST"])
def search():
    searchTerm = request.form["searchTerm"].lower()
    events=get_research_tours_and_events(searchTerm)
    filtered_data = [
        {
            "id": event.id,
            "name": event.name,
            "date": event.date.strftime("%Y-%m-%d %H:%M:%S"),  # Example formatting
            "duration": event.duration,
            "description": event.description,
            "event_type": event.event_type.name if event.event_type else None,  # Example
            "salle": event.salle.name if event.salle else None,  # Example
            "tour": event.tour.name if event.tour else None,  # Example
            "nb_places_availables": event.nb_places_availables,
            "image": event.image,
            "note": event.note,
            "etat": event.etat,
        }
        for event in events
    ]
    return jsonify(filtered_data)

@app.route("/search_all")
def search_view():
    return render_template("admin/search.html")
  