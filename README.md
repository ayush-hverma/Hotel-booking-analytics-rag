# Hotel Booking Analytics & Q&A System

## Overview
This project processes hotel booking data, extracts insights, and enables Retrieval-Augmented Question Answering (RAG) using FAISS and Sentence Transformers.

## Features
- **Data Preprocessing**: Cleans and processes booking records.
- **Analytics**: Generates revenue trends, cancellation rates, and lead-time distribution.
- **Question Answering**: Uses FAISS to retrieve relevant bookings based on user queries.
- **Flask API**: Provides `/ask` endpoint to answer user questions.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/hotel-booking-project.git
cd hotel-booking-project
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3. Run the Flask API
```
python flask_api.py
```
### 4. Test the API
```
import requests
url = "http://127.0.0.1:5000/ask"
data = {"question": "What is the average price of a hotel booking?"}
response = requests.post(url, json=data)
print(response.json())
```
