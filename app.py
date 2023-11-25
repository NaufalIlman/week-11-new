import flask
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

pesan_default = [
    "Makan patty",
    "Berdansalah,",
    "inpone",
    "selamat datang",
    "selamat belanja",
    "Semangat terus",
    "tidak boleh",
    "jangan lupa",
    "stay strong",
    "ayo main"
]

@app.route('/', methods=['GET', 'POST'])
def puja_kerang_ajaib():
    if request.method == 'GET':
        nama = request.args.get('nama')
        if nama:
            pesan = f"{nama}, {random.choice(pesan_default)}"
        else:
            pesan = random.choice(pesan_default)
        return jsonify({'pesan': pesan})

    elif request.method == 'POST':
        nama = request.form.get('nama')
        pesan = f"Selamat datang, {nama}, anda berhasil masuk ke Puja Kerang Ajaib"
        return jsonify({'pesan': pesan})

if __name__ == '__main__':
    # Use Waitress as the production server
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
