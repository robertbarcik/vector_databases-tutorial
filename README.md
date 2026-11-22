# Vector Databases Tutorial

Companion notebooks for the vector-databases module of Robert Barcik's GenAI engineering course. The module picks up where the RAG chapter of the previous course stops: there you built retrieval by hand with a pandas table; here the table becomes a real store (ChromaDB), then a managed one in the cloud with hybrid search and reranking (Pinecone), then a framework on top and the problem of getting text out of real documents (LlamaIndex, LlamaParse), then a graph database that a language model fills from plain text (GraphRAG), and finally the security layers around retrieval.

Default model in the notebooks that call OpenAI: `gpt-6-luna` (about 0.10 USD per million input tokens); embeddings are Chroma's free local model, `text-embedding-3-small`, or a model hosted by Pinecone. A whole module costs cents.

## Modules

| # | Folder | Notebooks | What it covers | Needs |
|---|--------|-----------|----------------|-------|
| 1 | `1. ChromaDB` | [Embeddings and a real vector store](1.%20ChromaDB/1_Creating_Embeddings_using_Chroma.ipynb), [Semantic search and RAG](1.%20ChromaDB/2_Semantic_Search_and_RAG_with_ChromaDB.ipynb), [Chunking and overlap](1.%20ChromaDB/3_Chunking_and_Overlap_with_ChromaDB.ipynb) | Embedding functions, collections, how an index keeps the search fast (built by hand in fifteen lines), metadata, `where` filters, `query()`, distances, a RAG pipeline with citations, an optional fully local variant; then chunking: the embedding model's token ceiling, a token-window splitter, chunk size and overlap tuned by experiment | OpenAI key (optional in nb 1 and 3) |
| 2 | `2. Pinecone` | [A managed vector database](2.%20Pinecone/1_Managed_Vector_Database_Pinecone.ipynb) | An index in the cloud with embedding done on the server, namespaces, filters, keyword search next to semantic search, hybrid search with reciprocal rank fusion, reranking | Pinecone key (free plan) |
| 3 | `3. LlamaIndex` | [RAG in five lines, and document parsing](3.%20LlamaIndex/1_LlamaIndex_RAG_and_Document_Parsing.ipynb) | The RAG pipeline as a framework, nodes and source nodes, a table question that a plain PDF reader gets wrong, LlamaParse, the index stored in Chroma, metadata written by the model | OpenAI key; LlamaCloud key optional |
| 4 | `4. Graph_Databases` | [Graph fundamentals with Neo4j](4.%20Graph_Databases/1_graph_fundamentals_neo4j.ipynb), [GraphRAG](4.%20Graph_Databases/2_graphrag_neo4j.ipynb) | Nodes, relationships, Cypher, loading a company graph; a language model extracts entities from text into Neo4j; one question answered by vectors, by the graph, and by both | OpenAI key (nb 2), Neo4j (started in Colab, Docker locally) |
| 5 | `5. Securing_RAG` | [Securing RAG](5.%20Securing_RAG/1_Securing_RAG.ipynb) | Three ways a RAG assistant leaks and the defence for each: pseudonymisation before embedding, access filters built from the user, retrieved text treated as untrusted, a last check on the answer | OpenAI key |

All notebooks are committed **with executed outputs**, so they read like an article before you run a cell.

## How the notebooks are organised

- **Numbered sections follow the videos.** A heading such as `## 2.2 Meaning or keywords? Hybrid search` is one video of the course (chapter 2, video 2). Read and run these top to bottom; this is the path for everyone.
- **`🛠️ Developer corner` sections are optional.** They hold the more technical material: changing rows, other embedding models, a local model, filters and free-plan limits in Pinecone, storing a LlamaIndex index in Chroma, drawing a graph, a measured prompt-injection test. They have no video, open collapsed in Colab, and nothing outside a corner depends on them.

| Chapter | Videos (= numbered sections) |
|---|---|
| 1 ChromaDB | 1.1 Embeddings and a collection · 1.2 How the search stays fast: the index · 1.3 Metadata and filters · 1.4 Search by meaning · 1.5 RAG on top of the store · 1.6 Chunking · 1.7 Chunk size and overlap |
| 2 Pinecone | 2.1 A database as a service · 2.2 Meaning or keywords? Hybrid search · 2.3 Reranking · 2.4 Which database when |
| 3 LlamaIndex | 3.1 RAG in five lines, and what is inside them · 3.2 Parsing sets the ceiling |
| 4 Graph databases | 4.1 Graphs: nodes, relationships and Cypher · 4.2 A company graph · 4.3 GraphRAG: a language model builds the graph · 4.4 One question, three ways |
| 5 Securing RAG | 5.1 A naive assistant and its first leak · 5.2 The wrong customer's tickets · 5.3 A ticket that lies, and all layers together |

## How to run

### Google Colab (recommended)

Click the "Open in Colab" badge at the top of a notebook. Add your keys as Colab secrets (`OPENAI_API_KEY`, `PINECONE_API_KEY`, `LLAMA_CLOUD_API_KEY` as needed) or paste them when prompted. The first time a notebook reads a secret, Colab asks you to grant access; click **Grant access**. Data files are fetched from this repository automatically. The Graph notebooks install and start Neo4j inside the Colab runtime (about a minute).

### Local Python

Python 3.12 or newer. One `requirements.txt` covers the whole course (tested on 3.13, November 2026); the install is large because of PyTorch.

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

## Sharing one key in a workshop

The notebooks are built so that a whole room can run them on keys handed out by the trainer.

- **Pinecone:** everybody works in one shared index (`vdb-course`, created by whoever runs the notebook first) and in a private namespace with a random name. The clean-up cell deletes only your own namespace, never the index.
- **LlamaCloud:** parsing needs no names that could collide, and a parsed file is cached by the service. If the key has no credits left or the service is busy, the notebook uses a parsed copy of the document from this repository.
- **OpenAI:** nothing is shared between users.

## Notes

- Every notebook looks for keys in this order: Colab secret, environment variable, interactive prompt.
- Library versions, model names and prices were checked in November 2026. They age; the pins in `requirements.txt` are the tested combination.
