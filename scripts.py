import os
import re
import collections
import socket

# Define file paths
data_dir = "/home/data"
output_file = "/home/data/output/result.txt"
file1_path = os.path.join(data_dir, "IF-1.txt")  # Path for first text file
file2_path = os.path.join(data_dir, "AlwaysRememberUsThisWay-1.txt")  # Path for second text file

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Function to read and clean text from a file
def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read().lower()  # Convert text to lowercase for uniform processing
    return text

# Function to expand common English contractions
def expand_contractions(text):
    contractions = {
        "i'm": "i am", "can't": "cannot", "don't": "do not", "it's": "it is",
        "won't": "will not", "you're": "you are", "isn't": "is not"
    }
    for contraction, expansion in contractions.items():
        text = text.replace(contraction, expansion)
    return text

# Function to count words and return both total count and word frequency
def count_words(text):
    words = re.findall(r"\b\w+\b", text)  # Extract words using regex
    return len(words), collections.Counter(words)  # Return word count and frequency dictionary

# Read text from both files
text1 = read_file(file1_path)
text2 = read_file(file2_path)

# Count words in IF-1.txt
count1, freq1 = count_words(text1)

# Expand contractions and count words in AlwaysRememberUsThisWay-1.txt
count2, freq2 = count_words(expand_contractions(text2))

# Compute the grand total of words across both files
grand_total = count1 + count2

# Get the top 3 most common words from each file
top3_file1 = freq1.most_common(3)
top3_file2 = freq2.most_common(3)

# Retrieve the container's IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Prepare the output text
output_text = (
    f"Total words in IF-1.txt: {count1}\n"
    f"Total words in AlwaysRememberUsThisWay-1.txt: {count2}\n"
    f"Grand total words: {grand_total}\n\n"
    f"Top 3 words in IF-1.txt: {top3_file1}\n"
    f"Top 3 words in AlwaysRememberUsThisWay-1.txt: {top3_file2}\n\n"
    f"Container IP Address: {ip_address}\n"
)

# Write the results to the output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(output_text)

# Print results to the console
print(output_text)
