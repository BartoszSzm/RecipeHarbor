FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy your application code into the container
COPY . /app

# Install any necessary dependencies using pip
RUN pip install -r requirements.txt

# Set env vars
ENV PYTHONPATH="$PYTHONPATH:/app/src"
