import spacy
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline

# --- SpaCy NER Function ---
def extract_entities_spacy(text_file, model_name='en_core_sci_sm'):
    # Load the SpaCy NER model
    nlp = spacy.load(model_name)
    
    # Read the content of the text file
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Process the text using the SpaCy model
    doc = nlp(text)
    
    # Extract diseases and drugs (you can adjust the labels depending on the entity types)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Return extracted entities
    diseases = [ent for ent, label in entities if label == 'DISEASE']
    drugs = [ent for ent, label in entities if label == 'DRUG']
    
    return diseases, drugs

# --- BioBERT NER Function ---
def extract_entities_biobert(text_file, model_name="dmis-lab/biobert-v1.1"):
    # Load the BioBERT model and tokenizer from Hugging Face
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    
    # Create an NLP pipeline for NER
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    
    # Read the text
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Use the pipeline to perform NER on the text
    ner_results = nlp(text)
    
    # Extract diseases and drugs
    diseases = [result['word'] for result in ner_results if 'DISEASE' in result['entity']]
    drugs = [result['word'] for result in ner_results if 'DRUG' in result['entity']]
    
    return diseases, drugs

# --- Comparison Function ---
def compare_entities(entities_spacy, entities_biobert):
    # Compare SpaCy and BioBERT entities
    spacy_unique = set(entities_spacy) - set(entities_biobert)
    biobert_unique = set(entities_biobert) - set(entities_spacy)
    common_entities = set(entities_spacy) & set(entities_biobert)
    
    return spacy_unique, biobert_unique, common_entities

# --- Main Task 4 Execution ---

# Define the input text file
text_file = 'combined_texts.txt'

# --- Extract entities using SpaCy ---
print("Extracting entities using SpaCy...")
diseases_spacy, drugs_spacy = extract_entities_spacy(text_file)
print(f"SpaCy - Diseases: {diseases_spacy}")
print(f"SpaCy - Drugs: {drugs_spacy}")

# --- Extract entities using BioBERT ---
print("\nExtracting entities using BioBERT...")
diseases_biobert, drugs_biobert = extract_entities_biobert(text_file)
print(f"BioBERT - Diseases: {diseases_biobert}")
print(f"BioBERT - Drugs: {drugs_biobert}")

# --- Compare entities detected by both models ---
print("\nComparing entities detected by SpaCy and BioBERT...")

# Compare diseases
spacy_unique_diseases, biobert_unique_diseases, common_diseases = compare_entities(diseases_spacy, diseases_biobert)
print(f"Unique diseases in SpaCy: {spacy_unique_diseases}")
print(f"Unique diseases in BioBERT: {biobert_unique_diseases}")
print(f"Common diseases: {common_diseases}")

# Compare drugs
spacy_unique_drugs, biobert_unique_drugs, common_drugs = compare_entities(drugs_spacy, drugs_biobert)
print(f"Unique drugs in SpaCy: {spacy_unique_drugs}")
print(f"Unique drugs in BioBERT: {biobert_unique_drugs}")
print(f"Common drugs: {common_drugs}")
