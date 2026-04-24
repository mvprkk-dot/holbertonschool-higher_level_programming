#!/usr/bin/python3
"""
Bu modul istifadəçi idarəetməsi üçün sadə bir Flask API təqdim edir.
İstifadəçilərin əlavə edilməsi, siyahıya alınması və məlumatların
gətirilməsi funksiyalarını dəstəkləyir.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçi məlumatlarını yadda saxlayan lüğət (In-memory storage)
users = {}


@app.route('/')
def home():
    """Əsas səhifə üçün mesaj qaytarır."""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """Sistemdəki bütün istifadəçi adlarının siyahısını qaytarır."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """API-ın işlək vəziyyətdə olduğunu yoxlamaq üçün endpoint."""
    return "OK"


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Yeni istifadəçini sistemə əlavə edir.
    Gözlənilən JSON formatı: {"username": "ad", "name": "...", ...}
    """
    data = request.get_json()

    # JSON datası və ya username yoxdursa xəta qaytar
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # İstifadəçinin artıq mövcud olub-olmadığını yoxla
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # İstifadəçi məlumatlarını topla
    user_data = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }
    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


@app.route("/users/<username>")
def get_user(username):
    """Müəyyən bir istifadəçinin məlumatlarını qaytarır."""
    user_info = users.get(username)

    if not user_info:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user_info)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
