from .keypath import keypaths
from .jsonschema.completer.completers import match_completions
from vim_bridge import bridged

schema_file=""

def completions(file_content,row,col):
    path = keypaths(file_content, row, col)
    print 'path:'+'/'.join(path)
    comps = match_completions(path,'/',schema_file)
    return comps

@bridged
def set_schema(filepath):
    global schema_file
    schema_file = filepath
    return schema_file

@bridged
def keys(file_content,row,col):
    comps = completions(file_content,row,col)
    return comps['keys']
    #return ['aaaa','bbbbb','cccc','dddd']

@bridged
def values(file_content,row,col):
    comps = completions(file_content,row,col)
    return comps['values']

@bridged
def show_path(file_content, row, col):
    path = keypaths(file_content, row, col)
    return '/'.join(path)

@bridged
def just_return(message):
    return message
