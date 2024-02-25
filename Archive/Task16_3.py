n = input()
def lowercase_deco(func):
  def wrapper():
    original_result = func()
    modi_result = original_result.lower()
    return modi_result
  return wrapper

@lowercase_deco
def w():
  return n
print(w())
