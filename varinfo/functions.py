import types


def udir(o, 
    find = '',
    show_privates = False,
    show_builtins = False, ):
    """
    Uber dir
    Returns a list of attributes found on the object.
    Excludes built-in attributes (everything starting with __)
    Excludes private attributes (everything starting with _)
    To include private attributes, set show_privates=True
    To include builtin attributes, set show_builtins=True
    """
    attributes = dir(o)

    if not show_privates and not show_builtins:
        attributes = [a for a in attributes if not a.startswith('_')]
    elif show_privates and not show_builtins:
        attributes = [a for a in attributes if not a.startswith('__')]
    elif show_builtins and not show_privates:
        attributes = [a for a in attributes if not a[0] == '_' or a.startswith('__')]

    if find:
        attributes = grep(attributes,find)
    
    return attributes

def varinfo(o, 
    find = '',
    max_str_len=200,
    show_privates = False,
    show_builtins = False,
    
    ):
    """
    Variable info
    Returns a human-readable list of properties of the object
    To include private attributes, set show_privates=True
    To include builtin attributes, set show_builtins=True

    Will return the actual value of the following types:
    *str (capped at 200 per default)
    *int
    *bool
    Other datatypes are displayed as the name of their Class
    Functions are simply displayed as ()
    """
    ret = [] 
    
    attributes = udir(o,
    find=find,
    show_privates=show_privates,
    show_builtins=show_builtins,
    )

    for name in attributes:
        val = getattr(o,name)
        if isinstance(val,str):
            str_val = val[:max_str_len].replace(r'\n',r'\n')
            ret.append(
                f'{name}: str -> {str_val}')
            continue
        if isinstance(val,bool):
            ret.append(f'{name}: bool -> {val}')
            continue
        if isinstance(val,int):
            ret.append(f'{name}: int -> {val}')
            continue
        if isinstance(val, types.BuiltinFunctionType):
            ret.append(f'{name}()')
            continue
        if isinstance(val, types.FunctionType):
            ret.append(f'{name}()')
            continue
        """
        Todo: figure out these
        types.BuiltinMethodType
        types.MethodType
        types.FunctionType
        """
        ret.append(f'{name} -> {type(val)}')
    
    return ret

def grep(lst,search_str):
    """Return only the entries of a list
    that contain the search string.
    Similar to unix grep
    """
    ret = [entry for entry in lst if search_str in entry]
    return ret

def _exclude_non_capitalized(lst):
    """Returns all list elements that are capitalized"""
    ret = []
    for l in lst:
        if l[0].isupper():
            ret.append(l)
    return ret
    
def _find_type_match(obj):
    """Returns all types that the object matches"""
    ret = []
    all_types_names = udir(types)
    all_types_names = _exclude_non_capitalized(all_types_names)
    for t in all_types_names:
        type_obj = getattr(types,t)
        if isinstance(obj, type_obj):
            ret.append(type_obj)
    return ret
        

        
