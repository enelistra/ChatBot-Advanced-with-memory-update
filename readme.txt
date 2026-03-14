SaaS AI ChatBot - Advanced with Memory (RAG)
==============================================

A professional, multi-tenant SaaS ChatBot system designed for businesses to provide AI-powered customer support using their proprietary knowledge. Built with a Retrieval-Augmented Generation (RAG) architecture, it ensures high accuracy by grounding LLM responses in company-specific documents.

ARCHITECTURE OVERVIEW
---------------------

The system follows a modern RAG pipeline where company data is processed into searchable vectors:
1. Company Document (.txt) -> Django Signal -> Text Splitting & Chunking
2. Text Chunks -> Sentence-Transformers Embedding -> FAISS Vector Index
3. User Message -> Query Embedding -> FAISS Search -> Top K Chunks
4. Context Assembly -> Google Gemini LLM -> Final Response

KEY FEATURES
------------

- Multi-Tenant Data Isolation: Separate FAISS indices and storage paths for every company code.
- Real-time Indexing: Automated vector synchronization via Django Signals when documents are updated.
- Smart RAG Pipeline: Intelligent text splitting with overlap and semantic search.
- LLM Context Injection: Dynamic prompt engineering with fallback logic.
- Admin Dashboard: Manage companies, API tokens, and Gemini configurations.

TECHNOLOGY STACK
----------------

- Backend: Django
- API: Django REST Framework
- Embeddings: Sentence-Transformers (all-MiniLM-L6-v2)
- Vector Engine: FAISS
- LLM: Google Gemini (gemini-2.0-flash)
- Storage: SQLite + Local Filesystem

PROJECT STRUCTURE
-----------------

- chatapp/: Core AI logic (FAISS engine, Gemini integration, etc.)
- companies/: Tenant and configuration management
- data/: Storage for uploads (txt/) and vectors (vectors/)
- chatbot/: Project configuration
- manage.py: Entry point

SETUP & INSTALLATION
--------------------

Prerequisites:
- Python 3.9 or higher
- Google AI Studio API Key

1. Environment Preparation:
   python -m venv venv
   venv\Scripts\activate (Windows)
   pip install django djangorestframework django-cors-headers faiss-cpu sentence-transformers google-generativeai numpy

2. Deployment Steps:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver

ADMINISTRATIVE WORKFLOW
-----------------------

1. Configure Gemini:
   - Go to http://127.0.0.1:8000/admin/
   - Add Gemini Config with your API Key and model "gemini-2.0-flash".

2. Onboard a New Client:
   - Add a new Company in Admin.
   - Upload document, define Code and API Token.
   - Vector files are created in data/vectors/ automatically.

API REFERENCE
-------------

Endpoint: POST /api/chat/

Payload Example:
{
  "company_code": "ALG01",
  "api_token": "your_secure_token",
  "message": "What is your office address?"
}

AUTHORS & LICENSE
-----------------

- Developed by: Algorytham Technologies Pvt. Ltd.
- Maintained for: AI SaaS Solutions.
