from sanic.response import text
from sanic import Blueprint
from sanic import Sanic
import json

bp_talk = Blueprint("talk")


@bp_talk.get("/talk")
async def talk(request):
    app = Sanic.get_app()
    ws = app.ctx.ws
    await ws.send(json.dumps({"type": "signal", "state": "wait"}))
    return text('对话')


@bp_talk.websocket("/ws")
async def feed(request, ws):
    # 获取到应用上下文示例
    app = Sanic.get_app()
    app.ctx.ws = ws
    print('ws已连接')
    # while True:
    # data = "signal"
    # print("Sending: " + data)
    # await ws.send(json.dumps({"type":data,"state":"listen"}))
    # data = await ws.recv()
    # print("Received: " + data)
    # break
    # data = "signal"
    # print("Sending: " + data)
    await ws.send(json.dumps({"type": "signal", "state": "wait"}))
