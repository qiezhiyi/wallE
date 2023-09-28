from sanic import Sanic
from sanic_cors import CORS
from blueprint.talk import bp_talk
from bg_task import wake
import json


app = Sanic(__name__)
# 挂载一个属性到应用上下文
app.ctx.ws = '我是初始化的ws'
# 添加CORS中间件
CORS(app)


# 挂载蓝图
app.blueprint(bp_talk)


# 异步后台任务
# @app.after_server_start
# async def task(app, loop):
#     wake_listener = wake.PorcupineListener()
#     app.add_task(wake_listener.run())


# 新建信号
# @app.signal("task.wake.happened")
# async def my_signal_handler():
#     print("唤醒")
# app_instance = Sanic.get_app()
# await app_instance.ctx.ws.send(json.dumps({"type":"signal","state":"listen"}))


if __name__ == '__main__':
    app.run()
