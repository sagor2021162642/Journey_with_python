from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text
text = """
Python is a powerful programming language.
It is used in web development, data science, artificial intelligence,
machine learning, and more.
"""

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the generated image
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()