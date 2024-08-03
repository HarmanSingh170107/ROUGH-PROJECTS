import matplotlib.pyplot as plt

# Define the text and font properties
text = "Hello, Harman!"
font_properties = {'family': 'sans-serif', 'weight': 'bold', 'size': 50}

# Create a plot to display the text
plt.figure(figsize=(10, 4))
plt.text(0.5, 0.5, text, fontdict=font_properties, horizontalalignment='center', verticalalignment='center')

# Hide axes
plt.axis('off')

# Show the plot
plt.show()
