# Contains code snippets for vectorisations from e seller, 

# --------------------- VIEW , ADD , DELETE ----------------------

from IPython.display import display

from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

from langchain.chains import VectorDBQA
from langchain_community.llms import OpenAI


from langchain.chains import RetrievalQAWithSourcesChain
import pandas as pd

import openai
import os
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = "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"

embeddings = OpenAIEmbeddings()

save_directory = "data/merged_vector"
new_db = FAISS.load_local(save_directory, embeddings)

# ---------------------- Display VectorStore -----------------------

# Display Documents in VectorStore
def show_vstore(store):
 vector_df = store_to_df(store)
 display(vector_df)

# Convert VectorStore into df to convenient access
def store_to_df(store):
 v_dict = store.docstore._dict
 data_rows = []
 for k in v_dict.keys():
   doc_name = v_dict[k].metadata['source'].split('/')[-1]
#    page_number = v_dict[k].metadata['page']+1
   content = v_dict[k].page_content
#    data_rows.append({"chunk_id":k, "document":doc_name, "page":page_number, "content":content})
   data_rows.append({"chunk_id":k, "document":doc_name, "content":content})
 vector_df = pd.DataFrame(data_rows)
 return vector_df

def delete_document(store, document):
  vector_df = store_to_df(store)
  chunks_list = vector_df.loc[vector_df['document']==document]['chunk_id'].tolist()
  store.delete(chunks_list)

# ---------------------- END - Display VectorStore - END -----------------------


# ---------- Execution -------------

# delete_document(new_db, "data\\filtered_txts\\artists\\abramovic_marina.txt")

# print(new_db)


# save_directory = "data/merged_vector"
# new_db.save_local(save_directory)

#------------------------------------------------- FRESH CODES -------------------------------------------------------------


def add_to_vector(type, xml_id):

  Merged_Vector_Path = "data/merged_vector"

  loader = DirectoryLoader(f'data/filtered_txts/{type}s', glob=f"./{xml_id}.txt", loader_cls=TextLoader, loader_kwargs=dict(encoding="utf-8"))
  loaded_txt = loader.load()
  text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
  docs = text_splitter.split_documents(loaded_txt)
  embeddings = OpenAIEmbeddings()
  VectorStore = FAISS.from_documents(docs, embeddings)

  Merged_VectorStore = FAISS.load_local(Merged_Vector_Path, embeddings)
  Merged_VectorStore.merge_from(VectorStore)
  Merged_VectorStore.save_local(Merged_Vector_Path)
  print("\n\nAdded to Vector : ",f"data/filtered_txts/{type}s/{xml_id}.txt","\n")


def first_vectorise():
    Merged_Vector_Path = "data/merged_vector"
    
    if not os.path.exists("data/faq"):
        os.makedirs("data/faq")
    
    # if not faq.txt, then create an empty faq.txt 

    loader = DirectoryLoader(f'data/faq', glob=f"./faq.txt", loader_cls=TextLoader, loader_kwargs=dict(encoding="utf-8"))
    document = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    docs = text_splitter.split_documents(document)
    embeddings = OpenAIEmbeddings()
    docs_db = FAISS.from_documents(docs, embeddings)
    docs_db.save_local(Merged_Vector_Path)


#--------- Refresh Dependencies -----------

# Display Documents in VectorStore
def show_vstore(store):
 vector_df = store_to_df(store)
 display(vector_df)

# Convert VectorStore into df to convenient access
def store_to_df(store):
 v_dict = store.docstore._dict
 data_rows = []
 for k in v_dict.keys():
   doc_name = v_dict[k].metadata['source'].split('/')[-1]
#    page_number = v_dict[k].metadata['page']+1  # Page used only when it is pdf
   content = v_dict[k].page_content
#    data_rows.append({"chunk_id":k, "document":doc_name, "page":page_number, "content":content})
   data_rows.append({"chunk_id":k, "document":doc_name, "content":content})
 vector_df = pd.DataFrame(data_rows)
 return vector_df

# Deleting a document from a vectorstore
def delete_document(store, document):
  vector_df = store_to_df(store)
  chunks_list = vector_df.loc[vector_df['document']==document]['chunk_id'].tolist()
  store.delete(chunks_list)

#-----------------------------------------

def refresh_vector(type, xml_id):
  Merged_Vector_Path = "data/merged_vector"
  embeddings = OpenAIEmbeddings()
  Merged_VectorStore = FAISS.load_local(Merged_Vector_Path, embeddings)
  delete_document(Merged_VectorStore, f"data\\filtered_txts\\{type}s\\{xml_id}.txt")
  print("\n--------\n",show_vstore(Merged_VectorStore),"\n--------- Deleted : ",f"data\\filtered_txts\\{type}s\\{xml_id}.txt","\n----------")
  add_to_vector(type, xml_id)
  Merged_VectorStore.save_local(Merged_Vector_Path)


# --------------------- END - VIEW , ADD , DELETE - END ----------------------

# --------------------- Formatted Source --------------------------

from dotenv import load_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
# from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain_community.callbacks import get_openai_callback
import os
import openai
import json
import re
import shutil

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def vectorise(xml_id, type):

    from langchain_community.document_loaders import DirectoryLoader
    from langchain_community.document_loaders import TextLoader
    from langchain_community.vectorstores import FAISS
    from langchain_openai import OpenAIEmbeddings
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    loader1 = DirectoryLoader(f'data/filtered_txts/{type}s', glob=f"./{xml_id}.txt", loader_cls=TextLoader, loader_kwargs=dict(encoding="utf-8"))
    document1 = loader1.load()
    
    if not os.path.exists("data/vectors"):
        os.makedirs("data/vectors")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    docs = text_splitter.split_documents(document1)
    embeddings = OpenAIEmbeddings()

    docs_db = FAISS.from_documents(docs, embeddings)
    docs_db.save_local(f"data/vectors/{type}_{xml_id}")
    print("Successfully vectorised --> ", type, " -- ", xml_id)

    return "Successful!"

global agent

def create_agent():

    from langchain_openai import ChatOpenAI
    from langchain.chains.conversation.memory import ConversationSummaryBufferMemory
    from langchain.chains import ConversationChain
    global agent

    llm = ChatOpenAI(model_name='gpt-3.5-turbo-16k')
    memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=1000)
    agent = ConversationChain(llm=llm, memory=memory, verbose=True)

    return "Successful!"

def formatted_response(docs, question, response, state):

    formatted_output = response + "\n\nSources"

    for i, doc in enumerate(docs):
        source_info = doc.metadata.get('source', 'Unknown source')
        page_info = doc.metadata.get('page', None)

        doc_name = source_info.split('/')[-1].strip()

        if page_info is not None:
            formatted_output += f"\n{doc_name}\tpage no {page_info}"
        else:
            formatted_output += f"\n{doc_name}"

    state.append((question, formatted_output))
    return state, state

def search_docs(prompt, question, state = []):

    from langchain_openai import OpenAIEmbeddings
    from langchain_community.vectorstores import FAISS
    from langchain_community.callbacks import get_openai_callback
    global agent
    agent = agent

    state = state or []

    embeddings = OpenAIEmbeddings()
    docs_db = FAISS.load_local("data/merged_vector", embeddings)
    docs = docs_db.similarity_search(question)

    prompt += "\n\n"
    prompt += question
    prompt += "\n\n"
    prompt += str(docs)

    with get_openai_callback() as cb:
        response = agent.predict(input=prompt)
        print(cb)

    # return formatted_response(docs, question, response, state)
    return response

def merge_db(callback):
    vector_base_folder = f"data/vectors"
    final_folder = f"data/merged_vector"
    if os.path.exists(final_folder):
        try:
            # Use shutil.rmtree to delete the folder and its contents
            shutil.rmtree(final_folder)
            print(f"Folder '{final_folder}' and its contents deleted successfully.")
        except Exception as e:
            print(f"Error: Unable to delete folder '{final_folder}'. {e}")
    else:
        print(f"Folder '{final_folder}' does not exist.")
    print(f"----------\n\n{vector_base_folder}\n\n{final_folder}\n\n--------")
    embeddings = OpenAIEmbeddings()
    all_items  = os.listdir(vector_base_folder)
    folders = [item for item in all_items if os.path.isdir(os.path.join(vector_base_folder, item))]
    print(len(folders))
    if len(folders)==1:
        VectorStore1 = FAISS.load_local(f"{vector_base_folder}/{folders[0]}", embeddings=embeddings)
        VectorStore1.save_local(final_folder)
        print("\n\nRunning Folder 1 only")
        # return "Merged - Single"
        return "success"
    print("\n\nRunning Multi Folders")
    print(f"\n\n{vector_base_folder}/{folders[0]}")
    VectorStore1 = FAISS.load_local(f"{vector_base_folder}/{folders[0]}", embeddings=embeddings)
    print(f"\n\n{vector_base_folder}/{folders[1]}")
    VectorStore2 = FAISS.load_local(f"{vector_base_folder}/{folders[1]}", embeddings=embeddings)
    VectorStore2.merge_from(VectorStore1)
    VectorStore2.save_local(final_folder)
    # for i in range(2,3):
    for i in range(2,len(folders)):
        VectorStore1 = FAISS.load_local(final_folder, embeddings=embeddings)
        VectorStore2 = FAISS.load_local(f"{vector_base_folder}/{folders[i]}", embeddings=embeddings)
        print(f"\n\n{vector_base_folder}/{folders[i]}")
        output = f"\nMerging Folder {i} out of {len(folders)} : {folders[i]}"
        callback(output)
        VectorStore2.merge_from(VectorStore1)
        VectorStore2.save_local(final_folder)

    # response = "Merged - Multiple"
    response = "success"

    return response

# print(process_docs())
# print(create_agent())
# print(search_docs("Give me the following answers from the context you have", "tell me about wiener werkstatte"))
# print(merge_db())


# --------------------- END - Formatted Source - END --------------------------

