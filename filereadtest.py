#read text
items=['EVENT_NONE']
with open('C:/Users/tfgui/Documents/PythonTest/ClientEvents.txt','r') as f:
    lines=f.readlines()
    for i in lines:
        temp=i.strip()
        if len(temp)==0:
            continue
        if temp[0:2]=='//':
            continue
        items.append(temp)
        
print(items)

def writeline(file, line, end=''):
    #file.write(line)
    #file.write(end)
    #file.write('\n')
    file.write(line+end+'\n')
    
    
#save .h
path='C:/Users/tfgui/Documents/Arduino/fsxconnect/ClientEvents.h'
with open(path, 'w') as f:
    #f.write('enum CLIENT_EVENTS {')
    #f.write('NONE,')
    writeline(f, 'enum CLIENT_EVENTS')
    writeline(f, '{')
    for i in items:
        writeline(f, i, end=',')
    writeline(f, '};')
    
#save .cs
path='C:/Users/tfgui/source/repos/FSXConnectCS/FSXConnectCS/ClientEvents.cs'
with open(path, 'w') as f:
    #f.write('enum CLIENT_EVENTS {')
    #f.write('NONE,')
    writeline(f, 'enum CLIENT_EVENTS')
    writeline(f, '{')
    for i in items:
        writeline(f, i, end=',')
    writeline(f, '};')
    
#save .py
path='C:/Users/tfgui/Documents/PythonTest/FSXConnectPi/ClientEvents.py'
with open(path, 'w') as f:
    value=0
    for i in items:
        writeline(f, i, end='=%d'%value)
        value+=1

