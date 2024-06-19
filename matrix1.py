def func(s):
    return s.count('*')*'*' + ''.join(s.split('*'))
print(func(input("Enter String : ")))