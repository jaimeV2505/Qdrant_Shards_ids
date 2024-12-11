# Qdrant_Shards_ids

This Python script queries the Qdrant API and retrieves information about the current shards of a specified collection in a Qdrant instance. The script presents the data in a well-formatted table for easy viewing. This version runs inside a Docker container for convenience.

Download the repo

Docker Setup
Build the Docker image: In the terminal, navigate to the folder containing the Dockerfile and run the following command to build the Docker image:

docker build -t qdrant-shards-script .
Run the Docker container: After building the image, you can run the script within the container by executing:


docker run --rm qdrant-shards-script

This will execute the script, and the output will be displayed in the terminal.
