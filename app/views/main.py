from flask import Flask, render_template, Blueprint, request, redirect, url_for
from app.forms.search_form import SearchForm
from ..utils import get_city_coordinates, search_api

RADIUS="150km"

main = Blueprint('main', __name__)

@main.route('/')
def index():
    form = SearchForm()
    
    return render_template('index.html', form=form)
  
@main.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        from_city = request.form.get('from_city')
        to_city = request.form.get('to_city')
        date_from = request.form.get('date_from')
        date_to = request.form.get('date_to')
        nights_in_dst_from = request.form.get('nights_in_dst_from') or 1
        nights_in_dst_to = request.form.get('nights_in_dst_to') or 5
        flight_type = request.form.get('flight_type') or "round"
        curr = request.form.get('curr') or "USD"
        price_from = request.form.get('price_from') or 1
        price_to = request.form.get('price_to') or 1000
        
        # Get coordinates for from_city and to_city
        from_lat, from_long = get_city_coordinates(from_city)
        to_lat, to_long = get_city_coordinates(to_city) if to_city else (None, None)
        from_city = f"{round(from_lat, 6)}-{round(from_long, 6)}-{RADIUS}"
        to_city = f"{round(to_lat, 6)}-{round(to_long, 6)}-{RADIUS}" if to_city else ""
        
        results = search_api(from_city, to_city, date_from, date_to, nights_in_dst_from, nights_in_dst_to, flight_type, curr, price_from, price_to)
        results = results["data"]
    
        return render_template("results.html", results=results, form=form)
    
    
    return render_template(url_for("main.index"), form=form)
