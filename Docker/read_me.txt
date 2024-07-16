##  Linux System  ##
For non-Gnome Desktop environments, gnome-terminal must be installed:
  sudo apt install gnome-terminal

Install Docker Desktop
  sudo apt-get update
  sudo apt-get install ./docker-desktop-<arch>.deb

Check Docker:
  docker --version
  docker compose version
  docker version

Intall Docker in visual studio code.

Create Image: 
  docker build -t <Docker_file_name> <File_location[eg .]>
  sudo docker build -t <Docker_file_name> <File_location[eg .]>


See Images Stored in device:
  sudo docker image ls


Run Docker:
  docker run <Docker_image_name>


##    Docker Hub build, connect and Push  ##
Create account in docker Hub

Build with docker username and respository:
  docker build -t tarunshrestha/first_try:hello-docker .

Login Docker:
  docker login

Docker Push:
  docker push tarunshrestha/first_try:hello-docker

Check present images:
  docker images


Pull Docker:
  docker push tarunshrestha/first_try
  
