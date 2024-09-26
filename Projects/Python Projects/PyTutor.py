# Beginner python coding tutor chatbot
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

class CodingTutorChatbot:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForQuestionAnswering.from_pretrained(model_name)

    def answer_question(self, question, context):
        inputs = self.tokenizer.encode_plus(question, context, return_tensors="pt")
        outputs = self.model(**inputs)
        
        answer_start = torch.argmax(outputs.start_logits)
        answer_end = torch.argmax(outputs.end_logits) + 1
        
        answer = self.tokenizer.convert_tokens_to_string(
            self.tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end])
        )
        
        return answer

    def chat(self):
        print("Python Coding Tutor: Hello! How can I help you with Python today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Python Coding Tutor: Goodbye! Happy coding!")
                break
            
            # Here, you would typically search for the most relevant context
            # from your dataset based on the user's question.
            context = "Python is a high-level programming language..."  # Placeholder
            
            response = self.answer_question(user_input, context)
            print(f"Python Coding Tutor: {response}")

if __name__ == "__main__":
    chatbot = CodingTutorChatbot("distilbert-base-uncased-distilled-squad")
    chatbot.chat()
    