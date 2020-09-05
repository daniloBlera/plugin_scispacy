#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implementation of the scispaCy plugin for DeepNLPF

This file is a modified version from the spaCy plugin.
"""
import json
import spacy

from deepnlpf.core.iplugin import IPlugin


class Plugin(IPlugin):
    def __init__(self, document, pipeline):
        self._document = document
        self._processors = pipeline["tools"]["scispacy"]["processors"]
        model = pipeline['tools']['scispacy']['model']
        self.nlp = spacy.load(model)

    def run(self):
        annotation =self.wrapper()
        return self.out_format(annotation)

    def wrapper(self):
        doc_formated = list()

        for index, sentence in enumerate(self._document):
            doc = self.nlp(sentence)
            data_tokens_list = []

            # Analisys in nivel token.
            for idx, token in enumerate(doc):
                data_token = {}

                data_token["idx"] = idx
                data_token["text"] = token.text

                if "pos" in self._processors:
                    data_token["pos"] = token.pos_
                if "tag" in self._processors:
                    data_token["tag"] = token.tag_
                if "shape" in self._processors:
                    data_token["shape"] = token.shape_
                if "is_alpha" in self._processors:
                    data_token["is_alpha"] = token.is_alpha
                if "is_title" in self._processors:
                    data_token["is_title"] = token.is_title
                if "like_num" in self._processors:
                    data_token["like_num"] = token.like_num

                data_tokens_list.append(data_token)

            list_chunks = list()
            if "noun_chunks" in self._processors:
                for chunk in doc.noun_chunks:
                    data_chunk = {}
                    data_chunk["text"] = chunk.text
                    data_chunk["root_text"] = chunk.root.text
                    data_chunk["root_dep_"] = chunk.root.dep_
                    data_chunk["root_head_text"] = chunk.root.head.text
                    json_data_chunk = data_chunk

                    list_chunks.append(json_data_chunk)
                    # print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)

            annotation_list = list()

            data = {}
            data["_id"] = index + 1
            data["text"] = sentence
            annotation_list.append({"tokens": data_tokens_list})

            if "noun_chunks" in self._processors:
                annotation_list.append({"noun_chunks": list_chunks})

            data["annotation"] = annotation_list
            json_data_result = json.loads(json.dumps(data))
            doc_formated.append(json_data_result)

        return doc_formated

    def out_format(self, doc):
        return doc
