from aiohttp import web

Rkn_TelegraphBot = web.RouteTableDef()

@Rkn_TelegraphBot.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Rkn_TelegraphBot")


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(Rkn_TelegraphBot)
    return web_app
  
