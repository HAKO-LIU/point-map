# LR_足厥陰肝経
from flask import Blueprint,render_template

lr_v=Blueprint("lr_v",__name__,template_folder="lr_templates")

@lr_v.route('/lr/',methods=['GET','POST'])
def lr():
    return render_template('lr.html')

@lr_v.route('/lr_01/',methods=['GET','POST'])
def lr_01():
    return render_template('lr_01.html')

@lr_v.route('/lr_02/',methods=['GET','POST'])
def lr_02():
    return render_template('lr_02.html')

@lr_v.route('/lr_03/',methods=['GET','POST'])
def lr_03():
    return render_template('lr_03.html')

@lr_v.route('/lr_04/',methods=['GET','POST'])
def lr_04():
    return render_template('lr_04.html')

@lr_v.route('/lr_05/',methods=['GET','POST'])
def lr_05():
    return render_template('lr_05.html')

@lr_v.route('/lr_06/',methods=['GET','POST'])
def lr_06():
    return render_template('lr_06.html')

@lr_v.route('/lr_07/',methods=['GET','POST'])
def lr_07():
    return render_template('lr_07.html')

@lr_v.route('/lr_08/',methods=['GET','POST'])
def lr_08():
    return render_template('lr_08.html')

@lr_v.route('/lr_09/',methods=['GET','POST'])
def lr_09():
    return render_template('lr_09.html')

@lr_v.route('/lr_10/',methods=['GET','POST'])
def lr_10():
    return render_template('lr_10.html')

@lr_v.route('/lr_11/',methods=['GET','POST'])
def lr_11():
    return render_template('lr_11.html')

@lr_v.route('/lr_12/',methods=['GET','POST'])
def lr_12():
    return render_template('lr_12.html')

@lr_v.route('/lr_13/',methods=['GET','POST'])
def lr_13():
    return render_template('lr_13.html')

@lr_v.route('/lr_14/',methods=['GET','POST'])
def lr_14():
    return render_template('lr_14.html')