#!/usr/bin/python
# -*- coding: utf-8 -*-

import apiRequest

class syntaxdb():
    def __init__(self):
        self.api_request = apiRequest.Request()
        self.options = {}

    def pre_process(self):
        #convert option value to string(recommend pass value's type exactly like the API Doc)
        for i in self.options:
            if not isinstance(self.options[i], str):
                self.options[i] = str(self.options[i])

        self.api_request.reset_url()
        if 'language_permalink' in self.options:
            self.api_request.addPath('languages', self.options['language_permalink'])
            del(self.options['language_permalink'])
        if 'category_id' in self.options:
            self.api_request.addPath('categories', self.options['category_id'])
            del(self.options['category_id'])
        if 'concept_permalink' in self.options:
            self.api_request.addPath('concepts', self.options['concept_permalink'])
            del(self.options['concept_permalink'])
        if 'concept_id' in self.options:
            self.api_request.addPath('concepts', self.options['concept_id'])
            del(self.options['concept_id'])

    def category(self):
        self.pre_process()
        if 'categories' not in self.api_request.request_url:
            self.api_request.addPath('categories')
        if 'q' in self.options:
            self.api_request.addPath('search')
        if self.options:
            self.api_request.addOptions(self.options)
        return self.api_request.send_request()
        
    def concept(self):
        self.pre_process()
        if 'concepts' not in self.api_request.request_url:
            self.api_request.addPath('concepts')
        if 'q' in self.options:
            self.api_request.addPath('search')
        if self.options:
            self.api_request.addOptions(self.options)
        return self.api_request.send_request()

    def language(self):
        self.pre_process()
        if 'languages' not in self.api_request.request_url:
            self.api_request.addPath('languages')
        if 'q' in self.options:
            self.api_request.addPath('search')
        if self.options:
            self.api_request.addOptions(self.options)
        return self.api_request.send_request()