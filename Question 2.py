import string
from collections import Counter

def get_top_words(file_path):
    # Read the content of the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()

    # Split the text into words
    words = text.split()

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Get the top 30 most common words
    top_words = word_counts.most_common(30)

    return top_words

# Replace 'your_file.txt' with the path to your text file
file_path = r'C:\Users\prgnp\OneDrive\Desktop\python_Project\Output_Text.txt'
top_words = get_top_words(file_path)

# Print the top 30 most common words
for word, count in top_words:
    print(f"{word}: {count}")