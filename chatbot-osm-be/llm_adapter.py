from llama_cpp import Llama
llm = Llama(model_path="./phi-2.Q4_K_S.gguf",
            chat_format="llama-2",
            n_ctx=1024,  # The max sequence length to use - note that longer sequence lengths require much more resources
            n_threads=6,  # The number of CPU threads to use, tailor to your system and the resulting performance
            # The number of layers to offload to GPU, if you have GPU acceleration available)
            n_gpu_layers=2)


def llm_chatbot_response(request_data):
    print("Inside llm_chatbot_response@@@@@@")
    print("request_data")
    print(request_data)

    '''Chatbot response function using Llama model'''

    messages = request_data.get('messages', [])
    max_tokens0 = request_data.get('max_tokens')
    temperature = request_data.get('temperature')
    print("llm_chatbot_response messages")
    print(messages)
    print("llm_chatbot_response max_tokens0")
    print(max_tokens0)
    print("llm_chatbot_response temperature")
    print(temperature)

    try:

        print("Inside llm_chatbot_response try@@@@@@")

        tempmsg = {
            "role": "system",
            "content": 'You are an expert and my personal computing assistant.'
        }

        print("Using llama-1 chat formatDATA")

        messages.insert(0, tempmsg)

        max_tokens = 512  # Experiment with different values
        '''LLM Model Parameters'''
        '''TO-DO Experiment with different values for these parameters to see how they affect the chatbot's responses.'''
        par_temperature = -0.7
        par_top_p = 0.9
        par_top_k = 50
        par_frequency_penalty = 0.5
        par_presence_of_special_tokens = True
        par_context_window_size = 100
        par_beam_size = 3
        print("Using llama-1 chat messages@@@@@@")
        print(messages)

        response = llm.create_chat_completion(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        print("Using llama-1 chat format@@@@@@22")
        print(response)
        return response
    except Exception as e:
        return {'error': str(e)}, 500
