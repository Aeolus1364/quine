code = """print('code = ?{}?, ?{}?'.format(code[0], code[1]))""", """[print(code[x]) if x == 1 else print(code[x].replace('?', '"'+'""')) for x in range(len(code))]"""
print('code = """{}""", """{}"""'.format(code[0], code[1]))
[print(code[x]) if x == 1 else print(code[x].replace('?', '"'+'""')) for x in range(len(code))]

