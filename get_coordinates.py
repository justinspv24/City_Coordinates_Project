import pandas as pd
from geopy.geocoders import Nominatim

def get_city_coordinates(city_name):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

def main():
    # Read the CSV file
    df = pd.read_csv('cities.csv')

    # Initialize lists to store coordinates
    latitudes = []
    longitudes = []

    # Get coordinates for each city
    for city in df['City']:
        latitude, longitude = get_city_coordinates(city)
        latitudes.append(latitude)
        longitudes.append(longitude)

    # Add the coordinates to the DataFrame
    df['Latitude'] = latitudes
    df['Longitude'] = longitudes

    # Save the DataFrame to a new CSV file
    df.to_csv('cities_with_coordinates.csv', index=False)

    print("Coordinates have been added and saved to cities_with_coordinates.csv")

if __name__ == "__main__":
    main()
