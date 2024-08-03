import ollama

# Initialize the chat stream with a specific model
stream = ollama.chat(model="mistral")

# Debug: Print the type and content of the stream object
print("Stream type:", type(stream))
print("Stream content:", stream)

