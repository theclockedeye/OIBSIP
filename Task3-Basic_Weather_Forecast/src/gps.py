# /src/gps.py
import geocoder

def get_location_from_gps():
    """Fetch the user's current location using geocoder"""
    g = geocoder.ip('me')
    return g.city if g.city else "London"  # Default to London if no location found
