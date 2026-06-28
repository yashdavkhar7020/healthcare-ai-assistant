from pathlib import Path
from langchain_core.documents import Document


DATA_DIR = Path("data")


def load_documents():
    documents = []

    for file_path in DATA_DIR.glob("*.txt"):

        text = file_path.read_text(encoding="utf-8")

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": file_path.name
                }
            )
        )

    return documents