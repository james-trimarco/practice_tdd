import unittest


class TestNerClient(unittest.TestCase):
    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(
        self,
    ):
        model = NerModelTestDouble("eng")
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_list_given_nonempty_input_causes_empty_spacy_doc_ents(
        self,
    ):
        model = NerModelTestDouble("eng")
        # assumes we don't get back any doc ents
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in Wisconsin")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Richie Floyd", "label_": "PERSON"}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_result = {
            "ents": [{"ent": "Richie Floyd", "label": "Person"}],
            "html": "",
        }
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Albanian", "label_": "NORP"}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_result = {
            "ents": [{"ent": "Albanian", "label": "Group"}],
            "html": "",
        }
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Tirana", "label_": "LOC"}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_result = {
            "ents": [{"ent": "Tirana", "label": "Location"}],
            "html": "",
        }
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_multiple_ents_serializes_all(self):
        model = NerModelTestDouble("eng")
        doc_ents = [
            {"text": "Tirana", "label_": "LOC"},
            {"text": "Judith Butler", "label_": "PERSON"},
        ]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_result = {
            "ents": [
                {"ent": "Tirana", "label": "Location"},
                {"ent": "Judith Butler", "label": "Person"},
            ],
            "html": "",
        }
        self.assertListEqual(result["ents"], expected_result["ents"])