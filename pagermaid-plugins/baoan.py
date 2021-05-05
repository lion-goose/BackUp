from time import sleep
from requests import get
from pagermaid.listener import listener
import json


@listener(is_plugin=True, outgoing=True, command="ba",
          description="保安日记。")
async def ba(context):
    await context.edit("正在编保安日记 . . .")
    status=False
    for _ in range(20): #最多尝试20次
        req = get("https://xiaojieapi.com/api/v1/get/security")
        if req.status_code == 200:
            data = json.loads(req.text)
            res = data['date'] + ' ' + data['week'] + ' ' + data['weather'] + '\n' + data['msg']
            await context.edit(res, parse_mode='html', link_preview=False)
            status=True
            break
        else:
            continue
    if status == False:
        await context.edit("出错了呜呜呜 ~ 试了好多好多次都无法访问到 API 服务器 。")
        sleep(2)
        await context.delete()
