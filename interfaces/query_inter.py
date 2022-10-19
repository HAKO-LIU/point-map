# # -*- coding: utf-8 -*-
# '''
#     @读取数据文件
#     @January, 1, 13
#     @author: lc
# '''
# import os
#
# from flask import Flask
# from flask import request,make_response,render_template
# from flask_restx import Resource,Namespace
# # from docker_pull import docker_pull
# # from docker_pull import docker_pull_sys
# import json
#
# api = Namespace('Keywords',description='根据关键词查询')
# global_message_dict = {}
#
# #关键词查询接口
# # @api.route('/KeywordsQUERY',methods=['GET','POST'])
# # @api.param('key_words','请输入您要搜索的关键字',_in='formData',type='str')
# # @api.param('table_name','table id',_in='formData',type='str')
# # #@api.param('table_name','需要查询的零件类型',_in='formData',type='str')
# #
# # class key_words_all(Resource):
# #     def post(self):
# #         try:
# #             result_dict = {}
# #             docker_dir = "../docker_pull/"
# #             key_words = request.values.get('key_words')
# #             key_list = key_words.split(",")
# #             id = request.values.get('table_name')
# #             print("id:{}".format(id))
# #             # os.system("python docker_pull.py " + key_words)
# #
# #             if id == None:
# #                 message_dict = docker_pull_sys.docker_pull(key_list)
# #                 print(message_dict)
# #                 if len(message_dict)>0:
# #                     result_dict['code'] = 1
# #                     result_dict['value'] = message_dict
# #                 else:
# #                     result_dict['code'] = 0
# #                     result_dict['value'] = None
# #             else:
# #                 message_dict = docker_pull_sys.docker_scan(id)
# #                 print(message_dict)
# #                 if len(message_dict)>0:
# #                     new_dict = {}
# #                     result_dict['code'] = 1
# #                     new_dict['result'] = message_dict
# #                     result_dict['value'] = new_dict
# #                 else:
# #                     result_dict['code'] = 0
# #                     result_dict['value'] = None
# #             response = make_response(result_dict)
# #             response.headers['Content-Type'] = 'json'
# #             return response
# #         except Exception as ex:
# #             print("出现如下异常：%s" % ex)
# #
# #     def get(self):
# #         try:
# #             result_dict = {}
# #             docker_dir = "../docker_pull/"
# #             key_words = request.values.get('key_words')
# #             key_list = key_words.split(",")
# #             id = request.values.get('table_name')
# #             print("id:{}".format(id))
# #             # os.system("python docker_pull.py " + key_words)
# #
# #             if id == None:
# #                 message_dict = docker_pull_sys.docker_pull(key_list)
# #                 print(message_dict)
# #                 if len(message_dict) > 0:
# #                     result_dict['code'] = 1
# #                     result_dict['value'] = message_dict
# #                 else:
# #                     result_dict['code'] = 0
# #                     result_dict['value'] = None
# #             else:
# #                 message_dict = docker_pull_sys.docker_scan(id)
# #                 print(message_dict)
# #                 if len(message_dict) > 0:
# #                     new_dict = {}
# #                     result_dict['code'] = 1
# #                     new_dict['result'] = message_dict
# #                     result_dict['value'] = new_dict
# #                 else:
# #                     result_dict['code'] = 0
# #                     result_dict['value'] = None
# #             response = make_response(result_dict)
# #             response.headers['Content-Type'] = 'json'
# #             return response
# #         except Exception as ex:
# #             print("出现如下异常：%s" % ex)
# #
# # #登陆接口
# # @api.route('/login_in', methods=['GET','POST'])
# # @api.param('username','用户名',_in='formData',type='str')
# # @api.param('password','密码',_in='formData',type='str')
# # class Login_Form(Resource):
# #     def post(self):
# #         try:
# #             username = request.values.get('username')
# #             password = request.values.get('password')
# #             result_dict = {}
# #             if username == "root" and password == "123456":
# #                 result_dict['code'] = 1
# #                 result_dict['msg'] = "success"
# #                 response = make_response(result_dict)
# #                 response.headers['Content-Type'] = 'json'
# #             else:
# #                 result_dict['code'] = 401
# #                 result_dict['msg'] = "账户名或密码错误"
# #                 response = make_response(result_dict)
# #                 response.headers['Content-Type'] = 'json'
# #             return response
# #         except Exception as ex:
# #             print("出现如下异常：%s" % ex)
# #
# #     def get(self):
# #         try:
# #             username = request.values.get('username')
# #             password = request.values.get('password')
# #             result_dict = {}
# #             if username == "root" and password == "123456":
# #                 result_dict['code'] = 1
# #                 result_dict['msg'] = "success"
# #                 response = make_response(result_dict)
# #                 response.headers['Content-Type'] = 'json'
# #             else:
# #                 result_dict['code'] = 401
# #                 result_dict['msg'] = "账户名或密码错误"
# #                 response = make_response(result_dict)
# #                 response.headers['Content-Type'] = 'json'
# #             return response
# #         except Exception as ex:
# #             print("出现如下异常：%s" % ex)
# #
# # #执行docker扫描
# # @api.route('/id_query', methods=['GET','POST'])
# # @api.param('key_words','请输入您要搜索的关键字',_in='formData',type='str')
# # @api.param('id','需要查询的零件类型',_in='formData',type='str')
# # class query_table(Resource):
# #     def post(self):
# #         try:
# #             result_dict = {}
# #             key_words = request.values.get('key_words')
# #             id = request.values.get('id')
# #             message_dict = global_message_dict[str(id)]
# #
# #             if len(message_dict) > 0:
# #                 result_dict['code'] = 1
# #                 result_dict['value'] = message_dict
# #             else:
# #                 result_dict['code'] = 0
# #                 result_dict['value'] = None
# #             response = make_response(result_dict)
# #             response.headers['Content-Type'] = 'json'
# #             return response
# #         except Exception as ex:
# #             print("出现如下异常：%s" % ex)
# #
# #     def get(self):
# #         try:
# #             result_dict = {}
# #             key_words = request.values.get('key_words')
# #             id = request.values.get('id')
# #             message_dict = global_message_dict[str(id)]
# #
# #             if len(message_dict) > 0:
# #                 result_dict['code'] = 1
# #                 result_dict['value'] = message_dict
# #             else:
# #                 result_dict['code'] = 0
# #                 result_dict['value'] = None
# #             response = make_response(result_dict)
# #             response.headers['Content-Type'] = 'json'
# #             return response
# #         except Exception as ex:
# #             print("出现如下异常：%s" % ex)
# #
# # #获取历史docker扫描记录
# # @api.route('/history', methods=['GET','POST'])
# # @api.param('value','请输入您要搜索的关键字',_in='formData',type='str')
# # class query_table(Resource):
# #     def post(self):
# #         try:
# #             result_dict = {}
# #             value = request.values.get('value')
# #             if value == "0":
# #                 message_dict = docker_pull_sys.docker_history()
# #                 if len(message_dict) > 0:
# #                     result_dict['code'] = 1
# #                     result_dict['value'] = message_dict
# #                 else:
# #                     result_dict['code'] = 0
# #                     result_dict['value'] = None
# #
# #             response = make_response(result_dict)
# #             response.headers['Content-Type'] = 'json'
# #             return response
# #         except Exception as ex:
# #             print("出现如下异常：%s" % ex)
# #
# #     def get(self):
# #         try:
# #             result_dict = {}
# #             value = request.values.get('value')
# #             if value == "0":
# #                 message_dict = docker_pull_sys.docker_history()
# #                 if len(message_dict) > 0:
# #                     result_dict['code'] = 1
# #                     for key in message_dict:
# #                         result_dict[key] = message_dict[key]
# #                 else:
# #                     result_dict['code'] = 0
# #                     result_dict['value'] = None
# #
# #             response = make_response(result_dict)
# #             response.headers['Content-Type'] = 'json'
# #             return response
# #         except Exception as ex:
# #             print("出现如下异常：%s" % ex)