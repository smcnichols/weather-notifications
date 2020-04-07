from twilio.rest import Client
import os
import weather

def weather_reminder():
    # chicago latitude and longitude, hardcoded for now
    latitude = '41.8781'
    longitude = '-87.6298'
    json_obj = weather.make_weather_request(latitude, longitude)
    rain_probs = weather.covert(json_obj)
    if (weather.is_rain(rain_probs)):
        message = "Today's forecast predicts a chance of rain! Make sure to bring an umbrella."
    else:
        message = "Today's forecast is all clear!"

    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        messaging_service_sid=os.getenv('TWILIO_MESSAGING_SERVICE_SID'),
        to=os.getenv('MY_PHONE_NUMBER')
    )

    return message