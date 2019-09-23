class HelloWorld(object):
    def __init__(self):
        self.hello_world = 'HelloWorld'

    def gen_hello_world_msg(self, name: str):
        return self.hello_world + ' ' + name
