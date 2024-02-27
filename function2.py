def name_args(**kwargs):
  for k in kwargs.keys():
    print(f"{k}:{kwargs[k]}")

name_args(name="Randon", weather="sunny",location="park",time=3)

#2
def all_true(iter):
  return all(iter)

print(all_true([True, False]))
print(all_true((True, True)))

#3
def one_true(iterTwo):
  return any(iterTwo)

print(one_true([True,True,True]))
print(one_true([False, False, False]))
print(one_true((True, False)))

#4
def recursive_factorial(n):
  if n <= 1:
    return 1
  else:
    return n * recursive_factorial(n-1)

print(recursive_factorial(3))
print(recursive_factorial(6))

#5
def recursive_factorial(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  return num * recursive_factorial(num-1)
print(recursive_factorial(5))

#6
def recursive_deduplicate(str):
  if len(str) <= 1:
    return str
  elif str[0] == str[1]:
    return recursive_deduplicate(str[1:])
  else:
    return str[0] + recursive_deduplicate(str[1:])
      
print(recursive_deduplicate("aabbccdd"))

#7
def recursive_reverse(s):
  if len(s) <= 1:
    return s
  return s[-1] + recursive_reverse(s[:-1])
  
print(recursive_reverse("ih"))