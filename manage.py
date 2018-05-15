from flask_script import Manager, Server
from misapp.main import app,db,User

manager = Manager(app)
manager.add_command("server",Server())

# 创建在命令行里面的上下文环境
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User)
if __name__ == "__main__":
    manager.run()