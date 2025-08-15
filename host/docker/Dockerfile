FROM ubuntu:latest

# Install dependencies
RUN apt-get update -y
RUN apt-get install -y python3-pip python3 git python3-flask

# Fetch the source
# production
# RUN cd / && git clone https://github.com/lheywang/IOThome.git
# dev (replace with your branch)
RUN cd / && git clone -b dev https://github.com/lheywang/IOThome.git

# Set the workdir to the base of the folder
WORKDIR /IOThome/

# Configure entry point !
ENTRYPOINT ["python3"]
CMD ["host/src/main.py"]