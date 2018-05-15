from db import app, db
from flask_script import Manager, Server
from misapp.modle import User
# 通过拓展来管理flask应用
manager = Manager(app)

# 添加自定义命令,通过python main.py server就可以开启
manager.add_command('server', Server)

@app.route('/')
def home():
    users = User.query.all()
    print (users)
    return str(users)
if __name__ == '__main__':
    app.run()