def doc_to_target(doc) -> int:
    choices = ["A", "B", "C", "D"]
    return choices.index(doc["prompt"][-1])
