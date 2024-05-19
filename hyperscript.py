from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.responses import StreamingResponse

import asyncio

from components.hyperscript import homepage



app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")


@app.get("/", response_class=HTMLResponse)
def chat_page():
    return homepage()

@app.get("/event-source")
async def chat(request: Request):
    print("connected")
    async def chatroom():
        i = 0

        while True:
            try:
                await asyncio.sleep(1)
                print("update")
                if i % 2 == 0:
                    yield "event: EventName\n" 
                    yield "data: black"
                else:
                    yield "event: EventName\n" 
                    yield "data: red"

                i += 1
            
            except asyncio.CancelledError:
                yield "event: close\n"
                break

    return StreamingResponse(chatroom(), media_type="text/event-stream")