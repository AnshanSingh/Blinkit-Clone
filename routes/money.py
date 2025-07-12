from flask import Blueprint, request, jsonify
from flask_cors import CORS      # ✅ Add this
from database import get_connection

money_routes = Blueprint("money", __name__)
CORS(money_routes)               # ✅ This is required!

@money_routes.route('/add-money', methods=['POST'])
def add_money():
    data = request.json
    amount = data.get('amount')

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (amount) VALUES (%s)", (amount,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Money added successfully!"})
