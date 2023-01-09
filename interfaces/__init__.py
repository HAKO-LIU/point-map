# -*- coding: utf-8 -*-
'''
    @
    @January, 1, 20
    @author: hako
'''

from flask_restx import Api
# from interfaces.query_inter import api as ns_keyword

api = Api(
    title='経絡・経穴の文字表示システム',
    version='1.0'
)


# api.add_namespace(ns_keyword)
api.add_namespace()