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
        "products": products,
        # "category": "feature", "products": products
    })
@app.route('/api/category/feature')
def get_feature():
    products = [
        {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://media.istockphoto.com/id/934717782/photo/traditional-indian-gold-necklace-with-earrings.jpg?s=2048x2048&w=is&k=20&c=7lC_e1P1Glox4VOLwOjwHYYJQdDV2SAZ4ACF_x5eCu0="
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://media.istockphoto.com/id/1177580113/photo/antique-gold-necklace-with-peacock-design.jpg?s=2048x2048&w=is&k=20&c=8kbQXxjfSTODyLaubpyHO1P7rO5WKTOCeAizLEP27wU="
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://media.istockphoto.com/id/1177579981/photo/antique-gold-necklace-with-peacock-design.jpg?s=2048x2048&w=is&k=20&c=njP5avX1tGZG0Fs0JaEWzIH3VJQm_ciiH-XIzbIbaSY="
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://media.istockphoto.com/id/1658696488/photo/close-up-of-gold-and-diamond-necklace-with-pair-of-earrings.jpg?s=2048x2048&w=is&k=20&c=xcblAozSyYMnn19zuurWQAmSOTNz0047LpKRBALt1SQ="
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://media.istockphoto.com/id/1142403677/photo/authentic-traditional-indian-jewelery-necklace-on-dark-background-wear-in-neck-in-wedding.jpg?s=2048x2048&w=is&k=20&c=pzZf82uwAOck9uqDVw_bTntS0DkoIrmjJvUeqBdrT-c="
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://media.istockphoto.com/id/153648526/photo/diamond-necklace-with-earring.jpg?s=2048x2048&w=is&k=20&c=TnpXlwnJLhUssFtqsVR6j2pahOeH_5J04cX-X6oWTlg="
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://images.pexels.com/photos/998521/pexels-photo-998521.jpeg"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://images.pexels.com/photos/265804/pexels-photo-265804.jpeg"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://images.pexels.com/photos/722905/pexels-photo-722905.jpeg"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://images.pexels.com/photos/27405174/pexels-photo-27405174.jpeg"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://images.pexels.com/photos/750148/pexels-photo-750148.jpeg"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://images.pexels.com/photos/32652451/pexels-photo-32652451.jpeg"
        }
    ]
    return jsonify({"category": "feature", "products": products})


@app.route('/api/category/paan')
def get_paan():
    products = [
        {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQc-UWzfwEFHo6PGI1rIC3LeJdsWXG_G8va1w&s"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGJDicO5UhuW2qH7bSR_b6nBWiYiyn2wfpZ7mMp2yZGgs7xMmL3Cogay_JEe-0j4c4BGg&usqp=CAU"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://images.raasakarts.com/insecure/fit/1920/1080/ce/0/plain/https://rasakart-assets.s3.ap-south-1.amazonaws.com/vendor/xJ4MV5sPqAU0XA8oMlTLxaw8UP0rnYvVwcrypWpI.jpg@webp"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8RTG2jSxkgKIpq3MqNYjRrowXJ3XOJmbq33YBMbUk5c7xj90AzROnjEcTR09Vkket_-o&usqp=CAU"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://cdn.grofers.com/cdn-cgi/image/f=auto,fit=scale-down,q=70,metadata=none,w=360/da/cms-assets/cms/product/a8b16dad-42a4-4f24-b5c9-13fb0ca62492.jpg?ts=1750072634"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://www.shaadidukaan.com//user_files/d_p_images/32-37-b.jpg"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://brijbooti.in/wp-content/uploads/2023/06/1-12.jpg"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://www.satvikstore.in/cdn/shop/files/Betel_Nuts.jpg?v=1745395531"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://surili.shop/cdn/shop/files/Ice-cream-Supari-My-Store-145699730.jpg?v=1744606843&width=1946"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://thestateplate.com/cdn/shop/products/B5_3_gwv7cUmIKsg.jpg?v=1680931873"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRk1KFiZpJCE62Ddu7F00ObXp9d4LKF-1G8kA&s"
        },
         {
            "name": "Parle Monaco Cheeslings Classic Biscuit",
            "weight": "300g",
            "price": 39,
            "mrp": 160,
            "discount": "10% off",
            "rating": 4,
            "ratingCount": 1956,
            "time": "8 MINS",
            "image": "https://desijadibuti.com/wp-content/uploads/2024/09/Supari-Puja-1.jpg"
        }
    ]
    return jsonify({"category": "paan", "products": products})




if __name__ == '__main__':
    app.run(debug=True, port=5000)
