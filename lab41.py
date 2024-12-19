def lab41():
    import json
    import yaml
    with open('лаб инф 4\\JSON-in.json', 'r',encoding='utf-8') as j:
        data = json.load(j)
    with open('лаб инф 4\\YAML-out.yaml', 'w',encoding='utf-8') as y:
        yaml.dump(data, y,allow_unicode=True)
lab41()