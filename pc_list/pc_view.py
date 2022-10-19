# PC_手厥陰心包経
from flask import Blueprint,render_template

pc_v=Blueprint("pc_v",__name__,template_folder="pc_templates")

@pc_v.route('/pc/',methods=['GET','POST'])
def pc():
    return render_template('pc.html')

@pc_v.route('/pc_01/',methods=['GET','POST'])
def pc_01():
    return render_template('pc_01.html')

@pc_v.route('/pc_02/',methods=['GET','POST'])
def pc_02():
    return render_template('pc_02.html')

@pc_v.route('/pc_03/',methods=['GET','POST'])
def pc_03():
    return render_template('pc_03.html')

@pc_v.route('/pc_04/',methods=['GET','POST'])
def pc_04():
    return render_template('pc_04.html')

@pc_v.route('/pc_05/',methods=['GET','POST'])
def pc_05():
    return render_template('pc_05.html')

@pc_v.route('/pc_06/',methods=['GET','POST'])
def pc_06():
    return render_template('pc_06.html')

@pc_v.route('/pc_07/',methods=['GET','POST'])
def pc_07():
    return render_template('pc_07.html')

@pc_v.route('/pc_08/',methods=['GET','POST'])
def pc_08():
    return render_template('pc_08.html')

@pc_v.route('/pc_09/',methods=['GET','POST'])
def pc_09():
    return render_template('pc_09.html')