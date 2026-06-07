from pathlib import Path

folders = [

    # Frontend
    "frontend/public",
    "frontend/src",
    "frontend/src/api",
    "frontend/src/components",
    "frontend/src/pages",
    "frontend/src/hooks",
    "frontend/src/context",

    # Backend
    "backend/core",
    "backend/chatbot",
    "backend/survey",

    # RAG
    "rag",
    "rag/ingestion",
    "rag/retrieval",
    "rag/reranking",
    "rag/memory",
    "rag/rewriting",
    "rag/generation",
    "rag/evaluation",

    # Agents
    "agents",
    "agents/tools",
    "agents/prompts",

    # Database
    "database",
    "database/models",
    "database/migrations",

    # Vectorstore
    "vectorstore",
    "vectorstore/faiss_index",
    "vectorstore/embeddings",
    "vectorstore/metadata",

    # Voice
    "voice",

    # Data
    "data",
    "data/pdfs",
    "data/survey_data",
    "data/uploaded_docs",

    # Docs
    "docs",
    "docs/ppt",
    "docs/screenshots",

    # Tests
    "tests",

    # Deployment
    "deployment"
]

files = [

    # Root
    ".env",
    "README.md",
    "requirements.txt",

    # Frontend
    "frontend/package.json",
    "frontend/vite.config.js",
    "frontend/index.html",

    "frontend/src/App.jsx",
    "frontend/src/main.jsx",

    "frontend/src/api/chatApi.js",

    "frontend/src/components/ChatBox.jsx",
    "frontend/src/components/Message.jsx",
    "frontend/src/components/SourceCard.jsx",
    "frontend/src/components/Navbar.jsx",

    "frontend/src/pages/Home.jsx",
    "frontend/src/pages/Chat.jsx",
    "frontend/src/pages/Survey.jsx",
    "frontend/src/pages/Dashboard.jsx",

    # Backend
    "backend/manage.py",

    "backend/core/__init__.py",
    "backend/core/settings.py",
    "backend/core/urls.py",
    "backend/core/asgi.py",
    "backend/core/wsgi.py",

    "backend/chatbot/__init__.py",
    "backend/chatbot/models.py",
    "backend/chatbot/views.py",
    "backend/chatbot/serializers.py",
    "backend/chatbot/urls.py",

    "backend/survey/__init__.py",
    "backend/survey/models.py",
    "backend/survey/views.py",
    "backend/survey/urls.py",

    # RAG
    "rag/__init__.py",
    "rag/pipeline.py",

    "rag/ingestion/__init__.py",
    "rag/ingestion/pdf_loader.py",
    "rag/ingestion/chunker.py",
    "rag/ingestion/metadata_extractor.py",
    "rag/ingestion/deduplicator.py",

    "rag/retrieval/__init__.py",
    "rag/retrieval/hybrid_retriever.py",
    "rag/retrieval/semantic_retriever.py",
    "rag/retrieval/bm25_retriever.py",
    "rag/retrieval/metadata_filter.py",

    "rag/reranking/__init__.py",
    "rag/reranking/reranker.py",

    "rag/memory/__init__.py",
    "rag/memory/conversation_memory.py",

    "rag/rewriting/__init__.py",
    "rag/rewriting/query_rewriter.py",

    "rag/generation/__init__.py",
    "rag/generation/prompts.py",
    "rag/generation/llm.py",

    "rag/evaluation/__init__.py",
    "rag/evaluation/ragas_eval.py",

    # Agents
    "agents/__init__.py",
    "agents/agent_executor.py",
    "agents/tool_router.py",

    "agents/prompts/__init__.py",
    "agents/prompts/agent_prompt.py",

    "agents/tools/__init__.py",
    "agents/tools/rag_tool.py",
    "agents/tools/web_search_tool.py",
    "agents/tools/db_tool.py",
    "agents/tools/bmi_tool.py",
    "agents/tools/calculator_tool.py",

    # Database
    "database/models/__init__.py",
    "database/models/survey.py",
    "database/models/user.py",
    "database/models/chat_history.py",

    # Voice
    "voice/__init__.py",
    "voice/speech_to_text.py",
    "voice/text_to_speech.py",
    "voice/multilingual_support.py",

    # Docs
    "docs/architecture.png",
    "docs/project_report.docx",

    # Tests
    "tests/test_rag.py",
    "tests/test_agent.py",
    "tests/test_tools.py",
    "tests/test_voice.py",

    # Deployment
    "deployment/Dockerfile",
    "deployment/docker-compose.yml",
    "deployment/render.yaml"
]

# Additional folders

folders.extend([
    "config",
    "logs",
    "cache/embeddings_cache",
    "cache/query_cache",
    "scripts",
    "notebooks"
])

# Additional files

files.extend([
    "config/__init__.py",
    "config/settings.py",
    "config/constants.py",
    "config/prompts.py",
    "config/model_config.py",

    "logs/app.log",
    "logs/rag.log",
    "logs/agent.log",
    "logs/voice.log",
    "logs/errors.log",

    "scripts/build_vectorstore.py",
    "scripts/ingest_pdfs.py",
    "scripts/initialize_db.py",

    "notebooks/experiments.ipynb",
    "notebooks/rag_testing.ipynb",

    ".gitignore"
])

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

for file in files:
    Path(file).parent.mkdir(parents=True, exist_ok=True)
    Path(file).touch(exist_ok=True)
    

print("✅ SmartHealth AI Complete Structure Created Successfully!")