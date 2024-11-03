from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Data dummy untuk produk toko swalayan
produk_data = {
    "1": {"name": "Susu", "category": "Minuman", "price": 10000, "stock": 50},
    "2": {"name": "Roti", "category": "Makanan", "price": 5000, "stock": 30},
    "3": {"name": "Sabun", "category": "Kebutuhan Rumah", "price": 8000, "stock": 20},
    "4": {"name": "Shampoo", "category": "Kebutuhan Rumah", "price": 15000, "stock": 40},
    "5": {"name": "Air Mineral", "category": "Minuman", "price": 3000, "stock": 100},
    "6": {"name": "Minyak Goreng", "category": "Makanan", "price": 25000, "stock": 60},
    "7": {"name": "Beras", "category": "Makanan", "price": 12000, "stock": 80},
    "8": {"name": "Gula", "category": "Makanan", "price": 13000, "stock": 70},
    "9": {"name": "Teh", "category": "Minuman", "price": 7000, "stock": 90},
    "10": {"name": "Kopi", "category": "Minuman", "price": 15000, "stock": 50},
    "11": {"name": "Cokelat", "category": "Makanan", "price": 20000, "stock": 45},
    "12": {"name": "Tisu", "category": "Kebutuhan Rumah", "price": 10000, "stock": 35},
    "13": {"name": "Saus Tomat", "category": "Makanan", "price": 5000, "stock": 60},
    "14": {"name": "Mentega", "category": "Makanan", "price": 8000, "stock": 40},
    "15": {"name": "Mie Instan", "category": "Makanan", "price": 2500, "stock": 200},
}

# Endpoint untuk Produk
class ProdukList(Resource):
    def get(self):
        return jsonify(produk_data)

    def post(self):
        new_id = str(len(produk_data) + 1)
        data = request.json
        produk_data[new_id] = data
        return jsonify(produk_data[new_id]), 201

class Produk(Resource):
    def get(self, produk_id):
        produk = produk_data.get(produk_id)
        return jsonify(produk) if produk else ('Produk tidak ditemukan', 404)

    def put(self, produk_id):
        if produk_id in produk_data:
            data = request.json
            produk_data[produk_id].update(data)
            return jsonify(produk_data[produk_id])
        return ('Produk tidak ditemukan', 404)

    def delete(self, produk_id):
        if produk_id in produk_data:
            deleted_produk = produk_data.pop(produk_id)
            return jsonify(deleted_produk)
        return ('Produk tidak ditemukan', 404)

# Menambahkan resource ke API
api.add_resource(ProdukList, '/produk')
api.add_resource(Produk, '/produk/<produk_id>')

if __name__ == '__main__':
    app.run(debug=True)
