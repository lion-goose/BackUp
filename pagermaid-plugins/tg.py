from time import sleep
from requests import get
from pagermaid.listener import listener
import json


@listener(is_plugin=True, outgoing=True, command="tg",
          description="舔狗语录。")
async def tg(context):
    await context.edit("正在编舔狗语录 . . .")
    status=False
    for _ in range(20): #最多尝试20次
        req = get("https://api.muxiaoguo.cn/api/tiangourj")
        if req.status_code == 200:
            data = json.loads(req.text)
            res = data['data']['comment']
            await context.edit(res, parse_mode='html', link_preview=False)
            status=True
            break
        else:
            continue
    if status == False:
        await context.edit("出错了呜呜呜 ~ 试了好多好多次都无法访问到 API 服务器 。")
        sleep(2)
        await context.delete()
