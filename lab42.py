def lab42():
    import re
    def tab(n):
        for j in range(n): f.write('\t')
    rex = re.compile(r'"(.*?)+"')
    fin=open('лаб инф 4\\JSON-in.json','r',encoding='utf-8').read()
    f=open('лаб инф 4\\YAML-out.yaml','w',encoding='utf-8')
    f.write('---\n')
    index = rex.finditer(fin)
    raw = re.sub(rex,'s',fin)
    raw = re.sub(r'[^\{\}\[\]:",s]','',raw)[1:-1]+' '
    raw2=''
    tabnum=0
    inlist=0
    inobj=0
    dash=0
    for i in range(len(raw)):
        if raw[i]=='[':
            raw2+='-'
            inlist=1
        if raw[i]==']':
            inlist=0
        if raw[i]==',' and inobj==0 and inlist==1:
            raw2+='-'
        if raw[i]=='{': inobj=1
        if raw[i]=='}': inobj=0
        raw2+=raw[i]
    raw=raw2
    for i in range(len(raw)):
        if raw[i]=='-':
            tabnum-=1
            dash=1
        if raw[i]=='s':
            if dash!=0:
                f.write('- ')
                tabnum+=1
                dash=0
            f.write(str(next(index).group(0)[1:-1]))
        if raw[i]=='{' and raw[i+1]!='[' or raw[i]=='[' and raw[i+1]!='{':
            tabnum+=1
            f.write('\n')
            tab(tabnum)
        if raw[i]=='}' and raw[i+1]!=']' or raw[i]==']' and raw[i+1]!='}':
            tabnum-=1
            f.write('\n')
        if raw[i]==':':
            if raw[i+1]=='[' or raw[i+1]=='{':
                f.write(':\n')
            else: f.write(': ')
        if raw[i]==',':
            f.write('\n')
            tab(tabnum)
    f.close()
    fin = open('лаб инф 4\\YAML-out.yaml','r',encoding='utf-8').readlines()
    f = open('лаб инф 4\\YAML-out.yaml','w',encoding='utf-8')
    for i in range(len(fin)):
            if fin[i].isspace()==False: f.write(fin[i])
lab42()