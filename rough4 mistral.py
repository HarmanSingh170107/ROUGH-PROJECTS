import ollama

# Initialize the chat stream with a specific model
stream = ollama.chat(model="mistral")
stream = ollama.chat(model="mistral")

# Debug: Print the type and content of the stream object
print("Stream type:", type(stream))
print("Stream content:", stream)

print("Hello from your branch")
print("Hello from the main branch")