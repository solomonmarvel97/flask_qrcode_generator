from flask import Flask, render_template, request, send_file, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Hello World!"})

@app.route("/qr_code", methods=["POST"])
def qr_code():
    try:
        json_data = request.get_json()
        if "data" in json_data:
            data = json_data["data"]
            name = data["name"]
            employee_id = data["employee_id"]
            return jsonify({"name": name})
        else:
            return jsonify({"message": "No data provided"})
    except Exception as e:
        return jsonify({"message": "Invalid data provided"})

if __name__ == "__main__":
    app.run(debug=True)