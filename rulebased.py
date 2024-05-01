import os
import spacy
import json
import re

# Define the entities and their values
entities_values = {
    "CONCEPT": ["Data Science", "Machine Learning", "Deep Learning", "Artificial Intelligence", "Big Data", "Data Mining", "Data Analysis", "Statistical Analysis"],
    "CODING LANGUAGES": ["Python", "R", "SQL"],
    "FRAMEWORKS": ["TensorFlow", "PyTorch", "Scikit-learn"],
    "TOOLS": ["Jupyter Notebook", "Anaconda", "Git", "Docker", "AWS", "Azure", "Google Cloud Platform"],
    "DATABASES": ["MySQL", "PostgreSQL", "MongoDB", "SQLite"],
    "VISUALIZATION TOOLS": ["Matplotlib", "Seaborn", "Plotly", "Tableau"],
    "EXPERIENCE": ["0-2 years", "2-5 years", "5+ years"],
    "DEGREE": ["Computer Science", "Statistics", "Mathematics", "Data Science", "Engineering"],
    "CERTIFICATIONS": ["Data Science Certification", "Machine Learning Certification", "AWS Certification", "Azure Certification"],
    "SOFT SKILLS": ["Analytical Thinking", "Problem-solving", "Communication", "Teamwork"],
    "DOMAIN KNOWLEDGE": ["Finance", "Healthcare", "E-commerce", "Marketing"],
    "PROJECTS": ["Predictive Modeling", "Natural Language Processing", "Computer Vision", "Time Series Analysis"],
    "PUBLICATIONS": ["Research Papers", "Conference Presentations", "Technical Blog Posts"]
}

# Regular expression for experience levels
experience_pattern = r"\b(\d+\s*(?:years|yrs?))\b"

# Load a blank English model
nlp = spacy.blank("en")

# Define the entity recognizer with the ner pipeline component
ner = nlp.add_pipe("ner")

# Initialize the named entity recognition component
print(lambda: [[label, None] for label in entities_values])
print(lambda: [(label, None) for label in entities_values])
ner.initialize(lambda: [[label, None] for label in entities_values])

# Add the labels to the entity recognizer
for label, values in entities_values.items():
    ner.add_label(label)

# Path to the directory containing sample data
sample_data_dir = r"sample data"

# Define a list to store annotated data
annotated_data = []

# Process each file in the sample data directory
for file_name in os.listdir(sample_data_dir):
    # Read the text from the file
    with open(os.path.join(sample_data_dir, file_name), "r") as file:
        text = file.read()
    
    # Create a Doc object from the text
    doc = nlp(text)
    
    # Extract annotated entities and store in JSON format
    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "start_char": ent.start_char,
            "end_char": ent.end_char,
            "label": ent.label_
        })
    
    # Add experience levels extracted using regular expression
    for match in re.finditer(experience_pattern, text):
        entities.append({
            "text": match.group(1),
            "start_char": match.start(),
            "end_char": match.end(),
            "label": "EXPERIENCE"
        })
    
    annotated_data.append({"text": text, "entities": entities})

# Save the annotated data to a JSON file
output_file = "annotated_data.json"
with open(output_file, "w") as f:
    json.dump(annotated_data, f, indent=4)

print(f"Annotated data saved to {output_file}")
