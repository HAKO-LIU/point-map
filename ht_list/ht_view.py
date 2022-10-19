# HT_手少陰心経
from flask import Blueprint,render_template

ht_v=Blueprint("ht_v",__name__,template_folder="ht_templates")

@ht_v.route('/ht/',methods=['GET','POST'])
def ht():
    return render_template('ht.html')

@ht_v.route('/ht_01/',methods=['GET','POST'])
def ht_01():
    return render_template('ht_01.html')

@ht_v.route('/ht_02/',methods=['GET','POST'])
def ht_02():
    return render_template('ht_02.html')

@ht_v.route('/ht_03/',methods=['GET','POST'])
def ht_03():
    return render_template('ht_03.html')

@ht_v.route('/ht_04/',methods=['GET','POST'])
def ht_04():
    return render_template('ht_04.html')

@ht_v.route('/ht_05/',methods=['GET','POST'])
def ht_05():
    return render_template('ht_05.html')

@ht_v.route('/ht_06/',methods=['GET','POST'])
def ht_06():
    return render_template('ht_06.html')

@ht_v.route('/ht_07/',methods=['GET','POST'])
def ht_07():
    return render_template('ht_07.html')

@ht_v.route('/ht_08/',methods=['GET','POST'])
def ht_08():
    return render_template('ht_08.html')

@ht_v.route('/ht_09/',methods=['GET','POST'])
def ht_09():
    return render_template('ht_09.html')