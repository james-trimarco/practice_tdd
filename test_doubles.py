class NerModelTestDouble:
    """
    Test double for spaCy NLP model
    """
    def __init__(self, model) -> None:
        self.model = model

    def returns_doc_ents(self, ents) -> None:
        self.ents = ents

    def __call__(self, sent):
        return DocTestDouble(sent, self.ents)

class DocTestDouble:
    """
    This is a test double for spaCy Doc.  
    """
    def __init__(self, sent, ents) -> None:
        self.ents = [SpanTestDouble(ent['text'], ent['label'] for ent in ents)]