import ollama

# Initialize the chat stream with a specific model
<<<<<<< HEAD
stream = ollama.chat(model="mistral","")
=======
stream = ollama.chat(model="mistral")
>>>>>>> cdb31c71806c055cfab1e09d2c9cdba0c908da89

# Debug: Print the type and content of the stream object
print("Stream type:", type(stream))
print("Stream content:", stream)

