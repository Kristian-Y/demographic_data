import requests
from apscheduler.schedulers.background import BackgroundScheduler

API_URL = "https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/USA_Census_Counties/FeatureServer/0/query"
QUERY_PARAMS = {
    "where": "1=1",
    "outFields": "population,state_name",
    "returnGeometry": "false",
    "f": "json"
}

def fetch_and_update_population():
    from .models import StatePopulation
    from django.utils.timezone import now
    
    response = requests.get(API_URL, params=QUERY_PARAMS)
    if response.status_code == 200:
        data = response.json()
        state_population = {}
        for feature in data.get("features", []):
            state_name = feature["attributes"].get("STATE_NAME")
            population = feature["attributes"].get("POPULATION", 0)
            print(feature["attributes"])
            if state_name and population:
                state_population[state_name] = state_population.get(state_name, 0) + population

        for state, population in state_population.items():
            StatePopulation.objects.update_or_create(
                state_name=state, defaults={"population": population, "updated_at": now()}
            )
        print("Population data updated.")
    else:
        print("Failed to fetch data.")

scheduler = BackgroundScheduler()

if not scheduler.running:
    scheduler.add_job(fetch_and_update_population, 'interval', minutes=1)
    scheduler.start()