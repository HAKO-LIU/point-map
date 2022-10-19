# LU_手太陰肺経

from flask import Blueprint,render_template

lu_v=Blueprint("lu_v",__name__,template_folder="lu_templates")

@lu_v.route("/lu/",methods=['GET','POST'])
def lu():
    return render_template('lu.html')

@lu_v.route('/lu_01/',methods=['GET','POST'])
def lu_01():
    return render_template('lu_01.html')

@lu_v.route('/lu_02/',methods=['GET','POST'])
def lu_02():
    return render_template('lu_02.html')

@lu_v.route('/lu_03/',methods=['GET','POST'])
def lu_03():
    return render_template('lu_03.html')

@lu_v.route('/lu_04/',methods=['GET','POST'])
def lu_04():
    return render_template('lu_04.html')

@lu_v.route('/lu_05/',methods=['GET','POST'])
def lu_05():
    return render_template('lu_05.html')

@lu_v.route('/lu_06/',methods=['GET','POST'])
def lu_06():
    return render_template('lu_06.html')

@lu_v.route('/lu_07/',methods=['GET','POST'])
def lu_07():
    return render_template('lu_07.html')

@lu_v.route('/lu_08/',methods=['GET','POST'])
def lu_08():
    return render_template('lu_08.html')

@lu_v.route('/lu_09/',methods=['GET','POST'])
def lu_09():
    return render_template('lu_09.html')

@lu_v.route('/lu_10/',methods=['GET','POST'])
def lu_10():
    return render_template('lu_10.html')

@lu_v.route('/lu_11/',methods=['GET','POST'])
def lu_11():
    return render_template('lu_11.html')