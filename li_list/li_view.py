# LI_手陽明大腸経
from flask import Blueprint,render_template

li_v=Blueprint("li_v",__name__,template_folder="li_templates")

@li_v.route('/li/',methods=['GET','POST'])
def li():
    return render_template('li.html')

@li_v.route('/li_01/',methods=['GET','POST'])
def li_01():
    return render_template('li_01.html')

@li_v.route('/li_02/',methods=['GET','POST'])
def li_02():
    return render_template('li_02.html')

@li_v.route('/li_03/',methods=['GET','POST'])
def li_03():
    return render_template('li_03.html')

@li_v.route('/li_04/',methods=['GET','POST'])
def li_04():
    return render_template('li_04.html')

@li_v.route('/li_05/',methods=['GET','POST'])
def li_05():
    return render_template('li_05.html')

@li_v.route('/li_06/',methods=['GET','POST'])
def li_06():
    return render_template('li_06.html')

@li_v.route('/li_07/',methods=['GET','POST'])
def li_07():
    return render_template('li_07.html')

@li_v.route('/li_08/',methods=['GET','POST'])
def li_08():
    return render_template('li_08.html')

@li_v.route('/li_09/',methods=['GET','POST'])
def li_09():
    return render_template('li_09.html')

@li_v.route('/li_10/',methods=['GET','POST'])
def li_10():
    return render_template('li_10.html')

@li_v.route('/li_11/',methods=['GET','POST'])
def li_11():
    return render_template('li_11.html')

@li_v.route('/li_12/',methods=['GET','POST'])
def li_12():
    return render_template('li_12.html')

@li_v.route('/li_13/',methods=['GET','POST'])
def li_13():
    return render_template('li_13.html')

@li_v.route('/li_14/',methods=['GET','POST'])
def li_14():
    return render_template('li_14.html')

@li_v.route('/li_15/',methods=['GET','POST'])
def li_15():
    return render_template('li_15.html')

@li_v.route('/li_16/',methods=['GET','POST'])
def li_16():
    return render_template('li_16.html')

@li_v.route('/li_17/',methods=['GET','POST'])
def li_17():
    return render_template('li_17.html')

@li_v.route('/li_18/',methods=['GET','POST'])
def li_18():
    return render_template('li_18.html')

@li_v.route('/li_19/',methods=['GET','POST'])
def li_19():
    return render_template('li_19.html')

@li_v.route('/li_20/',methods=['GET','POST'])
def li_20():
    return render_template('li_20.html')