from geopy.geocoders import Nominatim
import requests
import os

BASE_URL="https://api.tequila.kiwi.com/v2"
API_KEY=os.environ.get("API_KEY")

def get_city_coordinates(city):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(city)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude

    return None, None

def search_api(from_city, to_city, date_from, date_to, nights_in_dst_from, nights_in_dst_to, flight_type, curr, price_from, price_to, ret_from_diff_airport=0, ret_to_diff_airport=0, sort="price", limit=100):
    response = requests.get(
      BASE_URL + "/search",
      params={
        "fly_from": from_city,
        "fly_to": to_city,
        "date_from": date_from,
        "date_to": date_to,
        "nights_in_dst_from": nights_in_dst_from,
        "nights_in_dst_to": nights_in_dst_to,
        "flight_type": flight_type,
        "curr": curr,
        "price_from": price_from,
        "price_to": price_to,
        "ret_from_diff_airport": ret_from_diff_airport,
        "ret_to_diff_airport": ret_to_diff_airport,
        "sort": sort,
        "limit": limit,
      },
      headers={"apikey": API_KEY},
      )

    data = response.json()
 
    return data