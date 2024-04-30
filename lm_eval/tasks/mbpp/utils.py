import datasets

def process_docs(dataset: datasets.Dataset):
    """
    Processes the documents in the dataset to include the first element of the test list.
    """
    def _helper(doc):
        """
        Gets the first element from test list to use in our prompt.
        """
        doc["test"] = doc["test_list"][0]
        return doc
    return dataset.map(_helper)

def create_prompt(doc):
    """
    Creates a prompt from the document.
    """
    prompt = f"\"\"\"\n{doc['text']}\n{doc['test']}\n\"\"\"\n"
    return prompt[:1024]