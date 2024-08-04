
def chat():
    speak("Now what do you want to ask from me?")
    # Initialize the chat stream with a specific model
    stream = ollama.chat(model="mistral",messages=[{"role":"user","content":"What is the capital of France?"}])

    # Debug: Print the type and content of the stream object
    print("Stream type:", type(stream))
    print("Stream content:", stream)
