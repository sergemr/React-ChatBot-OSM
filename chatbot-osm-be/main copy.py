from llama_cpp import Llama
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize Llama model
print("Using llama-1 chat format@@@@@@")
llm = Llama(
    model_path="./phi-2.Q4_K_S.gguf",  # Download the model file first
    n_ctx=512,  # The max sequence length to use - note that longer sequence lengths require much more resources
    n_threads=16,  # The number of CPU threads to use, tailor to your system and the resulting performance
    # The number of layers to offload to GPU, if you have GPU acceleration available
    n_gpu_layers=10
)

# Simple inference example
output = llm(
    "Instruct: {prompt}\nOutput:",  # Prompt
    max_tokens=512,  # Generate up to 512 tokens
    # Example stop token - not necessarily correct for this specific model! Please check before using.
    stop=["</s>"],
    echo=True        # Whether to echo the prompt
)

# Chat Completion API


@app.route('/chat-completion', methods=['POST'])
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


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=8088)
