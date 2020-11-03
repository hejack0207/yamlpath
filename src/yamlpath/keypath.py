import yaml

def keypaths(document, row, column):
    text=document
    row = int(row) - 1
    column = int(column) - 1
    #print(text)
    paths=[]
    lastKey=None
    mappingStart=False

    for token in yaml.scan(text):
        #print("line:%d,column:%d" % (token.start_mark.line,token.start_mark.column))
        #print("token:%s" % repr(token))
        #print("start_mark:%s \nend_mark:%s" % (token.start_mark, token.end_mark))
        if token.start_mark.line > row or (token.start_mark.line == row and token.start_mark.column > column):
            return paths

        if isinstance(token, yaml.tokens.KeyToken):
            isKey = True
            isValue = False
        else:
            if isinstance(token, yaml.tokens.ValueToken):
                if len(paths) > 0:
                    paths[-1]=lastKey.value
            if isinstance(token, yaml.tokens.ScalarToken) and isKey:
                lastKey = token
                if mappingStart is True:
                    paths.append(token.value)
                    mappingStart = False
            if isinstance(token, yaml.tokens.BlockEndToken):
                if len(paths) > 0 and not (token.start_mark.line == row and token.start_mark.column > column):
                    paths.pop()
            if isinstance(token, yaml.tokens.BlockMappingStartToken):
                mappingStart=True
            isKey = False

    return paths
