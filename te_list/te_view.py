# TE_手少陽三焦経
from flask import Blueprint,render_template

te_v=Blueprint("te_v",__name__,template_folder="te_templates")

@te_v.route('/te/',methods=['GET','POST'])
def te():
    return render_template('te.html')

@te_v.route('/te_01/',methods=['GET','POST'])
def te_01():
    return render_template('te_01.html')

@te_v.route('/te_02/',methods=['GET','POST'])
def te_02():
    return render_template('te_02.html')

@te_v.route('/te_03/',methods=['GET','POST'])
def te_03():
    return render_template('te_03.html')

@te_v.route('/te_04/',methods=['GET','POST'])
def te_04():
    return render_template('te_04.html')

@te_v.route('/te_05/',methods=['GET','POST'])
def te_05():
    return render_template('te_05.html')

@te_v.route('/te_06/',methods=['GET','POST'])
def te_06():
    return render_template('te_06.html')

@te_v.route('/te_07/',methods=['GET','POST'])
def te_07():
    return render_template('te_07.html')

@te_v.route('/te_08/',methods=['GET','POST'])
def te_08():
    return render_template('te_08.html')

@te_v.route('/te_09/',methods=['GET','POST'])
def te_09():
    return render_template('te_09.html')

@te_v.route('/te_10/',methods=['GET','POST'])
def te_10():
    return render_template('te_10.html')

@te_v.route('/te_11/',methods=['GET','POST'])
def te_11():
    return render_template('te_11.html')

@te_v.route('/te_12/',methods=['GET','POST'])
def te_12():
    return render_template('te_12.html')

@te_v.route('/te_13/',methods=['GET','POST'])
def te_13():
    return render_template('te_13.html')

@te_v.route('/te_14/',methods=['GET','POST'])
def te_14():
    return render_template('te_14.html')

@te_v.route('/te_15/',methods=['GET','POST'])
def te_15():
    return render_template('te_15.html')

@te_v.route('/te_16/',methods=['GET','POST'])
def te_16():
    return render_template('te_16.html')

@te_v.route('/te_17/',methods=['GET','POST'])
def te_17():
    return render_template('te_17.html')

@te_v.route('/te_18/',methods=['GET','POST'])
def te_18():
    return render_template('te_18.html')

@te_v.route('/te_19/',methods=['GET','POST'])
def te_19():
    return render_template('te_19.html')

@te_v.route('/te_20/',methods=['GET','POST'])
def te_20():
    return render_template('te_20.html')

@te_v.route('/te_21/',methods=['GET','POST'])
def te_21():
    return render_template('te_21.html')

@te_v.route('/te_22/',methods=['GET','POST'])
def te_22():
    return render_template('te_22.html')

@te_v.route('/te_23/',methods=['GET','POST'])
def te_23():
    return render_template('te_23.html')