# vector_databases-tutorial — Vector Databases

Public student repo of the vector-databases course of the GenAI engineering path on Skillmea
(registry slug `vector-databases`, mapping key `vector-databases`). Syncs to the Courses drive
folder `4. Vector Databases (SYNCED)/course_materials (shared)` via `drive-push` (root files:
`requirements.txt`, `0_vector_databases_intro.pptx`, `README.md`; the five module folders).
Reworked 2026-11-22 before filming (target about 3 hours of video). Enterprise customers also
run these notebooks, always in Colab, sometimes all on keys Robert hands out.

## Heading contract (since 2026-11-22): the notebooks follow the videos

Same contract as `MCP-tutorial`. Robert films only what stays stable (concepts); the very
technical parts are not filmed.

- `## K.V Title` = exactly one video = lecture code `K_V` in the Skillmea tab "Vector Databases"
  (22 lectures: 0_1, 0_2, 1_1 to 1_6, 2_1 to 2_4, 3_1, 3_2, 4_1 to 4_4, 5_1 to 5_3, 6_1).
  Chapter K = module folder K; the six videos of chapter 1 run across its three notebooks.
- `###` = sub-parts and rituals inside a video.
- `## 🛠️ Developer corner: …` = no video, collapsed in Colab (`metadata.colab.collapsed_sections`
  lists the `metadata.id` of the corner heading cells). Tasks inside corners are `**🛠️ Stretch.**`.
- Unnumbered and not videos: `## Setup…`, `## Opening the store`, `## Cleaning up`,
  `## What you take with you`.
- **Two invariants**, tested by `training-ops/filming/vector-databases/build/skip_safety.py`
  (executes a corner-stripped copy of every notebook outside the repo): a corner never defines
  anything the numbered path uses, and Run all works with and without corners.
- Renaming, adding or moving a numbered section means updating the Skillmea tab and the chapter
  table in the README in the same go. When a concept moves, it moves to a corner, never out of
  the notebook. Cross-references use section numbers ("section 2.2") or plain words, never the
  old per-notebook numbers.

## Layout (all notebooks committed executed, with outputs)

| Folder | Notebooks | Built by |
|---|---|---|
| `1. ChromaDB` | embeddings, semantic search + RAG, chunking and overlap | 2026-09 builders are gone; the .ipynb is the source (one-off scripts, latest `restructure_2026_11_22.py`) |
| `2. Pinecone` | `1_Managed_Vector_Database_Pinecone.ipynb` + `articles_400.csv` | `build_pinecone_nb.py`, `make_articles_400.py` |
| `3. LlamaIndex` | `1_LlamaIndex_RAG_and_Document_Parsing.ipynb` + `livestock_poultry.pdf` + `livestock_poultry_parsed.md` | `build_llamaindex_nb.py`, `make_parsed_fallback.py` |
| `4. Graph_Databases` | graph fundamentals with Neo4j, `2_graphrag_neo4j.ipynb` | the .ipynb is the source (same one-off script) |
| `5. Securing_RAG` | `1_Securing_RAG.ipynb` + `support_tickets_raw.jsonl` | `build_security_nb.py` |

Builders live in `training-ops/filming/vector-databases/build/` (never in this repo; `nbkit.py`
holds the shared key cell). **Change a built notebook in its builder, rebuild, re-execute.** A
hand edit of the .ipynb is lost at the next build. Lecture notes and the filming plan:
`training-ops/filming/vector-databases/`.

`0_vector_databases_intro.pptx` (7 slides, Slovak notes) is edited by Robert on Drive; pull
before pushing. `recordings/` (July 2026, gitignored) describes the OLD notebooks.

## Conventions

- Pins (tested together 2026-11-22 on Python 3.13, which is what Colab runs): `chromadb==1.5.9`,
  `pinecone==10.3.0`, `openai==3.51.0`, `llama-index-core==0.14.26` (+ `llms-openai==0.9.0`),
  `llama-cloud==2.19.0`, `neo4j==6.4.1`, `networkx==3.7` (needs Python 3.12+). The `%pip` line of
  every notebook repeats the pins from `requirements.txt`; change both together.
- Default model `gpt-6-luna` (0.10 USD per million input tokens; a reasoning model). Prices in
  prose as "0.10 USD", never "$0.10".
- **Key cell:** every notebook uses `colab_secret()` / `get_key()` from `nbkit.py` (retry loop
  for Colab's "Grant access" dialog, `.strip()`, one test request). Do not simplify it; see
  `MCP-tutorial/CLAUDE.md`, "Colab check", for why.
- **Shared-key rules (workshops):** Pinecone = one shared index `vdb-course` + a random
  namespace per student, clean-up deletes only the own namespace, never the index (free plan: 5
  indexes, 100 namespaces per index, 5M embedding tokens a month per hosted model, 500 rerank
  requests a month). LlamaParse = no names to collide, 5 parse jobs at a time on the free plan,
  parsed files cached 48 h; the notebook falls back to `livestock_poultry_parsed.md`. Verified
  2026-11-22 with five simultaneous runs of the Pinecone notebook on one key.
- Pinecone uses the Documents API (schema with `embed` + `full_text_search` on one text field;
  filter fields are NOT declared in the schema; `embed` and `text` scoring cannot be combined in
  one request, hence the client-side rank fusion).
- GraphRAG has no LlamaIndex (Pydantic + `responses.parse`, plain Chroma). Extraction is not
  deterministic: after a re-run read sections 5 and 6 against the prose.
- Securing RAG: on `gpt-6-luna` crude "ignore your instructions" injections fail even with a
  naive prompt (measured 2026-11-22), so the demo plants a false FACT (fake helpdesk number).
  Re-measure before changing the model.
- Neo4j: locally `docker run -d --name neo4j -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password123 neo4j:5.26-community`;
  in Colab the notebooks install tarball 5.26.30 + Java 17 (verified live in Colab 2026-11-22).
- Data files are fetched from GitHub raw inside the notebooks, so a new data file works in
  Colab only after it is pushed to `main`.
- Classroom voice rules: `ADK-tutorial/CLAUDE.md`.

## Refresh outputs

Keys: `~/.config/training-ops/vector_databases.env` (`OPENAI_API_KEY`, `PINECONE_API_KEY`,
`LLAMA_CLOUD_API_KEY`, EU region). `.venv` is Python 3.13 with `requirements.txt` plus `pip`.

```
set -a; . ~/.config/training-ops/vector_databases.env; set +a
.venv/bin/jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=1800 "<folder>/<notebook>.ipynb"
```

Module 4 needs the Neo4j container running. After executing: read every output against its
prose, grep the .ipynb for local paths and keys, delete the `chroma_db/` folders the notebooks
create (`1. ChromaDB/`, `3. LlamaIndex/`; drive-push syncs the working tree), then
`drive-push --status`, dry-run, `--apply` after Robert confirms, and list the Drive folder.

## Open (as of 2026-11-22)

See `training-ops/filming/vector-databases/FILMING_PLAN_2026-11.md`, section "Still open".
