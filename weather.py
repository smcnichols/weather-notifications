import requests
import os

def make_weather_request(latitude, longitude):
	dark_sky_api_key = os.getenv('DARK_SKY_API_KEY')
	url_base = f'https://api.darksky.net/forecast'
	excludes = 'exclude=currently,minutely,daily,alerts,flags'
	request_url = f'{url_base}/{dark_sky_api_key}/{latitude},{longitude}?{excludes}'
	r = requests.get(request_url)
	return r.json()

def covert(json_obj):
	hourly_data = json_obj['hourly']['data']
	time_to_rain_prob = {}
	for entry in hourly_data:
		if 'precipType' in entry:
			time = entry['time']
			precip_prob = entry['precipProbability']
			time_to_rain_prob[time] = precip_prob
	return time_to_rain_prob

def rain_times(rain_probs):
	return [time for time in rain_probs if rain_probs[time] > 0.4]

def is_rain(rain_probs):
	return len(rain_times(rain_probs)) > 0