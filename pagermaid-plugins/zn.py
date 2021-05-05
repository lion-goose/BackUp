from time import sleep
from requests import get
from pagermaid.listener import listener
import json
from random import randint, choice


@listener(is_plugin=True, outgoing=True, command="zn",
          description="渣男语录。")
async def zn(context):
    count = randint(1, 20)
    await context.edit("正在编渣男语录 . . .")
    status=False
    for _ in range(20): #最多尝试20次
        req = get("'https://api.lovelive.tools/api/SweetNothing/Keyword/' + str(count)")
        if req.status_code == 200:
            data = json.loads(req.text)
            res = choice(data['returnObj'])
            await context.edit(res, parse_mode='html', link_preview=False)
            status=True
            break
        else:
            continue
    if status == False:
        await context.edit("出错了呜呜呜 ~ 试了好多好多次都无法访问到 API 服务器 。")
        sleep(2)
        await context.delete()
