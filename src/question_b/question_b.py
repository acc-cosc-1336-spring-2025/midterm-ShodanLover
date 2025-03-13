# write functions here, don't add input('') statements here!

def use_local_variable(num):
    num = 10

#test case
def test_local_variable():
  num = 100
  use_local_variable(num)
  assert num == 100, "Local variable should not affect the outer variable."

test_local_variable()
