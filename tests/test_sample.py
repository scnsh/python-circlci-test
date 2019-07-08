import sample
import pytest

@pytest.mark.parametrize('name, ans', [
  ('Alice', 'HelloWorld Alice'),
  ('Bob', 'HelloWorld Bob'),
])
def test_hello_world(name, ans):
  hello_world = sample.HelloWorld()
  assert hello_world.gen_hello_world_msg(name) == ans