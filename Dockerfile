# Use official Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy your Flask project folder into the container
COPY brundavanpackaging-python-code/ ./brundavanpackaging-python-code/

# Set working directory to the project folder
WORKDIR /app/brundavanpackaging-python-code

# Install dependencies (assuming you have requirements.txt)
COPY brundavanpackaging-python-code/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
