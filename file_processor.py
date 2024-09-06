from pdf_parse import get_text
from llm import Groq_llm
from langchain_text_splitters import RecursiveCharacterTextSplitter

def process_file(filePath):
    text = get_text(filePath)
    groq_llm = Groq_llm()
    llm_summary = ""
    splitTexts = RecursiveCharacterTextSplitter(chunk_size = 10000, chunk_overlap = 1000).split_text(text)
    for textChunk in splitTexts:
        llm_summary += groq_llm.getSummary(textChunk)
    return groq_llm.getSummary(llm_summary)