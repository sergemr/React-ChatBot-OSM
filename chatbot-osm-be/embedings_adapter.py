from llama_index.core.vector_stores import VectorStoreQuery
from llama_index.core.schema import TextNode
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.postgres import PGVectorStore
from sqlalchemy import make_url
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import numpy as np
import spacy
import psycopg2
from pathlib import Path
from llama_index.readers.file import PyMuPDFReader
from llama_index.core.schema import NodeWithScore
from typing import Optional
from llama_cpp import Llama
from llama_index.core import QueryBundle
from llama_index.core.retrievers import BaseRetriever
from typing import Any, List

from llama_index.core.query_engine import RetrieverQueryEngine
from retriever import VectorDBRetriever


nlp = spacy.load("en_core_web_md")

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

# model_url = "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q4_0.bin"
model_url = "./llm-gemma.gguf"

llm = LlamaCPP(
    # You can pass in the URL to a GGML model to download it automatically
    # model_url=model_url,
    model_path="./llama-2-13b-chat.gguf",
    # optionally, you can set the path to a pre-downloaded model instead of model_url
    # model_path=None,
    temperature=0.1,
    max_new_tokens=256,
    # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
    context_window=3900,
    # kwargs to pass to __call__()
    generate_kwargs={},
    # kwargs to pass to __init__()
    # set to at least 1 to use GPU

    model_kwargs={"n_gpu_layers": 1},
    verbose=True,
)

db_name = "vector_db"
host = "localhost"
password = "1234"
port = "5432"
user = "postgres"
# conn = psycopg2.connect(connection_string)
conn = psycopg2.connect(
    dbname="postgres",
    host=host,
    password=password,
    port=port,
    user=user,
)
conn.autocommit = True

with conn.cursor() as c:
    c.execute(f"REVOKE CONNECT ON DATABASE {db_name} FROM public ")
    c.execute(f"DROP DATABASE IF EXISTS {db_name} WITH (FORCE)")
    c.execute(f"CREATE DATABASE {db_name}")

vector_store = PGVectorStore.from_params(
    database=db_name,
    host=host,
    password=password,
    port=port,
    user=user,
    table_name="llama2_paper",
    embed_dim=384,  # openai embedding dimension
)
text_parser = SentenceSplitter(
    chunk_size=1024,
    # separator=" ",
)


def create_pipeline():

    # loader = PyMuPDFReader()
    # documents = loader.load(file_path="./data/page162.pdf")
    # text_chunks = []
    # maintain relationship with source doc index, to help inject doc metadata in (3)
    doc_idxs = []

    file_path = "./data/page16.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Split text into chunks (for simulation)
    text_chunks = text.split("\n")
    nodes = []

    # Split text into chunks (for simulation)
    text_chunks = text.split("\n")
    nodes = []

    # Create TextNode objects for each text chunk
    for text_chunk in text_chunks:
        node = TextNode(text=text_chunk)
        nodes.append(node)

    # Print the extracted text chunks
    # for idx, node in enumerate(nodes):
        # print(f"Text extracted from chunk {idx + 1}:")
        # print(node.text)

    for node in nodes:
        node_embedding = embed_model.get_text_embedding(
            node.get_content(metadata_mode="all")
        )
        node.embedding = node_embedding
        # print("Node embedding:")
        # print(node.text)

    vector_store.add(nodes)
    print("vector_store")
    print(vector_store)


def query_embedding():
    query_str = "Who is Xmi?"
    query_embedding = embed_model.get_query_embedding(query_str)

    # construct vector store query
    query_mode = "default"
    # query_mode = "sparse"
    # query_mode = "hybrid"

    vector_store_query = VectorStoreQuery(
        query_embedding=query_embedding,    similarity_top_k=2, mode=query_mode
    )

    # returns a VectorStoreQueryResult
    query_result = vector_store.query(vector_store_query)
    print("query_result.nodes[0] !")
    print(query_result.nodes[0])
    print("query_result.nodes[0].get_content()@ ")
    print(query_result.nodes[0].get_content())
    print("query_result.nodes[0].get_content()!!!!")
    print(query_result)

    nodes_with_scores = []
    for index, node in enumerate(query_result.nodes):
        score: Optional[float] = None
        if query_result.similarities is not None:
            score = query_result.similarities[index]
        nodes_with_scores.append(NodeWithScore(node=node, score=score))

    retriever = VectorDBRetriever(
        vector_store, embed_model, query_mode="default", similarity_top_k=2
    )
    query_engine = RetrieverQueryEngine.from_args(retriever, llm=llm)
    print("query_engine")

    query_str = "What is the force?"
    print("query_engine query_engine", retriever)
    # response = query_engine.query(query_str)
    print("query_engine the force1")
    print("query_engine the query_str")
    print(query_str)

    print("query_engine the force response")

    print("str(response)")
    # print(str(response))


def create_embedings():
    create_pipeline()
    query_embedding()
    # Save embeddings to vector store
    # print_to_vector_store(embeddings)
    # save_to_vector_store(embeddings)
    print('DONE!!   ')
    return {'message': 'Embeddings successful'}, 200


create_embedings()
