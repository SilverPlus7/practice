#文本块生成器
def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        else:
            if ''.join(block).strip():
                yield ''.join(block).strip()
            block = []
