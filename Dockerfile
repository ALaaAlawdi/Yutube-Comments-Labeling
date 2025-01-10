FROM python:3.12-slim

# Set the working directory 
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
COPY ./src ./src

# Run app.py when the container launches
CMD ["streamlit", "run" , "src/app.py"]

# # Build the image
# docker build -t friendlyhello .

# # Run the app
# docker run -p 4000:80 friendlyhello
