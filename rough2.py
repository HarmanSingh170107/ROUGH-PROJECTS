from ollama import Llama

# Load the model (example, adjust as per actual usage)
model = Llama.load_model('path/to/llama/model')

# Make a request
response = model.generate("Translate the following English text to French: 'Hello, how are you?'")

# Print the response
print(response)