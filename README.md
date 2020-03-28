# Weather Notifications

## About
This project is currently a work in progress. The project idea is to create a service that will text message me in the mornings about the weather. To start, this service will simply check if there is rain in the forecast for that day. If there is, then it will text message me a warning and suggest I bring an umbrella with me when I go out. If the forecast is clear, then the service will text message me to tell me just that. I'll call this functionality the MVP.

After I have completed the MVP, I have a few extension in mind:
* Based on the forecast, recommend a window of time for going for a walk/run in order to avoid the rain.
* If I haven't gone for a walk or run yet in a given day and the forecast predicts rain, then the service will send me a text message reminder to get outside before the rain starts.
* Add a way for other people to subscribe to this service.
* Maybe to learn more about webscraping, I could scrape weather data from weather sites instead of using api?

## Done
* Set up github repo.
* Sign up for free trial of Google Cloud Platform.
* Mirror the github repo on [Google Cloud Source Repositories](https://source.cloud.google.com/) ([guide](https://cloud.google.com/source-repositories/docs/mirroring-a-github-repository)).
* Create a new project on Google Cloud Platform.
* Create a "Hello World" Google Cloud Function.
* Sign up for free trial of Twilio.
* Fix up the versions of python I have installed on my personal computer [(guide)](https://docs.python-guide.org/starting/install3/osx/)
* Follow Twilio [python quickstart guide](https://www.twilio.com/docs/sms/quickstart/python-msg-svc).
* Add Twilio text messaging to my Google Cloud Function. The way the function works now is that it will check if the incoming request that triggered the function has a message in it. If so, it text messages that message to me. Otherwise, it sends "Hello World!"
* Add a test job to Google Cloud Scheduler that sends HTTP request to my Google Cloud Function. Right now the test job sends a POST request with a body that contains the message "Goodnight, Sally!" and is scheduled to trigger every night at 10:45pm. This way my function will text message me 15 mins before my bed time each night :)
* In target function, temporarily force parsing incoming HTTP request to JSON because Google Cloud Scheduler does not allow you to specify the mimetype in your HTTP request. I had to do this in order to get my test job that sends a goodnight message working.
* Sign up for [Dark Sky weather api](https://darksky.net/).
* Write function to make Dark Sky request.

## TODO
* Make HTTP request parsing more robust in Google Cloud Function instead of just forcing json parsing.
* Schedule weather reporting job to text message me in the mornings.
* Find a way to automatically deploy my Google Cloud Function based on version control trigger. This way whenever I push a new change to github, I don't have to manually go in and deploy the new code for my function.
* Find good ways to test in python (and in general for this project).
* Find out if there is a way to programatically create a job for Google Cloud Scheduler. This way I could add my jobs to version control and keep everything handy in one place. That helps me keep track of all the parts of the project, and also helps make things more replicable.
* python virtual env for local testing
* Make local config file with secret keys for easy local testing. This config file will be in gitignore.
* Programatically get latitude and longitude for a location