from flask import Flask, redirect, render_template, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from forms import CupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'mychickensteve'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()


@app.route('/api/cupcakes', methods=['GET'])
def get_cupcakes():
    """Returns all cupcakes as JSON"""
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<id>', methods=['GET'])
def get_cupcake_by_id(id):
    """Returns single cupcake by ID as JSON"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake = cupcake.serialize()
    return jsonify(cupcake=cupcake)

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """Creates a new cupcake and saves to db, returns created cupcake as JSON"""
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']
    
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<id>', methods=['PATCH'])
def update_cupcake(id):
    """Updates a single cupcake by ID returns updated cupcake as JSON"""
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    return (jsonify(cupcake=cupcake.serialize()), 200)

@app.route('/api/cupcakes/<id>', methods=['DELETE'])
def delete_cupcake(id):
    """Deletes a single cupcake from db by ID, returns 'deleted'"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='Deleted')



@app.route('/')
def homepage():
    form = CupcakeForm()
    return render_template('index.html', form=form)