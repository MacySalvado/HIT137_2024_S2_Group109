from transformers import AutoTokenizer
from collections import Counter

def count_unique_tokens(text_file, model_name='bert-base-uncased', top_n=30):
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(text)
    token_counts = Counter(tokens).most_common(top_n)
    
    return token_counts

# Define input text file
text_file = 'combined_texts.txt'

# Count the top 30 unique tokens
top_tokens = count_unique_tokens(text_file)
print(top_tokens)
