# SP_足太陰脾経
from flask import Blueprint,render_template

sp_v=Blueprint("sp_v",__name__,template_folder="sp_templates")

@sp_v.route('/sp/',methods=['GET','POST'])
def sp():
    return render_template('sp.html')

@sp_v.route('/sp_01/',methods=['GET','POST'])
def sp_01():
    return render_template('sp_01.html')

@sp_v.route('/sp_02/',methods=['GET','POST'])
def sp_02():
    return render_template('sp_02.html')

@sp_v.route('/sp_03/',methods=['GET','POST'])
def sp_03():
    return render_template('sp_03.html')

@sp_v.route('/sp_04/',methods=['GET','POST'])
def sp_04():
    return render_template('sp_04.html')

@sp_v.route('/sp_05/',methods=['GET','POST'])
def sp_05():
    return render_template('sp_05.html')

@sp_v.route('/sp_06/',methods=['GET','POST'])
def sp_06():
    return render_template('sp_06.html')

@sp_v.route('/sp_07/',methods=['GET','POST'])
def sp_07():
    return render_template('sp_07.html')

@sp_v.route('/sp_08/',methods=['GET','POST'])
def sp_08():
    return render_template('sp_08.html')

@sp_v.route('/sp_09/',methods=['GET','POST'])
def sp_09():
    return render_template('sp_09.html')

@sp_v.route('/sp_10/',methods=['GET','POST'])
def sp_10():
    return render_template('sp_10.html')

@sp_v.route('/sp_11/',methods=['GET','POST'])
def sp_11():
    return render_template('sp_11.html')

@sp_v.route('/sp_12/',methods=['GET','POST'])
def sp_12():
    return render_template('sp_12.html')

@sp_v.route('/sp_13/',methods=['GET','POST'])
def sp_13():
    return render_template('sp_13.html')

@sp_v.route('/sp_14/',methods=['GET','POST'])
def sp_14():
    return render_template('sp_14.html')

@sp_v.route('/sp_15/',methods=['GET','POST'])
def sp_15():
    return render_template('sp_15.html')

@sp_v.route('/sp_16/',methods=['GET','POST'])
def sp_16():
    return render_template('sp_16.html')

@sp_v.route('/sp_17/',methods=['GET','POST'])
def sp_17():
    return render_template('sp_17.html')

@sp_v.route('/sp_18/',methods=['GET','POST'])
def sp_18():
    return render_template('sp_18.html')

@sp_v.route('/sp_19/',methods=['GET','POST'])
def sp_19():
    return render_template('sp_19.html')

@sp_v.route('/sp_20/',methods=['GET','POST'])
def sp_20():
    return render_template('sp_20.html')

@sp_v.route('/sp_21/',methods=['GET','POST'])
def sp_21():
    return render_template('sp_21.html')