from collections import deque
from typing import List


class AtCoderBase:
    def __init__(self, all_input: List[str]):
        self.all_input = deque(all_input)
        self.ret_str = ""
        self.msg = list()

    def input(self):
        def _input() -> str:
            line = self.all_input.pop()
            yield line
        return _input().__next__()

    def print(self, data):
        self.msg.append(str(data))

    def process(self):
        raise NotImplementedError
