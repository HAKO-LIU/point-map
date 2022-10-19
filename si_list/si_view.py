# SI_手太陽小腸経
from flask import Blueprint,render_template

si_v=Blueprint("si_v",__name__,template_folder="si_templates")

@si_v.route('/si/',methods=['GET','POST'])
def si():
    return render_template('si.html')

@si_v.route('/si_01/',methods=['GET','POST'])
def si_01():
    return render_template('si_01.html')

@si_v.route('/si_02/',methods=['GET','POST'])
def si_02():
    return render_template('si_02.html')

@si_v.route('/si_03/',methods=['GET','POST'])
def si_03():
    return render_template('si_03.html')

@si_v.route('/si_04/',methods=['GET','POST'])
def si_04():
    return render_template('si_04.html')

@si_v.route('/si_05/',methods=['GET','POST'])
def si_05():
    return render_template('si_05.html')

@si_v.route('/si_06/',methods=['GET','POST'])
def si_06():
    return render_template('si_06.html')

@si_v.route('/si_07/',methods=['GET','POST'])
def si_07():
    return render_template('si_07.html')

@si_v.route('/si_08/',methods=['GET','POST'])
def si_08():
    return render_template('si_08.html')

@si_v.route('/si_09/',methods=['GET','POST'])
def si_09():
    return render_template('si_09.html')

@si_v.route('/si_10/',methods=['GET','POST'])
def si_10():
    return render_template('si_10.html')

@si_v.route('/si_11/',methods=['GET','POST'])
def si_11():
    return render_template('si_11.html')

@si_v.route('/si_12/',methods=['GET','POST'])
def si_12():
    return render_template('si_12.html')

@si_v.route('/si_13/',methods=['GET','POST'])
def si_13():
    return render_template('si_13.html')

@si_v.route('/si_14/',methods=['GET','POST'])
def si_14():
    return render_template('si_14.html')

@si_v.route('/si_15/',methods=['GET','POST'])
def si_15():
    return render_template('si_15.html')

@si_v.route('/si_16/',methods=['GET','POST'])
def si_16():
    return render_template('si_16.html')

@si_v.route('/si_17/',methods=['GET','POST'])
def si_17():
    return render_template('si_17.html')

@si_v.route('/si_18/',methods=['GET','POST'])
def si_18():
    return render_template('si_18.html')

@si_v.route('/si_19/',methods=['GET','POST'])
def si_19():
    return render_template('si_19.html')