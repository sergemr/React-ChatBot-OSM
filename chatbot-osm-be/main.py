from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS extension
from llm_adapter import llm_chatbot_response
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/api', methods=['POST'])
def api_endpoint():
    try:

        data = request.get_json()
        print("Using llama-1 chat format@@@@@@ intro")
        print(data)
        request_payload = {
            "message": "Hello"
        }
        response = llm_chatbot_response(data)
        # Your processing logic here

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=8080)
