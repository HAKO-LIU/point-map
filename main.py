# -*- coding: utf-8 -*-
'''
    @读取数据文件
    @January, 1, 8
    @author: lc
'''
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


from flask_cors import CORS
# from interfaces import api
import os
import tablib
import pandas as pd
import numpy as np
import database_config


from bl_list import bl_view
from cv_list import cv_view
from gb_list import gb_view
from gv_list import gv_view
from ht_list import ht_view
from ki_list import ki_view
from li_list import li_view
from lr_list import lr_view
from lu_list import lu_view
from pc_list import pc_view
from si_list import si_view
from sp_list import sp_view
from st_list import st_view
from te_list import te_view




app = Flask(__name__)
# CORS(app,supports_credentials=True)
# api.init_app(app)

app.config.from_object(database_config)

db=SQLAlchemy(app)  #数据库连接
db.create_all()


app.register_blueprint(bl_view.bl_v)
app.register_blueprint(cv_view.cv_v)
app.register_blueprint(gb_view.gb_v)
app.register_blueprint(gv_view.gv_v)
app.register_blueprint(ht_view.ht_v)
app.register_blueprint(ki_view.ki_v)
app.register_blueprint(li_view.li_v)
app.register_blueprint(lr_view.lr_v)
app.register_blueprint(lu_view.lu_v)
app.register_blueprint(pc_view.pc_v)
app.register_blueprint(si_view.si_v)
app.register_blueprint(sp_view.sp_v)
app.register_blueprint(st_view.st_v)
app.register_blueprint(te_view.te_v)

@app.route('/',methods=['GET','POST'])
def admin():
    return render_template('menu.html')

@app.route('/menu/',methods=['GET','POST'])
def menu():
    return render_template('menu.html')

@app.route('/display/<csv_id>',methods=['GET','POST'])
def display(csv_id):
    csv_id=csv_id;
    # print(csv_id)
    csv_url='/Users/liuzhihan/Downloads/code/データ保存ファイル/'+csv_id+'.csv'
    print(csv_url)

    # dataset = tablib.Dataset()
    # with open(os.path.join(os.path.dirname(__file__),'/Users/liuzhihan/Downloads/code/データ保存ファイル/八.csv')) as f:
    #     dataset.csv = f.read()
    # dataset = pd.read_csv('/Users/liuzhihan/Downloads/code/データ保存ファイル/八.csv')
    dataset=pd.read_csv(csv_url)
    data = np.array(dataset)
    h = data.shape[0]
    w = data.shape[1]
    all_list = []
    for i in range(h):
        row_list = []
        for k in range(w):
            row_list.append(data[i][k])
        all_list.append(row_list)
    # print(all_list)

    return render_template('display.html',dataset=all_list)

@app.route('/404/')
def err_404():
    return render_template('404.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True)
    #  app.run(host='10.211.55.2', port=5000,debug=True)