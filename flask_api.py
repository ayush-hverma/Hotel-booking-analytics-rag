import pickle
import faiss
import numpy as np
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

index = faiss.read_index("C:/Users/ayush/Desktop/New folder/faiss_index.bin")
df = pickle.load(open("C:/Users/ayush/Desktop/New folder/df.pkl", "rb"))
model = SentenceTransformer('all-MiniLM-L6-v2')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Hotel Booking API."})

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get('question', '')
    
    if not query:
        return jsonify({"error": "Question is required"}), 400
    
    query_embedding = model.encode([query], convert_to_numpy=True)
    _, indices = index.search(query_embedding, 5)
    
    results = df.iloc[indices[0]].to_dict(orient='records')
    return jsonify({"results": results})

if __name__ == '__main__':
    print("Starting Flask API...")
    app.run(host='0.0.0.0', port=5000, debug=False)
