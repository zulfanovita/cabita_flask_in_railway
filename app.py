# import os
# from flask import Flask, request, jsonify
# import numpy as np
# import joblib
# from tensorflow.keras.models import load_model, Model
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
# from io import BytesIO

# app = Flask(__name__)

# # === Load CNN & Random Forest ===
# cnn_model = load_model("mobilenetv2.h5")
# # Ganti ini untuk ambil fitur 256 (Dense layer) yang sesuai dengan RF training
# feature_extractor = Model(inputs=cnn_model.input, outputs=cnn_model.layers[-3].output)

# rf_model_kadar_air = joblib.load("rf_model_kadar_air.joblib")

# # === Preprocess Gambar ===
# def preprocess_image(file_storage):
#     img = load_img(BytesIO(file_storage.read()), target_size=(224, 224))
#     img = img_to_array(img) / 255.0
#     return np.expand_dims(img, axis=0)

# # === Endpoint Prediksi ===
# @app.route("/predict_kadar_air", methods=["POST"])
# def predict_kadar_air():
#     if 'image' not in request.files:
#         return jsonify({"error": "No image uploaded"}), 400

#     img = preprocess_image(request.files["image"])
#     features = feature_extractor.predict(img)
#     kadar_air = rf_model_kadar_air.predict(features)[0]

#     # # === Aturan: kalau < 5, jadi 0.0; lainnya dibulatkan 1 desimal ===
#     # if kadar_air < 5:
#     #     kadar_air = 0
#     # else:
#     #     kadar_air = round(kadar_air, 1)

#     return jsonify({"predicted_kadar_air": f"{kadar_air}%"})

# @app.route("/", methods=["GET"])
# def home():
#     return "Cabita API is running!"


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Cabita API is running!"

@app.route("/predict_kadar_air", methods=["POST"])
def predict_kadar_air():
    return jsonify({"predicted_kadar_air": "12.5%"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

