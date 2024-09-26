import openai
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer, util

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def split_into_sections(text):
    # This is a simple split by newlines. You might want to use a more sophisticated method.
    return text.split("\n\n")

def encode_sections(sections):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model.encode(sections)

def find_most_relevant_section(query, sections, section_embeddings):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode(query)
    
    similarities = util.cos_sim(query_embedding, section_embeddings)[0]
    best_match = similarities.argmax()
    
    return sections[best_match]

def generate_response(query, relevant_section):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on document sections."},
            {"role": "user", "content": f"Based on the following section of a document, answer this question: {query}\n\nDocument section: {relevant_section}"}
        ]
    )
    return response.choices[0].message.content

def main():
    pdf_path = "path/to/your/document.pdf"
    query = "What is the main topic of chapter 3?"
    
    text = extract_text_from_pdf(pdf_path)
    sections = split_into_sections(text)
    section_embeddings = encode_sections(sections)
    
    relevant_section = find_most_relevant_section(query, sections, section_embeddings)
    response = generate_response(query, relevant_section)
    
    print(f"Query: {query}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main()