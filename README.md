# Vector Databases Tutorial

Companion notebooks for the vector-databases module of Robert Barcik's GenAI engineering course. The module picks up where the RAG chapter of the previous course ("Intro to GenAI in Python") stops: there you built retrieval by hand with a pandas table; here the table becomes a real store (ChromaDB), then a managed one (Pinecone), then a framework on top (LlamaIndex), then a graph database that a language model fills from plain text (GraphRAG), and finally the security layer around retrieval.

Default model in the notebooks that call OpenAI: `gpt-5.6-luna` (about 0.20 USD per million input tokens); embeddings are Chroma's free local model or `text-embedding-3-small`. A whole module costs cents.

## Modules

| # | Folder | Notebooks | What it covers | Needs |
|---|--------|-----------|----------------|-------|
| 1 | `1. ChromaDB` | [Embeddings and a real vector store](1.%20ChromaDB/1_Creating_Embeddings_using_Chroma.ipynb), [Semantic search and RAG](1.%20ChromaDB/2_Semantic_Search_and_RAG_with_ChromaDB.ipynb), [Chunking and overlap](1.%20ChromaDB/3_Chunking_and_Overlap_with_ChromaDB.ipynb) | Embedding functions, collections, metadata, `where` filters, `query()`, distances, a RAG pipeline with citations, an optional fully local variant; then chunking: the embedding model's token ceiling, a token-window splitter, chunk vectors vs. document vectors in 2D, chunk size and overlap tuned by experiment | OpenAI key (optional in nb 1 and 3) |
| 2 | `2. Pinecone` | Semantic search, Audio similarity, Named entity recognition | A managed vector database: serverless indexes, namespaces, metadata filters, non-text embeddings (audio), NER-based metadata | Pinecone key, GPU helps |
| 3 | `3. LlamaIndex` | LlamaIndex basics, Advanced RAG with metadata extraction | Document loaders, indexes and query engines, LlamaCloud parsing, metadata extractors, response synthesis modes | OpenAI key, LlamaCloud key (nb 7) |
| 4 | `4. Graph_Databases` | [Graph fundamentals with Neo4j](4.%20Graph_Databases/1_graph_fundamentals_neo4j.ipynb), [GraphRAG](4.%20Graph_Databases/2_graphrag_neo4j_llamaindex.ipynb) | Nodes, relationships, Cypher, loading a company graph; a language model extracts entities from text into Neo4j, vector + graph hybrid retrieval | OpenAI key (nb 2), Neo4j (started in Colab, Docker locally) |
| 5 | `5. Securing_RAG` | RAG security | Anonymisation, access-control metadata, prompt constraints, output redaction | OpenAI + Pinecone keys |

The ChromaDB and Graph notebooks are committed **with executed outputs**, so they read like an article before you run a cell. The Pinecone, LlamaIndex and security notebooks need third-party keys and are committed without outputs.

## How to run

### Google Colab (recommended)

Click the "Open in Colab" badge at the top of a notebook. Add your keys as Colab secrets (`OPENAI_API_KEY`, `PINECONE_API_KEY`, `LLAMA_CLOUD_API_KEY` as needed) or paste them when prompted. Data files are fetched from this repository automatically. The Graph notebooks install and start Neo4j inside the Colab runtime (about a minute).

### Local Python

Python 3.10 or newer. One `requirements.txt` covers the whole course (tested on 3.12 and 3.14, September 2026); the install is large because of PyTorch.

```bash
python3 -m venv vectordb_env && source vectordb_env/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."
jupyter notebook
```

For module 4 start Neo4j in Docker first:

```bash
docker run -d --name neo4j -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password123 neo4j:5.26-community
```

## Notes

- Every notebook looks for keys in this order: Colab secret, environment variable, interactive prompt.
- `openai` stays on the 2.x line because the LlamaIndex OpenAI integrations require it; the Responses API and `gpt-5.6-luna` work the same there.
- Library versions, model names and deprecation dates were checked in September 2026. They age; the pins in `requirements.txt` are the tested combination.
