from collections import Counter
import csv

def count_top_words(text_file, output_csv, top_n=30):
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read().lower().split()

    word_counts = Counter(text).most_common(top_n)
    
    # Save the top 30 words and their counts into a CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count'])
        writer.writerows(word_counts)

# Define input text file and output CSV file
text_file = 'combined_texts.txt'
output_csv = 'top_30_words.csv'

# Count the top 30 words
count_top_words(text_file, output_csv)
