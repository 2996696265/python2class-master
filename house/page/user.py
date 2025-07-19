from flask import Flask, Blueprint, render_template, redirect
from models import User;

user_page = Blueprint('user_page', __name__)

@user_page.route('/user/<name>')
def index(name):
    # 查询用户
    user = User.query.filter(User.name == name).first()
    if user:
        # 渲染页面 
        return render_template('user.html', user=user)

    else:
        #不存在则跳转回首页
        return redirect('/')

