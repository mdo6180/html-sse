from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi import Request

import asyncio

from subapp.main import Node
from table import Table

from components.home import home_page
from components.table import table_rows

table = Table()
node1 = Node("node1", table)
node2 = Node("node2", table)
node1.start()
node2.start()

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")




start_index = 0
end_index = 0


@app.get("/", response_class=HTMLResponse)
def read_root():
    global start_index
    global end_index
    end_index = len(table)

    print(f"GET /: start_index = {start_index}, end_index = {end_index}")
    start_index = end_index
    return home_page(table[0:end_index])

def format_html_for_sse(html_content: str) -> str:
    # Split the HTML content into lines
    lines = html_content.split('\n')

    # Prefix each line with 'data: ' and join them back into a single string with newlines
    formatted_content = "\n".join(f"data: {line}" for line in lines if line.strip()) + "\n\n"

    return formatted_content

@app.get("/events", response_class=HTMLResponse)
async def stuff(request: Request):
    async def event_stream():
        while True:
            try:
                if await request.is_disconnected():
                    break
                else:
                    global start_index
                    global end_index 
                    end_index = len(table)

                    if end_index > start_index:
                        print(f"sse: start_index = {start_index}, end_index = {end_index}")
                        updated_table = table_rows(table[start_index:end_index])
                        start_index = end_index
                        yield "event: UpdateEvent\n"
                        yield format_html_for_sse(updated_table)
                    else:
                        await asyncio.sleep(1)

            except asyncio.CancelledError:
                print("browser closed")
                break

    return StreamingResponse(event_stream(), media_type="text/event-stream")
