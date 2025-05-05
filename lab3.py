
# Author: Yoko Parks
#
# Class:  CSCD 330 Tony Espinoza 
#
# Date:   22 April 2025


from flask import Flask
from json import loads 
from requests import get
from socket import gethostbyname
from subprocess import getstatusoutput


# !!! APPLICATION DATA CACHE: !!!
address_cache = {}
weather_cache = {}


app = Flask(__name__)

# Returns Full Address of Domain:
@app.route("/address/<domain>")
def get_address(domain):

   try:
      # Check For Data Cache:
      if domain in address_cache:
         address = address_cache[domain]['address']
         return f"[CACHED]: {address} \n" 

      # Get IP from domain:
      ip = gethostbyname(domain)
     
      # Get Whois Info:
      status, out = getstatusoutput(f"whois {ip}")    

      # Fields for Address:
      fields = {
         'NetRange': None,
         'Address': None,
         'City': None,
         'State': None,
         'Postal Code': None,
         }

      # Address Field Mapping:
      mapping = {
         'NetRange': 'NetRange',
         'Address': 'Address',
         'City': 'City',
         'State': 'State',
         'StateProv': 'StateProv',
         'PostalCode': 'Postal Code',
         'Zip': 'Postal Code',
         }

      # Line Trim for Address: 
      for line in out.splitlines():
         line = line.strip()
         for whois_key, field_name in mapping.items():
            if line.startswith(f"{whois_key}:"):
               fields[field_name] = line.split(":", 1)[1].strip()
      
               break;
      
      # Format the address for output:
      street= fields.get("Address")
      city= fields.get("City")
      state= fields.get("StateProv") or fields.get("State")
      zip= fields.get("Postal Code" )
   
      # Modify Global Var For Use in "/range"
      nrange= fields.get("NetRange")   
  
      # Nicely Formatted Address For My Human Eyes
      address = f"{street}, {city}, {state}, {zip} \n"
   
      # !!! CACHE ADDRESS & NRANGE DATA !!!
      address_cache[domain] = {'address': address, 'nrange': nrange}

      # Function Returns The Address
      return address

   # $$ Error Code: DOMAIN FORMAT $$
   except:
      return f"Couldn't Resolve Domain: Error DOMAIN_FMT \n"


# Shows Network Range of Domain 
@app.route("/range/<domain>")
def get_nrange(domain):
   
   try:
      # Retrieve Address & Nrange Together
      if domain in address_cache:
         nrange = address_cache[domain]['nrange']
         return f"Network range for {domain} is : {nrange} \n"

      # Else Populate The Cache
      get_address(domain)
      nrange = address_cache[domain]['nrange']
      return f"Network range for {domain} is: {nrange} \n"

   # $$ Error Code: BAD DOMAIN $$
   except:
      return f"Couldn't Fetch NetRange: Error BAD_DOMAIN \n"



# Shows Last Hr. Weather
# Condition, high temp, wind dir && speed
@app.route("/weather/<domain>")
def get_weather(domain):
   
   try:   
      # Check Data Cache for Existing Data
      if domain in weather_cache:
         weatherout = weather_cache[domain]['weather']
         return f"[CACHED]: {weatherout} \n"

      # If Not Found, get_address of Domain
      if domain not in address_cache:
         get_address(domain)

      # !!! CACHE ADDRESS !!!
      address = address_cache[domain]['address']
      
      # Make Address Pleasant & Error If You Can't Format 
      parts = [part.strip() for part in address.strip().split(",") if part.strip()]
      if len(parts) != 4:

         # $$ Error Code: BAD ADDRESS FORMAT $$
         return "Invalid Address Format Can't Fetch Weather: Error BAD_ADDR_FMT \n"
  
      # Formatted Address: 
      street, city, state, zip = parts
   
      # API URLs Used:
      coords_url= f"https://geocoding.geo.census.gov/geocoder/locations/address?street={street}&city={city}&state={state}&zip={zip}&benchmark=Public_AR_Current&format=json"
   
      # Get Coordinates API call:
      response = get(coords_url)
      coords_js = loads(response.text)
      coords = coords_js['result']['addressMatches'][0]['coordinates']
  
      # Assign Fetched Coordinates to lat, lon
      lon = coords['x']
      lat = coords['y']
      
      # Get Weather API call:
      weather_url = f"https://api.weather.gov/points/{lat},{lon}"
      weather_response = get(weather_url)
      weather_data = loads(weather_response.text)

      # Get Weather Data:
      forecast_url = weather_data['properties']['forecast']
      weather_forecast = get(forecast_url)
      forecast_js = loads(weather_forecast.text)

      # Weather Data Formatting:
      weatherout = [period['detailedForecast'] for period in forecast_js['properties']['periods'][:1]]   
      weather_final = weatherout[0]
     
      # !!! CACHE WEATHER DATA: !!!
      weather_cache[domain] = {'weather': weather_final}

      # Return Weather Data With NewLine spacing:
      return f"{weather_final} \n"

   # $$ Error Code: BAD API CALL $$
   except:
      return f"Can't Get Weather Data: Error BAD_API_CALL \n"    


@app.route('/')
def online_status():
   return 'Weather API is Online!'




if __name__ == "__main__":

   # Execute App
   app.run()
