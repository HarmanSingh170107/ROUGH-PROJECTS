import ollama

# Initialize the chat stream with a specific model
stream = ollama.chat(model="mistral",

                     messages=[{"role":"user","content":"What is the capital of France?"}])

def ask_question(question):
    # Send a question to the chat model
    stream.send(question)
    
    # Retrieve the response from the chat model
    response = stream.receive()
    
    # Print the response
    print("Response:", response)

# Ask a question
question = "What is the capital of France?"
print("Question:", question)
ask_question(question)
