from llama_cpp import Llama
from flask import Flask, request, jsonify
# import llm adapter with response function
from llm_adapter import llm_chatbot_response

from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
# Initialize Llama model
print("Using llama-1 chat format@@@@@@")


# Chat Completion API


@app.route('/', methods=['GET'])
def hello_world():
    return '''
    <html>
    <head><title>API Interface for Chatbot 1.0</title></head>
    <body>
        <h1>API Interface for Chatbot 1.0</h1>
        <h2>Description</h2>
        <p>This API provides an interface for interacting with a chatbot based on the LLM (Large Language Model) architecture. The <code>llm_chatbot_response_api</code> function processes incoming POST requests containing chat messages and returns the chatbot's response.</p>
        <h2>Function: llm_chatbot_response_api</h2>
        <p>
            <strong>Purpose:</strong> This function generates a response from the chatbot based on the provided conversation context.
            <br>
            <strong>Method:</strong> POST
            <br>
            <strong>Endpoint:</strong> /chat-completion
            <br>
            <strong>Parameters:</strong>
            <ul>
                <li><code>messages</code>: List of dictionaries representing the conversation history.</li>
                <li><code>temperature</code>: Controls the randomness of the response generation.</li>
                <li><code>max_tokens</code>: Maximum number of tokens to generate in the completion.</li>
                <li><code>stream</code>: Boolean indicating whether to stream the response.</li>
                <!-- Add more parameters as needed -->
            </ul>
            <strong>Returns:</strong> JSON object containing the chatbot's response.
        </p>
    </body>
    </html>
    '''


@app.route('/chat-completion', methods=['POST'])
def llm_chatbot_response_api():
    print("Entering API")

    data = request.json  # Access the incoming JSON data

    try:

        print("Using llama adapter API")

        response = llm_chatbot_response(data)
     #   print(response)
        return response
    except Exception as e:
        return {'error': str(e)}, 500


if __name__ == '__main__':
    # Run the Flask app
    port = 8080  # Define the port number
    print(f"Server running on port {port}")
    app.run(debug=True, port=port)
