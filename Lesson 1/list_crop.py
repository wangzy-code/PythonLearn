# list裁剪的使用
def stim(s):
    if s[:1]!=' 'and s[-1:]!=' ':
        return stim(s) 
    elif s[:1]==' ':
        return stim(s[1:])
    elif s[-1:]=='':
        return stim(s[:-2])
    print(s[:])
print(stim(' my name is yaner '))
