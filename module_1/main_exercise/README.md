** Build the Docker Image **
docker build -t global_weather_tracker_app .

** Deploying Python Applications with Docker **
docker run -it --rm --name my-running-app global_weather_tracker_app