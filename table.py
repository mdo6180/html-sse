from threading import Lock


class Table:
    def __init__(self) -> None:
        self.list = list()
        self.lock = Lock()
    
    def append(self, item):
        with self.lock:
            self.list.append(item)

    def remove(self, item):
        with self.lock:
            self.list.remove(item)

    def __getitem__(self, index):
        with self.lock:
            return self.list[index]

    def __len__(self):
        with self.lock:
            return len(self.list)
    
    