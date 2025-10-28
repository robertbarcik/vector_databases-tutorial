# ChromaDB Tutorial - Testing Guide

## ✅ CORRECT CONFIGURATION (Final)

### Package Versions
```
chromadb==0.5.3
openai==0.28.1  
sentence-transformers==3.0.1
```

## 🧪 How to Test in Google Colab

### Step 1: Install
```python
!pip install -q chromadb==0.5.3 openai==0.28.1 sentence-transformers==3.0.1
```
**Then: Runtime → Restart runtime** ⚠️

### Step 2: Import (after restart)
```python
import os
import chromadb
from chromadb.utils import embedding_functions
```
✅ **Should work** without AttributeError about np.float_

### Step 3: Configure API Key
```python
try:
    from google.colab import userdata
    OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')
    print("✅ API key loaded from Colab secrets")
except:
    from getpass import getpass
    OPENAI_API_KEY = getpass("Enter your OpenAI API Key: ")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
print("✅ Authentication configured!")
```
✅ **Should work** and print success message

### Step 4: Create Embedding Function
```python
openai_embedding_function = embedding_functions.OpenAIEmbeddingFunction(
    model_name="text-embedding-3-small",
    api_key=OPENAI_API_KEY
)
```
✅ **Should work** without TypeError about 'proxies'

## ❌ Common Errors (Now Fixed)

| Error | Cause | Fix |
|-------|-------|-----|
| `AttributeError: np.float_` | chromadb 0.4.x with NumPy 2.0 | Use chromadb 0.5.3 ✅ |
| `TypeError: 'proxies'` | openai 1.x with chromadb | Use openai 0.28.1 ✅ |
| `ImportError: OpenAI` | Importing OpenAI class from 0.28.1 | Don't import it ✅ |

## 🎯 Why This Works

1. **chromadb 0.5.3**: Compatible with NumPy 2.0+ (Colab's default)
2. **openai 0.28.1**: Old API that chromadb expects (no 'proxies' argument)
3. **No OpenAI class import**: Use only embedding_functions

## 📋 Updated Files
- ✅ `1_Creating_Embeddings_using_Chroma.ipynb`
- ✅ `2.Semantic_Search_and_RAG_with_ChromaDB.ipynb`
- ✅ `requirements_chromadb.txt`
