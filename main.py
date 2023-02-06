# -*- coding: utf-8 -*-
'''
    @读取数据文件
    @January, 1, 8
    @author: lc
'''
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# 查询
from flask_wtf import FlaskForm
from flask import flash, request, send_file, redirect, url_for
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from foo.read_csv import read_csv
import subprocess
from time import sleep

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

# 全局变量串口exe
chuankou_p = None


def get_chuankou_exe() -> subprocess.Popen:
    global chuankou_p
    if chuankou_p:
        return chuankou_p
    exe_path = 'chuankou.exe'
    p = subprocess.Popen(exe_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True, shell=True, encoding='gbk')
    chuankou_p = p
    # print("启动串口exe")
    return p


def close_chuankou_exe():
    global chuankou_p
    if chuankou_p:
        # print("关闭串口exe")
        chuankou_p.stdin.write("e\n")
        chuankou_p.stdin.flush()
        try:
            timer = 0
            while timer < 10:
                try:
                    # 读出串口程序打印的数据, 一定要读取出来 可以不print
                    line = chuankou_p.stdout.readline()
                    # print("exe out: ", line)
                except UnicodeError:
                    print('UnicodeError')
                    line = ""
                if line == 'end\n':
                    break
                if line == "":
                    timer += 1
                    # sleep(0.1)
        except Exception as e:
            # 这段运行十有八九会出异常 怀疑因为在读取输出的时候chuankou.exe已经完成退出导致取不到数据, 但是程序运行不受影响
            print(e)
        chuankou_p = None


# 此处是为了代码自动补全功能
chuankou_p = get_chuankou_exe()

app = Flask(__name__)
# CORS(app,supports_credentials=True)
# api.init_app(app)

app.config.from_object(database_config)

# db=SQLAlchemy(app)  #数据库连接
# db.create_all()


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

# 可以自行调整
app.config["SECRET_KEY"] = 'happynewyear'

def display_serial(char):
    char_ = char
    res = read_csv('pin/' + char_ + '.csv')
    # 调用c
    print("res: ", res)
    # 此处会先关闭串口程序再次打开 是为了避免同一串口进程缺少init和屏幕清零过程导致不更新数据
    p = get_chuankou_exe()
    close_chuankou_exe()
    p = get_chuankou_exe()
    # 连续写入两次需要发送的数据 怀疑python底层有bug
    p.stdin.write(res + '\n')
    p.stdin.flush()
    p.stdin.write(res + '\n')
    p.stdin.flush()
    # sleep(2)
    # 读出串口程序打印的数据, 一定要读取出来 可以不print
    try:
        line = p.stdout.readline()
        # print(line)
    except UnicodeError as e:
        # print(e)
        # sleep(0.1)
        line = ""
    timer = 0
    # 999作为输出完成的标志 如果需要调整需要同步调整串口c文件
    while '999' not in line and timer < 10:
        # print(1)
        # p.stdin.write('\n')
        try:
            line = p.stdout.readline()
            print(line)
        except UnicodeError as e:
            print(e)
            timer += 1
            # sleep(0.1)
            line = ""
        print(2)
    print(line)

# @app.route('/', methods=['GET', 'POST'])
# def admin():
#     return render_template('menu.html')

# 替换首页为搜索框
@app.route('/', methods=['GET', 'POST'])
def admin():
    if request.method == "POST":
        char_ = request.form.get("char")
        print(char_)
        if not all([char_]):
            # 向前端界面弹出一条提示(闪现消息)
            flash("文字を入力してください")
        if len(char_) > 1:
            flash("入力できる文字数は1文字のみ")

        else:
            res = read_csv('C:/Users/watanabe Lab/PycharmProjects/point-map/pin/' + char_ + '.csv')
            print(res)
            if res == -1:
                flash("文字が見つからない")
            else:
                display_serial(char_)
                # # 调用c
                # # flash('[{char_}]正在调用串口'.format(char_=char_))
                # print("res: ", res)
                # # 此处会先关闭串口程序再次打开 是为了避免同一串口进程缺少init和屏幕清零过程导致不更新数据
                # p = get_chuankou_exe()
                # close_chuankou_exe()
                # p = get_chuankou_exe()
                # # 连续写入两次需要发送的数据 怀疑python底层有bug
                # p.stdin.write(res + '\n')
                # p.stdin.flush()
                # p.stdin.write(res + '\n')
                # p.stdin.flush()
                # sleep(2)
                # # 读出串口程序打印的数据, 一定要读取出来 可以不print
                # try:
                #     line = p.stdout.readline()
                #     print(line)
                # except UnicodeError as e:
                #     print(e)
                #     sleep(0.1)
                #     line = ""
                # # line, err = p.communicate()
                # timer = 0
                # # 999作为输出完成的标志 如果需要调整需要同步调整串口c文件
                # while '999' not in line and timer < 10:
                #     print(1)
                #     # p.stdin.write('\n')
                #     try:
                #         line = p.stdout.readline()
                #         print(line)
                #     except UnicodeError as e:
                #         print(e)
                #         timer += 1
                #         sleep(0.1)
                #         line = ""
                #     print(2)
                #
                # print(line)
                # cmd = 'chuankou.exe {exit_flag} {res}'.format(exit_flag=1, res=res)
                # out = os.system(cmd)
                # try:
                #     timer = 0
                #     while timer < 10:
                #         line = get_chuankou_exe().stdout.readline()
                #         print("exe out: ", line.replace("\n", ""))
                #         if line == " ":
                #             break
                #         if line.replace(" ", "") == "":
                #             timer += 1
                #             sleep(0.1)
                #             print(timer)
                #         print("exe out: ", line)
                # except UnicodeDecodeError:
                #     pass
                # flash('[{char_}]调用已完成'.format(char_=char_))
                # 打印结束后跳转到csv界面
                return redirect('/dispaly_html/{csv_id}'.format(csv_id=char_))

    return render_template('menu.html')


# 串口开关后台接口
@app.route('/serial/<serial_switch>', methods=['GET', 'POST'])
def serial_switch(serial_switch):
    global chuankou_p
    serial_switch = serial_switch
    if serial_switch == "1":
        chuankou_p = get_chuankou_exe()
    else:
        close_chuankou_exe()
    return redirect(url_for('admin'))


@app.route('/dispaly_html/<csv_id>', methods=['GET', 'POST'])
def display_html(csv_id):
    csv_id = csv_id
    all_list = get_all_list(csv_id)

    return render_template('display_html.html', dataset=all_list)


@app.route('/menu/', methods=['GET', 'POST'])
def menu():
    return redirect(url_for('admin'))


@app.route('/img/<img_name>', methods=['GET'])
def get_pic(img_name):
    return send_file('static\\{img_name}.jpg'.format(img_name=img_name))


def get_all_list(csv_id):
    csv_id = csv_id
    # print(csv_id)
    # 原存档csv的文件夹改名为pin, 防止编码错误
    # csv_url = os.getcwd() + 'pin/' + csv_id + '.csv'
    csv_url = 'C:/Users/watanabe Lab/PycharmProjects/point-map'+ '/pin/' + csv_id + '.csv'
    # print(csv_url)

    # dataset = tablib.Dataset()
    # with open(os.path.join(os.path.dirname(__file__),'/Users/liuzhihan/Downloads/code/データ保存ファイル/八.csv')) as f:
    #     dataset.csv = f.read()
    # dataset = pd.read_csv('/Users/liuzhihan/Downloads/code/データ保存ファイル/八.csv')
    dataset = pd.read_csv(csv_url)
    data = np.array(dataset)
    h = data.shape[0]
    w = data.shape[1]
    all_list = []
    for i in range(h):
        row_list = []
        for k in range(w):
            row_list.append(data[i][k])
        all_list.append(row_list)
    return all_list


@app.route('/display/<csv_id>', methods=['GET', 'POST'])
def display(csv_id):
    all_list = get_all_list(csv_id)
    # csv_id = csv_id
    # # print(csv_id)
    # csv_url = os.getcwd()+'/pin/' + csv_id + '.csv'
    # print(csv_url)
    #
    # # dataset = tablib.Dataset()
    # # with open(os.path.join(os.path.dirname(__file__),'/Users/liuzhihan/Downloads/code/データ保存ファイル/八.csv')) as f:
    # #     dataset.csv = f.read()
    # # dataset = pd.read_csv('/Users/liuzhihan/Downloads/code/データ保存ファイル/八.csv')
    # dataset = pd.read_csv(csv_url)
    # data = np.array(dataset)
    # h = data.shape[0]
    # w = data.shape[1]
    # all_list = []
    # for i in range(h):
    #     row_list = []
    #     for k in range(w):
    #         row_list.append(data[i][k])
    #     all_list.append(row_list)
    # # print(all_list)
    #
    res = read_csv('pin/' + csv_id + '.csv')
    if res == -1:
        return redirect(url_for('admin'))
    else:
        display_serial(csv_id)
    #
    return render_template('display.html', dataset=all_list)


@app.route('/404/')
def err_404():
    return render_template('404.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
    #  app.run(host='10.211.55.2', port=5000,debug=True)
