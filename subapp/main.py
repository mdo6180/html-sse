from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Response

import threading
import random
import time


app = FastAPI()


class Node(threading.Thread):
    def __init__(self, name, table):
        self.table = table
        threading.Thread.__init__(self, name=name, daemon=True)
    
    def get_app(self):
        return app
    
    def run(self):
        i = 0
        time.sleep(2)

        while len(self.table) < 10:
            entry = {
                "book": f"book{i}", 
                "author": f"author{i}",
                "node": f"{self.name}"
            }

            self.table.append(entry)
            print(entry)
            i += 1
            time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    table = []
    node1 = Node("node1", table)
    node1.start()

    time.sleep(10)
    node1.join()