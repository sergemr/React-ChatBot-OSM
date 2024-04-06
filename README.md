# React-ChatBot-OSM

React-ChatBot Open Source Model

- Security & Privacy are the first concerns, please keep in mind to use opensource, locally executable libraries and assets.

- This application uses PHI, GEMMA & LLama-Instruct for the LLM models, they can be downloaded here (you can ask for the file in the office during the CM Hackathon event):

https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF/resolve/main/codellama-7b-instruct.Q4_K_S.gguf

https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_S.gguf

https://huggingface.co/lmstudio-ai/gemma-2b-it-GGUF/resolve/main/gemma-2b-it-q8_0.gguf

- You are encouraged to use different LLMs and experiment with the results

# Rag Architecture

![alt text](https://docs.aws.amazon.com/images/sagemaker/latest/dg/images/jumpstart/jumpstart-fm-rag.jpg)

## Todo list

1. **Integrate a file upload function**

   - Create an interface in your React application for users to upload files.
   - Utilize a library like `react-dropzone` for handling file uploads.
   - Implement backend logic in your Python module to receive and process the uploaded files.

2. **Integrate a Python function to create embeddings for the file**

   - **Step-by-step guide:**
     1. Choose a natural language processing library such as `spaCy` or `gensim` for generating embeddings.
     2. Write a Python function that takes the file content as input and generates embeddings using the chosen library.
     3. Test the function with sample files to ensure proper functionality.
     4. Integrate the function into your backend module to create embeddings for uploaded files.

3. **Save the embeddings into a vector store**

   - **Step-by-step guide:**
     1. Choose a suitable database or storage solution such as MongoDB, SQLite, or Redis for saving embeddings.
     2. Design a schema to store embeddings along with metadata (e.g., file name, timestamp).
     3. Implement logic in your backend module to save the generated embeddings into the chosen storage.
     4. Verify that embeddings are properly stored and retrievable.

4. **Modify the llm_adapter and create another function to integrate the context from the vector store into the prompt**

   - **Step-by-step guide:**
     1. Extend the functionality of your Python module to include a function for retrieving context from the vector store based on the prompt received.
     2. Design a strategy for integrating the retrieved context into the prompt, such as appending it to the input message or using it to fine-tune the response.
     3. Update the llm_adapter module to incorporate the new function and utilize the retrieved context when generating responses.
     4. Test the modified module with different prompts to ensure that contextual information is effectively utilized in responses.

5. **Modify the llm_adapter and create another function to include source and accuracy into the response**

   - Enhance your llm_adapter module to include information about the source of the response and its accuracy.
   - You may need to modify the response data structure to accommodate this additional information.

6. **Bonus: Integrate to SharePoint and embed the pages into the vector store as well**
   - Explore SharePoint APIs to fetch content from SharePoint pages programmatically.
   - Extend your vector store to handle embedding of SharePoint pages along with other file types.
   - Implement a mechanism to periodically sync SharePoint content with your vector store.

## Additional Considerations

1. **User Interface Design**:

   - Design an intuitive and user-friendly interface for interacting with the chatbot.
   - Consider using modern UI frameworks like Material-UI or Ant Design for React to expedite the UI development process.

2. **State Management**:

   - Decide on a state management solution such as Redux or React Context API to manage application state, especially for handling chat history, uploaded files, and other user interactions.

3. **Authentication and Authorization**:

   - Implement user authentication mechanisms if needed, especially if the application involves sensitive data or user-specific functionalities.
   - You may integrate authentication providers like Firebase Authentication or implement custom authentication logic.

4. **Error Handling**:

   - Implement robust error handling mechanisms to gracefully handle errors and provide meaningful feedback to users.
   - Consider displaying error messages or alerts in the UI for better user experience.

5. **Responsive Design**:

   - Ensure that the application is responsive and works well across different devices and screen sizes.
   - Use CSS frameworks like Bootstrap or Flexbox/Grid for responsive layout design. Material UI is already installed and implemented at some capacity.

6. **Testing**:

   - Write comprehensive unit tests and integration tests for both frontend and backend components of the application.
   - Utilize testing libraries like Jest and React Testing Library for frontend testing, and pytest for backend testing.

7. **Deployment**:

   - Decide on a deployment strategy for your React application. Options include deploying to platforms like AWS, Heroku, Netlify, or using Docker containers.
   - Suggest: Set up CI/CD pipelines for automated testing and deployment.

8. **Accessibility**:

   - Ensure that your application is accessible to users with disabilities by following accessibility best practices.
   - Use semantic HTML elements, provide proper alt text for images, and ensure keyboard navigation is available.

9. **Internationalization and Localization**:

   - The use of libraries like react-i18next for handling translations and locale-specific content are welcomed.

10. **Documentation**:
    - Document the installation process, configuration options, and usage instructions for developers who want to contribute or use your application.
    - Provide clear and concise documentation for both frontend and backend components.
