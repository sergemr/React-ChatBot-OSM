from llama_cpp import Llama
import numpy as np
# llm = Llama(model_path="./llm-phi.gguf", #Use llm-phi.gguf for the Phi model
# llm = Llama(model_path="./llm-codellama-instruct.gguf", #Use llm-codellama-instruct.gguf for the CodeLlama model
llm = Llama(model_path="./llm-gemma.gguf",  # Use llm-gemma.gguf for the Gemma model
            chat_format="llama-2",
            n_ctx=124,  # The max sequence length to use - note that longer sequence lengths require much more resources
            n_threads=6,  # The number of CPU threads to use, tailor to your system and the resulting performance
            # The number of layers to offload to GPU, if you have GPU acceleration available)
            n_gpu_layers=2)


def sanitize_response(response):
    """
    Sanitize the response by removing unwanted characters and formatting.

    Args:
        response (str): The response string to sanitize.

    Returns:
        str: The sanitized response.
    """
    # Remove newline characters, leading and trailing whitespace, and HTML tags
    sanitized_response = response.replace("\n", "").strip().replace(
        "<[/SYS>]", "").replace("<[/S", "").replace("<S>", "").replace("</S>", "").replace("<Inst>", "").replace("</Inst>", "")

    return sanitized_response


def llm_chatbot_response(request_data):
    '''Chatbot response function using Llama model'''

    messages = request_data.get('messages', [])
    max_tokens0 = request_data.get('max_tokens')
    temperature = request_data.get('temperature')

    try:

        tempmsg = {
            "role": "system",
            "content": 'Given only the context provided.'
        }

        messages.insert(0, tempmsg)

        max_tokens = 124  # Experiment with different values
        '''LLM Model Parameters'''
        '''TO-DO Experiment with different values for these parameters to see how they affect the chatbot's responses.'''
        par_temperature = -0.7
        par_top_p = 0.9
        par_top_k = 50
        par_frequency_penalty = 0.5
        par_presence_of_special_tokens = True
        par_context_window_size = 100
        par_beam_size = 3

        response = llm.create_chat_completion(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

        content_to_sanitize = response['choices'][0]['message']['content']

        # Sanitize the content
        sanitized_content = sanitize_response(content_to_sanitize)

        response['choices'][0]['message']['content'] = sanitized_content

        return response
    except Exception as e:
        return {'error': str(e)}, 500


def llm_chatbot_response_vs(request_data, vector_store):
    # Get request data
    messages = request_data.get('messages', [])
    temperature = request_data.get('temperature')
    max_tokens = 200
    try:
        # Extract embeddings from the vector store
        embeddings = [vector_store.get(
            f'embedding_{i}', None) for i in range(len(messages))]
        # Filter out None values
        embeddings = [emb for emb in embeddings if emb is not None]
        print("messages")
        print(messages)
        # Construct combined input with messages and embeddings
        combined_input = []
        # Add embeddings to the combined input

        combined_input += [
            {'role':  message['role'], 'content': message['content']} for message in messages]
        combined_input += [{'role': 'context', 'content': emb}
                           for emb in embeddings]
        # Print combined input for debugging
        print("Combined input:")
        print(combined_input)

        # Use LLama model to generate chatbot response
        response = llm.create_chat_completion(
            messages=combined_input, temperature=temperature, max_tokens=max_tokens
        )

        # Extract and sanitize chatbot response
        sanitized_content = sanitize_response(
            response['choices'][0]['message']['content'])

        # Return sanitized response
        return {'message': sanitized_content}, 200

    except Exception as e:
        return {'error': str(e)}, 500
