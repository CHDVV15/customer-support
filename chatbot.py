import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

from utils import clean_text


class CustomerSupportChatbot:
    def __init__(self):
        # Load FAQ dataset
        self.data = pd.read_csv("data/cleaned_faq.csv")

        # Load embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # Load FAISS index
        self.index = faiss.read_index("model/faq_index.faiss")

        # Confidence threshold for escalation
        self.threshold = 0.60

    def get_response(self, user_question):
        """
        Returns the most relevant answer for a user's question.
        Escalates to human support if confidence is too low.
        """

        # Clean user input
        cleaned_question = clean_text(user_question)

        # Generate embedding
        embedding = self.model.encode(
            [cleaned_question],
            convert_to_numpy=True
        ).astype("float32")

        # Search FAISS index
        distances, indices = self.index.search(embedding, 1)

        distance = float(distances[0][0])
        faq_index = int(indices[0][0])

        # Convert distance to confidence score
        confidence = 1 / (1 + distance)

        # Escalate if confidence is low
        if confidence < self.threshold:
            return {
                "status": "escalate",
                "answer": (
                    "I'm sorry, I couldn't confidently answer your question.\n\n"
                    "Please contact our customer support team for further assistance."
                )
            }

        # Safety check
        if faq_index < 0 or faq_index >= len(self.data):
            return {
                "status": "error",
                "answer": (
                    "Sorry, something went wrong while processing your request."
                )
            }

        # Retrieve answer
        answer = self.data.iloc[faq_index]["answer"]

        return {
            "status": "success",
            "answer": answer
        }


if __name__ == "__main__":
    chatbot = CustomerSupportChatbot()

    print("=" * 50)
    print(" AI Customer Support Chatbot ")
    print("=" * 50)
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Thank you for using the chatbot. Goodbye!")
            break

        response = chatbot.get_response(user_input)

        print(f"Bot: {response['answer']}\n")