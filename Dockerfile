# Use the official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY ./Qdrant_Instance.py /app/Qdrant_Instance.py

# Install dependencies
RUN pip install requests prettytable

# Run the Python script
CMD ["python", "Qdrant_Instance.py"]
