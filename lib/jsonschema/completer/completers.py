import json
from ref_resolver import RefResolver

def _array():
    return ["[]",]

def _boolean():
    return ["true","false"]

def _integer():
    return ["0",]

def _null():
    return ["",]

def _number():
    return ["0.0",]

def _object():
    return ["{}",]

def _string():
    return ["abc",]

completers={
    u"array": _array, u"boolean": _boolean, u"integer": _integer,
    u"null": _null, u"number": _number, u"object": _object,
    u"string": _string,
}   

resolver=None

def ref(ref, schema, completions):
    #print "refering:"+ref
    scope, resolved = resolver.resolve(ref)
    resolver.push_scope(scope)

    complete(resolved, completions)
    resolver.pop_scope()


def complete(schema, completions):
    #print schema
    completions['keys']=[]
    completions['keypatterns']=[]
    completions['values']=[]

    if 'type' in schema:
        #print schema['type']
        types = schema['type']
        if isinstance(types, list):
            candi = [] 
            for typ in types:
                c = completers[typ]
                candidates = c()
                candi += candidates
            completions['values']=candi
        else:
            c = completers[types]
            candidates = c()
            completions['values']=candidates

    if 'properties' in schema:
        properties=schema['properties']
        keys=properties.keys()
        #print keys
        completions['keys']=keys
        for key in keys:
            #print "key:"+key
            completions[key]=dict()
            complete(properties[key],completions[key])

    if 'patternProperties' in schema:
        properties=schema['patternProperties']
        keys=properties.keys()
        #print keys
        completions['keypatterns']=keys
        for key in keys:
            #print "key:"+key
            completions[key]=dict()
            complete(properties[key],completions[key])

    if '$ref' in schema:
        #print "resolving reference"
        ref(schema["$ref"],schema,completions)
    #if "anyOf" in schema:
    #    for seq in schema["anyOf"]:
    #        ref(seq["$ref"],schema,completions)
    #if "allOf" in schema:
    #    for seq in schema["allOf"]:
    #        ref(seq["$ref"],schema,completions)
    #if "oneOf" in schema:
    #    for seq in schema["oneOf"]:
    #        ref(seq["$ref"],schema,completions)

def gen_completions(schema_file):
    global resolver
    with open(schema_file) as sf:
        sc = json.load(sf)
        resolver=RefResolver.from_schema(sc)
        #print "resolver:%s"%resolver
        completions=dict()
        complete(sc,completions)
        return completions

def match_completions(path, path_sep, schema_file):
    completions = gen_completions(schema_file)
    import pprint 
    pp = pprint.PrettyPrinter(indent=2)
    #pp.pprint(completions)

    paths = path.split(path_sep)
    paths = paths[1:]
    for p in paths:
        if not p == '':
            if p in completions['keys']:
                completions=completions[p]
            else:
                import re
                found = False
                for pt in completions['keypatterns']:
                    if re.match(pt,p):
                        found = True
                        completions=completions[pt]

    ret = {'keys': completions['keys'], 'keypatterns': completions['keypatterns'], 'values':completions['values'] }
    pp.pprint(ret)
    return ret

if __name__ == '__main__':
    match_completions('/volumes/xxx/external','/','./config_schema_v3.0.json')
    match_completions('/volumes/xxx','/','./config_schema_v3.0.json')
