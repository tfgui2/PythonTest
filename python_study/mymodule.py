def sum(a,b,op='+'):
    if op=='-':
        return a-b
    return a+b

def varg(*args):
    return len(args)