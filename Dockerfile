# Use a minimal Python image as the base image  
FROM python:3.9-slim  

# Set the working directory inside the container  
WORKDIR /home/data  

# Copy the Python script into the container  
# This script will be executed when the container runs  
COPY scripts.py /home/data/scripts.py  

# Copy text files into the container  
# These files might be used as input data for the script  
COPY IF-1.txt /home/data/IF-1.txt  
COPY AlwaysRememberUsThisWay-1.txt /home/data/AlwaysRememberUsThisWay-1.txt  

# Install required Python packages  
# Using --no-cache-dir to reduce image size by avoiding unnecessary cache files  
RUN pip install --no-cache-dir nltk  

# Set the default command to execute the Python script  
# This ensures the script runs automatically when the container starts  
CMD ["python", "/home/data/scripts.py"]  
