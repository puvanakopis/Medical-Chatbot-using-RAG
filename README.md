# 🩺 Medical Chatbot using RAG  

This project is a **Medical Assistant Chatbot** built using **Flask, Pinecone, LangChain, HuggingFace Embeddings, and Google Gemini**.  
It uses **Retrieval-Augmented Generation (RAG)** to provide concise answers based on a knowledge base (medical PDFs).  

---

## 📂 Project Structure  

```
├── data/                 
├── src/
│   ├── helper.py
│   ├── prompt.py         
├── static/
│   ├── style.css
├── templates/
│   ├── chat.html         
├── app.py                
├── store_index.py        
├── requirements.txt       
├── setup.py               
├── .env                   
└── README.md              
```

---

## ⚙️ Requirements  

- Python **3.9+**
- Virtual environment (`venv`)
- Accounts & API keys for:
  - **Pinecone**
  - **Google Gemini API**

---

## 🔑 Environment Variables  

Create a `.env` file in the project root with the following:  

```ini
PINECONE_API_KEY=your_pinecone_api_key
GEMINI_API_KEY=your_gemini_api_key
```

---

## 🚀 Installation & Setup  

1. **Clone the repository**  

```bash
git clone https://github.com/puvanakopis/Medical-Chatbot-using-RAG.git
cd Medical-Chatbot-using-RAG
```

2. **Create virtual environment & activate it**  

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**  

```bash
pip install -r requirements.txt
```

---

## 📑 Build the Vector Index  

Before running the chatbot, index your medical PDFs into Pinecone:  

```bash
python store_index.py
```

This will:  
- Load PDFs from `data/`  
- Split them into chunks  
- Generate embeddings using HuggingFace  
- Store them in a Pinecone index (`medical-chatbot`)  

---

## 💬 Run the Chatbot  

Start the Flask server:  

```bash
python app.py
```

By default, it runs at:  
👉 http://localhost:8080  

---

## 🖥️ Chatbot UI  

- The chatbot uses **chat.html** (under `templates/`) for frontend  
- Styled with **static/style.css**  
- You can ask medical-related questions based on the uploaded PDF (`Medical_book.pdf`)  

---

## 🔍 Example Workflow  

1. Upload your medical book in `data/`  
2. Run `store_index.py` to index it  
3. Start `app.py`  
4. Open browser at `http://localhost:8080`  
5. Ask your medical questions  

---

## 📌 Notes  

- The chatbot gives concise answers in **max 3 sentences**  
- If it doesn’t know the answer, it replies: *"I don’t know."*  
- Supports multiple PDFs if added to the `data/` folder  
