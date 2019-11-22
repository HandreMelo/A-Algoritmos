#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, os.path
import random
import string

import cherrypy

grafo = {}
entregas = {}
class StringGenerator(object):


    @cherrypy.expose
    def index(self):
        return open('indexTest.html')

    @cherrypy.expose
    def mostrarArquivo(self):
        return cherrypy.session['mystring']

    @cherrypy.expose
    def enviarArquivo(self, ufile):
        upload_path = os.path.dirname(__file__)

        grafo, entregas = graphLogic.ler_arquivo(ufile)
        grafoJson = json.dumps(entregas)
        return grafoJson

    @cherrypy.expose
    def alterarArquivo(self, another_string):
        cherrypy.session['mystring'] = another_string

    @cherrypy.expose
    def deletarArquivo(self):
        cherrypy.session.pop('mystring', None)


if __name__ == '__main__':

    import json
    import networkx as nx
    import graphLogic
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }

    cherrypy.quickstart(StringGenerator(), '/', conf)