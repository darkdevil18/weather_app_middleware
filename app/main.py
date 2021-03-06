import requests
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

api_key = "YOUR_API_KEY"
app = FastAPI()

origins = [
	'http://localhost:3000',
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["GET"],
	allow_headers=["*"],
)


@app.get("/")
async def weather_api():
	return {
		"details": "This api is just a middleware between the actual api and the website"
	}


@app.get("/api/weather/{city}",
         description='Returns weather details of the city provided')
async def weather_details(city: str):
	data = requests.get(
		f'https://api.openweathermap.org/data/2.5/weather?', {
			'q': city,
			'APPID': api_key,
			'units': 'metric',
		})

	return data.json()
