from llama_cpp import Llama

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
print("Using llama-1 chat format@@@@@@")
llm = Llama(
    model_path="./phi-2.Q4_K_S.gguf",  # Download the model file first
    n_ctx=2048,  # The max sequence length to use - note that longer sequence lengths require much more resources
    # The number of CPU threads to use, tailor to your system and the resulting performance
    n_threads=8,
    # The number of layers to offload to GPU, if you have GPU acceleration available
    n_gpu_layers=6
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

# Set chat_format according to the model you are using

""" print("Using llama-1 chat format@@@@@@")
llm = Llama(model_path="./phi-2.Q4_K_S.gguf", chat_format="llama-2")
response = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "You are a story writing assistant."},
        {
            "role": "user",
            "content": "Write a story about llamas."
        }
    ]
)
print("finished llama-1 chat format@@@@@@")

print(response) """


def llm_chatbot_response(request: None):
    print("Using llama-1 chat llm_chatbot_response @@@@@@")
    print(request)
    llm = Llama(model_path="./phi-2.Q4_K_S.gguf", chat_format="llama-2")

    try:
        data = request
        msg = "Write a story about llamas."
        print("Using llama-1 chat format@@@@@@")
        print(data)
        tempmsg = [
            {"role": "system", "content": "You are a story writing assistant."},
            {
                "role": "user",
                "content": msg
            }
        ]
        print("Using llama-1 chat formatDATA")
        print(tempmsg)
        print(data)
        response = llm.create_chat_completion(
            messages=data
        )
        print("Using llama-1 chat format@@@@@@22")
        print(response)
        return response
    except Exception as e:
        return {'error': str(e)}, 500
