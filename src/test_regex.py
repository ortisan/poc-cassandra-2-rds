import re
if __name__ == "__main__":
    import json    
    x = "[{id: fbb3286a-b6ac-492b-891a-c6191019ac6e, phone_number: 123456, description: , creation_date: '2018-04-26 05:59:38.000+0000'}]"
    x = re.sub(r'([a-zA-Z0-9_]+)\s*:\s*([^,}]+)?', '"\\1": "\\2"', x)
    print(x)
    x = re.sub(r'(\"\')|(\'\")', '"', x)    
    y = json.loads(x)
    print(y)
