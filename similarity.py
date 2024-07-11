def get_similarity_score(text:str, model_name:str, dir:str):

    from langchain_community.embeddings import OllamaEmbeddings
    from langchain_community.vectorstores import Chroma

    ollama_emb = OllamaEmbeddings(model=model_name, show_progress=True)
    vectorstore = Chroma(persist_directory=dir, embedding_function=ollama_emb)

    return vectorstore.similarity_search_with_relevance_scores(text)[0][1]

def add_new(text:str, model_name:str, dir:str):
    from langchain_community.embeddings import OllamaEmbeddings
    from langchain_community.vectorstores import Chroma

    ollama_emb = OllamaEmbeddings(model=model_name, show_progress=True)
    Chroma(embedding_function=ollama_emb, persist_directory=dir, collection_metadata={"hnsw:space": "cosine"}).add_texts(texts=[text])

# add_new('NEWS2','all-minilm:33m','./chroma_db')
# add_new('NEWS3','all-minilm:33m','./chroma_db')
# add_new('NEWS4','all-minilm:33m','./chroma_db')
# add_new('NEWS5','all-minilm:33m','./chroma_db')
# add_new('NEWS6','all-minilm:33m','./chroma_db')
# add_new('NEWS7','all-minilm:33m','./chroma_db')
# add_new('NEWS8','all-minilm:33m','./chroma_db')
# add_new('NEWS9','all-minilm:33m','./chroma_db')
# print(get_similarity_score('anime','all-minilm:33m','./chroma_db'))