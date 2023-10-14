from aiohttp import web
from base.application import View
from config import BASE_DIR
import os

class MiniAppView(View):
    '''
    View for Mini App.
    '''
    async def get(self):
        with open(os.path.join(BASE_DIR, 'client', 'dist', 'index.html'), 'r') as f:
            file = f.read()

        return web.Response(
            body=file,
            headers={
                'Content-Type': 'text/html',
            }
        )

class WebSocketView(View):
    '''
    View for WebSocket connection.
    '''
    async def get(self):
        await self.explorer.ws.open(self.request)
        await self.explorer.ws_manager.handle_connection(self.request.game_id, self.request.user_id)
        await self.explorer.ws_manager.on_user_disconnect(self.request.game_id, self.request.user_id)
        # return self.explorer.ws.connections[self.request.game_id][self.request.user_id].ws