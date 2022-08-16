# Base image
FROM python:3.8

# Set working directory
WORKDIR /app

# Copy files
COPY main.py /app
COPY apps /app/apps
COPY requirements.txt /app
COPY model /app/model

# Install dependencies
RUN pip install -r requirements.txt

# Run the application
EXPOSE 8501
CMD streamlit run main.py
