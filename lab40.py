def lab40():
    def tab(n):
        for j in range(n): f.write('\t')
    fin=open('лаб инф 4\\JSON-in.json','r',encoding='utf-8').read()
    f=open('лаб инф 4\\YAML-out.yaml','w',encoding='utf-8')
    f.write('---')
    step=-1
    instring=0
    enterstat=0
    inlist=0
    listsym=0
    tabstat=0
    wait=0
    for i in range(len(fin)):
        if fin[i] not in r'{}[]":, ': f.write(fin[i])
        else:
            if fin[i]=='{':
                obj=1
                if enterstat==0:
                    f.write('\n')
                    step+=1
                enterstat=1
                tabstat=1
            if fin[i]=='}':
                obj=0
                if enterstat==0:
                    step-=1
                enterstat=1
                tabstat=1
            if fin[i]=='[':
                if wait==1: listsym=2
                else: listsym=1
                inlist=1
                if enterstat==0:
                    f.write('\n')
                    step+=1
                enterstat=1
                tabstat=1
            if fin[i]==']':
                inlist=0
                if enterstat==0:
                    step-=1
                enterstat=1
                tabstat=1
            if fin[i]==',':
                wait=1
                enterstat=0
                if instring==0:
                    f.write('\n')
                    tabstat=1
                    if obj==0 and inlist==1: listsym=1
                else: f.write(fin[i])
            if fin[i]=='"':
                wait=0
                instring^=1
                enterstat=0
                if tabstat==1:
                    tab(step-listsym)
                    tabstat=0
                while listsym >0:
                    f.write('- ')
                    listsym-=1
            if fin[i]==' 'and instring==1: f.write(' ')
            if fin[i]==':':
                f.write(fin[i]+' ')
    f.close()
    fin = open('лаб инф 4\\YAML-out.yaml','r',encoding='utf-8').readlines()
    f = open('лаб инф 4\\YAML-out.yaml','w',encoding='utf-8')
    for i in range(len(fin)):
        if fin[i].isspace()==False: f.write(fin[i])
lab40()