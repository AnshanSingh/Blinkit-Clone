from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/category/<name>', methods=['GET'])
def get_category(name):
    products = []

    if name == "electronics":
        products = [
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/1649771/pexels-photo-1649771.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/31683433/pexels-photo-31683433.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/1619651/pexels-photo-1619651.jpeg"},
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/18589085/pexels-photo-18589085.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/5099868/pexels-photo-5099868.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3330855/pexels-photo-3330855.jpeg"}
        ]

    elif name == "All":
        products = [
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/286951/pexels-photo-286951.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3800060/pexels-photo-3800060.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/14924052/pexels-photo-14924052.jpeg"},
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/19577587/pexels-photo-19577587.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3373738/pexels-photo-3373738.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/20499754/pexels-photo-20499754.jpeg"}
        ]

    elif name == "beauty":
        products = [
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/286951/pexels-photo-286951.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3800060/pexels-photo-3800060.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/14924052/pexels-photo-14924052.jpeg"},
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/19577587/pexels-photo-19577587.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3373738/pexels-photo-3373738.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/20499754/pexels-photo-20499754.jpeg"}
        ]
    elif name == "decor":
        products = [
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/286951/pexels-photo-286951.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3800060/pexels-photo-3800060.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/14924052/pexels-photo-14924052.jpeg"},
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/19577587/pexels-photo-19577587.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3373738/pexels-photo-3373738.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/20499754/pexels-photo-20499754.jpeg"}
        ]

    elif name == "kids":
        products = [
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/286951/pexels-photo-286951.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3800060/pexels-photo-3800060.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/14924052/pexels-photo-14924052.jpeg"},
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/19577587/pexels-photo-19577587.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3373738/pexels-photo-3373738.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/20499754/pexels-photo-20499754.jpeg"}
        ]

    elif name == "gifting":
        products = [
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/286951/pexels-photo-286951.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3800060/pexels-photo-3800060.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/14924052/pexels-photo-14924052.jpeg"},
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/19577587/pexels-photo-19577587.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3373738/pexels-photo-3373738.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/20499754/pexels-photo-20499754.jpeg"}
        ]

    elif name == "premium":
        products = [
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/286951/pexels-photo-286951.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3800060/pexels-photo-3800060.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/14924052/pexels-photo-14924052.jpeg"},
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/19577587/pexels-photo-19577587.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3373738/pexels-photo-3373738.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/20499754/pexels-photo-20499754.jpeg"}
        ]
    else:
        products = [
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/1649771/pexels-photo-1649771.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/31683433/pexels-photo-31683433.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/1619651/pexels-photo-1619651.jpeg"},
            {"name": "Laptop", "price": 50000, "image": "https://images.pexels.com/photos/18589085/pexels-photo-18589085.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/5099868/pexels-photo-5099868.jpeg"},
            {"name": "Phone", "price": 20000, "image": "https://images.pexels.com/photos/3330855/pexels-photo-3330855.jpeg"}
        ]

    return jsonify({
        "category": name,
        "products": products
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
