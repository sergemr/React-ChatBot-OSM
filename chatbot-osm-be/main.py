from llama_cpp import Llama
from flask import Flask, request, jsonify


from flask_cors import CORS  # Import the CORS extension
# from llm_adapter import llm_chatbot_response
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
# Initialize Llama model
print("Using llama-1 chat format@@@@@@")


llm = Llama(
    model_path="./phi-2.Q4_K_S.gguf",  # Download the model file first
    n_ctx=586,  # The max sequence length to use - note that longer sequence lengths require much more resources
    n_threads=22,  # The number of CPU threads to use, tailor to your system and the resulting performance
    # The number of layers to offload to GPU, if you have GPU acceleration available
    n_gpu_layers=16
)

# Simple inference example
# output = llm(
#    "Instruct: {prompt}\nOutput:",  # Prompt
#    max_tokens=50,  # Generate up to 512 tokens
#    # Example stop token - not necessarily correct for this specific model! Please check before using.
#    stop=["</s>"],
#    echo=True        # Whether to echo the prompt
# )

# Chat Completion API


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@app.route('/chat-completion2', methods=['POST'])
def chat_completion_api():
    print("Using chat_completion_api@@@@@@")
    try:
        # Uncomment the lines below if you want to handle incoming JSON requests
        # data = request.get_json()
        # messages = data.get('messages', [])

        # Example messages for testing
        input_messages = [
            {"role": "system", "content": "You are a story writing assistant."},
            {"role": "user", "content": "Write a story about llamas."}
        ]

        print("Using chat_completion_api@@@@@@1")
        response = llm.create_chat_completion(messages=input_messages)
        print("Using chat_completion_api@@@@@@2")
        print(response)

        # Return the response in JSON format
        return jsonify({'response': {"response": response, "messages": []}})

    except Exception as e:
        # Return error message in case of an exception
        return jsonify({'error': str(e)}), 500


@app.route('/chat-completion', methods=['POST'])
def llm_chatbot_response():
    print("Using llama-1 chat llm_chatbot_response @@@@@@")
    print(request)
    llm1 = Llama(model_path="./phi-2.Q4_K_S.gguf",
                 chat_format="llama-2")
    llm = Llama(model_path="./phi-2.Q4_K_S.gguf",
                chat_format="llama-2",
                n_ctx=128,  # The max sequence length to use - note that longer sequence lengths require much more resources
                n_threads=6,  # The number of CPU threads to use, tailor to your system and the resulting performance
                # The number of layers to offload to GPU, if you have GPU acceleration available)
                n_gpu_layers=2)

    data = request.json  # Access the incoming JSON data
    messages = data.get('messages', [])  # Get the messages from the JSON data
    '''
    messages.insert(0, {
        "role": "system",
        "content": "Keep all your answers to a maximum of 25 words",
    },)
    '''
    print("messages")
    print(messages)

    try:
        data = request

        msg = "Write a story about llamas."
        print("Using llama-1 chat format@@@@@@")
        print(data)
        tempmsg = [
            # {"role": "system", "content": "You are a story writing assistant."},
            # {"role": "system", "content": "Your name is Jarvis, you are my personal assistant, and will always introduce youself as such in the biggining of the conversation."},
            {
                "role": "user",
                "content": 'Write a very short story about llamas.'
            }
        ]
        print("Using llama-1 chat formatDATA")
        print(messages)
        print(tempmsg)
        print(data)

        max_tokens = 512  # Experiment with different values
        response = llm.create_chat_completion(
            messages=messages, max_tokens=max_tokens)
        print("Using llama-1 chat format@@@@@@22")
        print(response)
        return response
    except Exception as e:
        return {'error': str(e)}, 500


if __name__ == '__main__':
    # Run the Flask app
    port = 8080  # Define the port number
    print(f"Server running on port {port}")
    app.run(debug=True, port=port)
