FROM ubuntu:latest

# Install dependencies
RUN apt-get update -y
RUN apt-get install -y python3-pip python3 git python3-flask

# Invalidate cache :
ARG CACHE_DATE=2016-01-02

# Fetch the source
# production
# RUN cd / && git clone https://github.com/lheywang/IOThome.git
# dev (copy your local folder)
ADD . /IOThome/

# Set the workdir to the base of the folder
WORKDIR /IOThome/

# Configure entry point !
ENTRYPOINT ["python3"]
CMD ["host/main.py"]