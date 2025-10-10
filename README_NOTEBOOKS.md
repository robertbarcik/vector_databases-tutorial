# Graph Database & GraphRAG Educational Notebooks

## 📚 Overview

This directory contains two comprehensive educational notebooks for teaching graph databases and GraphRAG (Graph Retrieval-Augmented Generation) in a Generative AI course.

## 📓 Notebook 1: Graph Database Fundamentals with Neo4j

**File:** `graph_fundamentals_neo4j.ipynb`
**Requirements:** `requirements_nb1.txt`

### What Students Learn:
- Core graph database concepts (nodes, relationships, properties)
- Cypher query language for pattern matching
- Building knowledge graphs from structured data
- Graph traversal and pattern matching
- Data visualization with matplotlib and NetworkX
- When to use graph databases vs other data stores

### Structure (7 Parts):
1. **Part 1:** Theory - What Are Graph Databases?
2. **Part 2:** Setup - Installing Neo4j in Google Colab
3. **Part 3:** Cypher Basics - The Graph Query Language
4. **Part 4:** Building a Knowledge Graph
5. **Part 5:** Pattern Matching & Traversal
6. **Part 6:** Visualizing Your Graph (with matplotlib)
7. **Part 7:** Next Steps and Extensions

### Key Features:
- ✅ Runs entirely in Google Colab (no external accounts needed)
- ✅ Real-world company organizational knowledge graph
- ✅ 18 employees, 4 departments, 10 projects, 15 skills
- ✅ Interactive matplotlib visualizations
- ✅ Hands-on Cypher query examples

## 📓 Notebook 2: GraphRAG with Neo4j and LlamaIndex

**File:** `graphrag_neo4j_llamaindex.ipynb`
**Requirements:** `requirements_nb2.txt`

### What Students Learn:
- LLM-powered entity extraction from unstructured text
- Automatic knowledge graph construction
- Vector embeddings for semantic search
- Hybrid retrieval combining graphs and vectors
- Multi-hop reasoning and entity disambiguation
- Production GraphRAG system design

### Structure (12 Parts):
1. **Part 1:** Theory - Understanding GraphRAG
2. **Part 2:** Setup - Installing Dependencies
3. **Part 3:** Loading Sample Documents
4. **Part 4:** LLM-Powered Entity Extraction
5. **Part 5:** Building the Knowledge Graph Automatically
6. **Part 6:** Creating Vector Embeddings
7. **Part 7-8:** Vector Search vs Graph Search
8. **Part 9-10:** Hybrid Search - GraphRAG in Action
9. **Part 11:** Advanced GraphRAG Patterns
10. **Part 12:** Next Steps & Production Considerations

### Key Features:
- ✅ Uses GPT-5-nano for cost-efficient entity extraction
- ✅ LlamaIndex integration for RAG orchestration
- ✅ ChromaDB for vector storage
- ✅ 6 realistic documents with rich entities and relationships
- ✅ Demonstrates vector-only, graph-only, and hybrid search
- ✅ Multi-hop reasoning examples

## 🚀 Getting Started

### Prerequisites:
- Google Colab account (free)
- OpenAI API key (for Notebook 2 only)

### Setup Instructions:

1. **Upload to Google Colab:**
   - Go to https://colab.research.google.com/
   - Click `File → Upload notebook`
   - Select the notebook file

2. **For Notebook 1:**
   - Simply run all cells in order
   - No API keys needed!

3. **For Notebook 2:**
   - Upload `api_keys.txt` with your OpenAI API key
   - Or manually set the API key in the configuration cell
   - Run all cells in order

## 📦 Dependencies

### Notebook 1:
- Neo4j Community Edition 4.4.36 (installed via script)
- Python packages: neo4j, py2neo, pandas, matplotlib, networkx

### Notebook 2:
- All dependencies from Notebook 1, plus:
- OpenAI Python SDK
- LlamaIndex (core + graph stores + vector stores)
- ChromaDB
- LlamaIndex integrations for Neo4j and OpenAI

All dependencies are installed automatically within the notebooks!

## 🎯 Learning Path

**Recommended order:**
1. Complete Notebook 1 first to understand graph database fundamentals
2. Then proceed to Notebook 2 to learn GraphRAG and automation

**Time estimate:**
- Notebook 1: 1-2 hours
- Notebook 2: 2-3 hours

## 📖 Key Concepts Covered

### Graph Database Concepts:
- Nodes, relationships, properties
- Cypher query language
- Pattern matching and traversal
- Index-free adjacency
- Graph modeling best practices

### GraphRAG Concepts:
- Entity extraction with LLMs
- Knowledge graph automation
- Vector embeddings and semantic search
- Hybrid retrieval strategies
- Multi-hop reasoning
- Entity disambiguation

## 🎓 Educational Design

Both notebooks follow educational best practices:
- **Theory first:** Each section starts with conceptual explanations
- **Hands-on examples:** Immediately apply concepts with code
- **Real-world scenarios:** Use realistic business/research contexts
- **Progressive complexity:** Start simple, gradually add sophistication
- **Visual learning:** Include visualizations and diagrams
- **Practice exercises:** Suggested extensions for deeper learning

## 🛠️ Technical Notes

- **Neo4j Installation:** Uses tarball-based installation for Colab compatibility
- **API Model:** Uses OpenAI's `client.responses.create()` format with gpt-5-nano
- **Vector Store:** ChromaDB in ephemeral mode (in-memory for Colab)
- **Graph Store:** Neo4j Community Edition running locally in Colab VM

## ⚠️ Important Notes

1. **Colab Runtime:** Neo4j runs in the Colab VM and resets when runtime restarts
2. **API Costs:** Notebook 2 makes OpenAI API calls - monitor usage
3. **Data Persistence:** All data is ephemeral; nothing is saved between sessions
4. **Neo4j Browser:** Not directly accessible in Colab; use matplotlib visualizations

## 📝 Files in This Directory

- `graph_fundamentals_neo4j.ipynb` - Notebook 1
- `graphrag_neo4j_llamaindex.ipynb` - Notebook 2
- `requirements_nb1.txt` - Dependencies for Notebook 1
- `requirements_nb2.txt` - Dependencies for Notebook 2
- `api_keys.txt` - OpenAI API key (user-provided)
- `CLAUDE.md` - Development instructions
- `README_NOTEBOOKS.md` - This file

## 🎉 Ready to Start!

Both notebooks are complete, tested, and ready for classroom use. Students can run them directly in Google Colab with minimal setup.

Happy teaching! 🚀
