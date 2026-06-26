# 🤖 AI Customer Support Chatbot

An AI-powered Customer Support Chatbot developed using **Natural Language Processing (NLP)** and **Semantic Search**. The chatbot understands customer queries, retrieves the most relevant answer from a custom FAQ database, and escalates queries to human support when necessary.

---

## 📌 Project Overview

Customer support teams often receive a large number of repetitive queries related to accounts, orders, shipping, payments, and refunds. This project automates the process by using semantic similarity instead of simple keyword matching.

The chatbot is capable of understanding different ways users ask the same question and provides accurate responses using Sentence Transformers and FAISS.

---

## 🚀 Features

* Semantic search using Sentence Transformers
* Fast similarity search with FAISS
* Customer support FAQ chatbot
* Human support escalation for unknown queries
* Streamlit-based interactive web application
* Lightweight model suitable for deployment
* Modular and easy-to-understand code structure

---

## 🛠️ Tech Stack

| Component           | Technology            |
| ------------------- | --------------------- |
| Language            | Python                |
| Frontend            | Streamlit             |
| NLP Model           | all-MiniLM-L6-v2      |
| Vector Database     | FAISS                 |
| Data Processing     | Pandas                |
| Numerical Computing | NumPy                 |
| Machine Learning    | Sentence Transformers |
| Version Control     | Git & GitHub          |

---

## 📂 Project Structure

```text
customer_support/
│
├── app.py
├── chatbot.py
├── utils.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── faq.csv
│   └── cleaned_faq.csv
│
├── model/
│   ├── faq_index.faiss
│   └── faq_embeddings.npy
│
├── preprocess.ipynb
├── train.ipynb
│
└── screenshots/
```

---

## ⚙️ Workflow

1. Create a custom FAQ dataset.
2. Preprocess and clean customer queries.
3. Generate sentence embeddings using Sentence Transformers.
4. Store embeddings in a FAISS vector index.
5. Accept user queries through the Streamlit interface.
6. Retrieve the most relevant FAQ.
7. Return the corresponding answer or escalate the query if no suitable match is found.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/customer-support.git
```

Navigate to the project directory:

```bash
cd customer-support
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser automatically.

---

## 📊 Dataset

The chatbot uses a custom FAQ dataset containing customer support questions related to:

* Greetings
* Account Management
* Orders
* Shipping
* Payments
* Returns
* Refunds
* Technical Support
* Contact Information

---

## 📈 Future Enhancements

* Multi-language support
* Voice-based chatbot
* Database integration
* Live chat agent handoff
* Chat history storage
* User authentication
* Analytics dashboard
* REST API integration

---

## 🎯 Learning Outcomes

This project demonstrates:

* Natural Language Processing
* Semantic Search
* Vector Databases
* Information Retrieval
* Streamlit Application Development
* AI Model Deployment
* Software Engineering Best Practices

---

## 👨‍💻 Author

**Srinu Dinesh**

B.Tech Computer Science Engineering

AI & Machine Learning Enthusiast

---

## 📄 License

This project is intended for educational and internship purposes.
