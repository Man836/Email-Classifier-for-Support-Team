from flask import Flask, request, jsonify
from utils import mask_pii
import joblib

app = Flask(__name__)
model = joblib.load("model/classifier.pkl")

@app.route("/classify_email", methods=["POST"])
def classify():
    data = request.get_json()
    input_email = data["email"]
    masked_email, entities = mask_pii(input_email)
    category = model.predict([masked_email])[0]

    response = {
        "input_email_body": input_email,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
