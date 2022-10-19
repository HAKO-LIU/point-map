# CV_任脈
from flask import Blueprint,render_template

cv_v=Blueprint("cv_v",__name__,template_folder="cv_templates")

@cv_v.route('/cv/',methods=['GET','POST'])
def cv():
    return render_template('cv.html')

@cv_v.route('/cv_01/',methods=['GET','POST'])
def cv_01():
    return render_template('cv_01.html')

@cv_v.route('/cv_02/',methods=['GET','POST'])
def cv_02():
    return render_template('cv_02.html')

@cv_v.route('/cv_03/',methods=['GET','POST'])
def cv_03():
    return render_template('cv_03.html')

@cv_v.route('/cv_04/',methods=['GET','POST'])
def cv_04():
    return render_template('cv_04.html')

@cv_v.route('/cv_05/',methods=['GET','POST'])
def cv_05():
    return render_template('cv_05.html')

@cv_v.route('/cv_06/',methods=['GET','POST'])
def cv_06():
    return render_template('cv_06.html')

@cv_v.route('/cv_07/',methods=['GET','POST'])
def cv_07():
    return render_template('cv_07.html')

@cv_v.route('/cv_08/',methods=['GET','POST'])
def cv_08():
    return render_template('cv_08.html')

@cv_v.route('/cv_09/',methods=['GET','POST'])
def cv_09():
    return render_template('cv_09.html')

@cv_v.route('/cv_10/',methods=['GET','POST'])
def cv_10():
    return render_template('cv_10.html')

@cv_v.route('/cv_11/',methods=['GET','POST'])
def cv_11():
    return render_template('cv_11.html')

@cv_v.route('/cv_12/',methods=['GET','POST'])
def cv_12():
    return render_template('cv_12.html')

@cv_v.route('/cv_13/',methods=['GET','POST'])
def cv_13():
    return render_template('cv_13.html')

@cv_v.route('/cv_14/',methods=['GET','POST'])
def cv_14():
    return render_template('cv_14.html')

@cv_v.route('/cv_15/',methods=['GET','POST'])
def cv_15():
    return render_template('cv_15.html')

@cv_v.route('/cv_16/',methods=['GET','POST'])
def cv_16():
    return render_template('cv_16.html')

@cv_v.route('/cv_17/',methods=['GET','POST'])
def cv_17():
    return render_template('cv_17.html')

@cv_v.route('/cv_18/',methods=['GET','POST'])
def cv_18():
    return render_template('cv_18.html')

@cv_v.route('/cv_19/',methods=['GET','POST'])
def cv_19():
    return render_template('cv_19.html')

@cv_v.route('/cv_20/',methods=['GET','POST'])
def cv_20():
    return render_template('cv_20.html')

@cv_v.route('/cv_21/',methods=['GET','POST'])
def cv_21():
    return render_template('cv_21.html')

@cv_v.route('/cv_22/',methods=['GET','POST'])
def cv_22():
    return render_template('cv_22.html')

@cv_v.route('/cv_23/',methods=['GET','POST'])
def cv_23():
    return render_template('cv_23.html')

@cv_v.route('/cv_24/',methods=['GET','POST'])
def cv_24():
    return render_template('cv_24.html')