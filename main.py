from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import Request, Response
from fastapi.responses import StreamingResponse

import asyncio

from subapp.main import Node
from table import Table

from components.home import home_page
from components.table import table_rows
from components.chat import chat_homepage, chat_data

table = Table()
node1 = Node("node1", table)
node2 = Node("node2", table)
node1.start()
node2.start()

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root():
    return home_page()


start_index = 0

@app.get("/rows", response_class=HTMLResponse)
def rows():
    global start_index
    end_index = len(table)

    if end_index > start_index:
        return_table = table_rows(table[start_index:end_index])
        print(f"start_index = {start_index}, end_index = {end_index}")
        start_index = end_index
        return return_table


@app.get("/events", response_class=HTMLResponse)
async def stuff(request: Request):
    async def event_stream():
        while True:
            try:
                await asyncio.sleep(1)
                print("update")
                yield "event: update\n"

            except asyncio.CancelledError:
                yield "event: close\n"
                break

    return StreamingResponse(event_stream(), media_type="text/event-stream")

@app.get("/chat", response_class=HTMLResponse)
def chat_page():
    return chat_homepage()

n = 0
@app.get("/chat-row", response_class=HTMLResponse)
def chat_row():
    global n
    html_str = chat_data(n)
    n += 1
    return html_str

@app.get("/event-source")
async def chat(request: Request):
    async def chatroom():
        i = 0

        while True:
            try:
                await asyncio.sleep(1)
                print("update")
                yield "event: EventName\n" 
                yield "data:\n\n"
                i += 1
            
            except asyncio.CancelledError:
                yield "event: close\n"
                break

    return StreamingResponse(chatroom(), media_type="text/event-stream")

