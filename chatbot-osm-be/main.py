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
        <h2>Endpoint: chat-completion</h2>
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
        
    <h1>React-ChatBot-OSM</h1>

    <p>React-ChatBot Open Source Model</p>

    <ul>
    <li>Security & Privacy are the first concerns, please keep in mind to use opensource, locally executable libraries and assets.</li>
    <li>This application uses PHI, GEMMA & LLama-Instruct for the LLM models, they can be downloaded here (you can ask for the file in the office during the CM Hackathon event):
        <ul>
        <li><a href="https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF/resolve/main/codellama-7b-instruct.Q4_K_S.gguf">codellama-7b-instruct.Q4_K_S.gguf</a></li>
        <li><a href="https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_S.gguf">phi-2.Q4_K_S.gguf</a></li>
        <li><a href="https://huggingface.co/lmstudio-ai/gemma-2b-it-GGUF/resolve/main/gemma-2b-it-q8_0.gguf">gemma-2b-it-q8_0.gguf</a></li>
        </ul>
    </li>
    <li>You are encouraged to use different LLMs and experiment with the results</li>
    </ul>

    <h2>Rag Architecture</h2>

    <img src="https://docs.aws.amazon.com/images/sagemaker/latest/dg/images/jumpstart/jumpstart-fm-rag.jpg" alt="Rag Architecture">

    <h2>Todo list</h2>

    <ol>
    <li>
        <strong>Integrate a file upload function</strong>
        <ul>
        <li>Create an interface in your React application for users to upload files.</li>
        <li>Utilize a library like <code>react-dropzone</code> for handling file uploads.</li>
        <li>Implement backend logic in your Python module to receive and process the uploaded files.</li>
        </ul>
    </li>
    <li>
        <strong>Integrate a Python function to create embeddings for the file</strong>
        <ul>
        <li><strong>Step-by-step guide:</strong>
            <ol>
            <li>Choose a natural language processing library such as <code>spaCy</code> or <code>gensim</code> for generating embeddings.</li>
            <li>Write a Python function that takes the file content as input and generates embeddings using the chosen library.</li>
            <li>Test the function with sample files to ensure proper functionality.</li>
            <li>Integrate the function into your backend module to create embeddings for uploaded files.</li>
            </ol>
        </li>
        </ul>
    </li>
    <li>
        <strong>Save the embeddings into a vector store</strong>
        <ul>
        <li><strong>Step-by-step guide:</strong>
            <ol>
            <li>Choose a suitable database or storage solution such as MongoDB, SQLite, or Redis for saving embeddings.</li>
            <li>Design a schema to store embeddings along with metadata (e.g., file name, timestamp).</li>
            <li>Implement logic in your backend module to save the generated embeddings into the chosen storage.</li>
            <li>Verify that embeddings are properly stored and retrievable.</li>
            </ol>
        </li>
        </ul>
    </li>
    <li>
        <strong>Modify the llm_adapter and create another function to integrate the context from the vector store into the prompt</strong>
        <ul>
        <li><strong>Step-by-step guide:</strong>
            <ol>
            <li>Extend the functionality of your Python module to include a function for retrieving context from the vector store based on the prompt received.</li>
            <li>Design a strategy for integrating the retrieved context into the prompt, such as appending it to the input message or using it to fine-tune the response.</li>
            <li>Update the llm_adapter module to incorporate the new function and utilize the retrieved context when generating responses.</li>
            <li>Test the modified module with different prompts to ensure that contextual information is effectively utilized in responses.</li>
            </ol>
        </li>
        </ul>
    </li>
    <li>
        <strong>Modify the llm_adapter and create another function to include source and accuracy into the response</strong>
        <ul>
        <li>Enhance your llm_adapter module to include information about the source of the response and its accuracy.</li>
        <li>You may need to modify the response data structure to accommodate this additional information.</li>
        </ul>
    </li>
    <li>
        <strong>Bonus: Integrate to SharePoint and embed the pages into the vector store as well</strong>
        <ul>
        <li>Explore SharePoint APIs to fetch content from SharePoint pages programmatically.</li>
        <li>Extend your vector store to handle embedding of SharePoint pages along with other file types.</li>
        <li>Implement a mechanism to periodically sync SharePoint content with your vector store.</li>
        </ul>
    </li>
    </ol>

    <h2>Additional Considerations</h2>

    <ol>
    <li>
        <strong>User Interface Design</strong>
        <ul>
        <li>Design an intuitive and user-friendly interface for interacting with the chatbot.</li>
        <li>Consider using modern UI frameworks like Material-UI or Ant Design for React to expedite the UI development process.</li>
        </ul>
    </li>
    <li>
        <strong>State Management</strong>
        <ul>
        <li>Decide on a state management solution such as Redux or React Context API to manage application state, especially for handling chat history, uploaded files, and other user interactions.</li>
        </ul>
    </li>
    <li>
        <strong>Authentication and Authorization</strong>
        <ul>
        <li>Implement user authentication mechanisms if needed, especially if the application involves sensitive data or user-specific functionalities.</li>
        <li>You may integrate authentication providers like Firebase Authentication or implement custom authentication logic.</li>
        </ul>
    </li>
    <li>
        <strong>Error Handling</strong>
        <ul>
        <li>Implement robust error handling mechanisms to gracefully handle errors and provide meaningful feedback to users.</li>
        <li>Consider displaying error messages or alerts in the UI for better user experience.</li>
        </ul>
    </li>
    <li>
        <strong>Responsive Design</strong>
        <ul>
        <li>Ensure that the application is responsive and works well across different devices and screen sizes.</li>
        <li>Use CSS frameworks like Bootstrap or Flexbox/Grid for responsive layout design. Material UI is already installed and implemented at some capacity.</li>
        </ul>
    </li>
    <li>
        <strong>Testing</strong>
        <ul>
        <li>Write comprehensive unit tests and integration tests for both frontend and backend components of the application.</li>
        <li>Utilize testing libraries like Jest and React Testing Library for frontend testing, and pytest for backend testing.</li>
        </ul>
    </li>
    <li>
        <strong>Deployment</strong>
        <ul>
        <li>Decide on a deployment strategy for your React application. Options include deploying to platforms like AWS, Heroku, Netlify, or using Docker containers.</li>
        <li>Suggest: Set up CI/CD pipelines for automated testing and deployment.</li>
        </ul>
    </li>
    <li>
        <strong>Accessibility</strong>
        <ul>
        <li>Ensure that your application is accessible to users with disabilities by following accessibility best practices.</li>
        <li>Use semantic HTML elements, provide proper alt text for images, and ensure keyboard navigation is available.</li>
        </ul>
    </li>
    <li>
        <strong>Internationalization and Localization</strong>
        <ul>
        <li>The use of libraries like react-i18next for handling translations and locale-specific content are welcomed.</li>
        </ul>
    </li>
    <li>
        <strong>Documentation</strong>
        <ul>
        <li>Document the installation process, configuration options, and usage instructions for developers who want to contribute or use your application.</li>
        <li>Provide clear and concise documentation for both frontend and backend components.</li>
        </ul>
    </li>
    </ol>
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
