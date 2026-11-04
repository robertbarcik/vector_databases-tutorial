# vector_databases-tutorial — Vector Databases

Public student repo of the vector-databases module of the GenAI engineering path (registry slug
`vector-databases`, mapping key `vector-databases`). Syncs to the Courses drive folder
`4. Vector Databases (SYNCED)/course_materials (shared)` via `drive-push` (root files:
`requirements.txt`, `0_vector_databases_intro.pptx`, `README.md`; the five module folders).
Low-priority module; Robert's framing: it boils down to ChromaDB and the GraphRAG demo.

## Layout

| Folder | Notebooks | State |
|---|---|---|
| `1. ChromaDB` | embeddings, semantic search + RAG, chunking and overlap | executed with outputs |
| `2. Pinecone` | semantic search, audio similarity, named entity recognition | unexecuted (no Pinecone key on the machine; free tier is us-east-1 only) |
| `3. LlamaIndex` | basics, advanced RAG with metadata extraction | unexecuted (no LlamaCloud key) |
| `4. Graph_Databases` | graph fundamentals with Neo4j, GraphRAG (entities → Neo4j + Chroma hybrid) | executed with outputs |
| `5. Securing_RAG` | RAG security | unexecuted |

`0_vector_databases_intro.pptx` (7 slides, Slovak notes) is edited by Robert on Drive; pull
before pushing. `recordings/` (July 2026 filming material) is gitignored and describes the OLD
notebooks; regenerate before filming. Lecture notes:
`training-ops/filming/vector-databases/LECTURE_NOTES_2026-09.md`, never in this repo.

## Conventions

- **`openai==2.28.0` on purpose**: `llama-index-llms-openai` 0.8.1 requires `openai<3`. Luna and
  the Responses API work on 2.x. Do not "harmonise" to the 3.x pin of the sibling courses.
- Default model `gpt-5.6-luna`; embeddings are Chroma's free local model or
  `text-embedding-3-small`. Prices in prose as "0.20 USD", never "$0.20".
- **GraphRAG has no LlamaIndex any more** (Pydantic + `responses.parse`, plain Chroma). The old
  version silently ran a MockLLM (`Settings.llm = None`); see PAST_MISTAKES 2026-09-13.
- Neo4j: locally `docker run -d --name neo4j -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password123 neo4j:5.26-community`;
  in Colab the notebook installs tarball 5.26.30 + Java 17 (verified in an Ubuntu 22.04
  container, not in Colab itself). The install cell is skipped outside Colab.
- Executed notebooks (ChromaDB, Graph) stay executed with outputs + Colab badge (hub
  convention); the others stay blank. Data files are fetched from GitHub raw inside the
  notebooks so Colab runs without a clone.
- Classroom voice rules: `ADK-tutorial/CLAUDE.md`.

## Refresh outputs

```
set -a; . ~/.config/training-ops/openai.env; set +a
.venv/bin/jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=1800 "<folder>/<notebook>.ipynb"
```

`.venv` is Python 3.12 with `requirements.txt` (large: PyTorch). Module 4 needs the Neo4j
container running. After executing: read every output against its prose, grep the .ipynb for
local paths and keys, then `drive-push --status`, dry-run, `--apply` after Robert confirms, and
list the Drive folder.

## Open (as of 2026-11-04)

Open the rebuilt notebooks once in Colab with a fresh runtime; the Pinecone notebooks have not
been re-run since the 2026-09 refresh; check whether the old `vector_database_intuition.pptx`
still sits unmapped on Drive.
