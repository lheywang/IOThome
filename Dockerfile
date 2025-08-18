FROM ubuntu:latest

# Install dependencies
RUN apt-get update  -y
RUN apt-get install -y python3-pip python3 git 
RUN apt-get install -y python3-flask python3-paho-mqtt python3-dotenv

ADD . /IOThome/

# Set the workdir to the base of the folder
WORKDIR /IOThome/host/

# Configure entry point !
ENTRYPOINT ["python3"]
CMD ["main.py"]