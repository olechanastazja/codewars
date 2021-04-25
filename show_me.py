# create the function show_me
def show_me(instname):
    attrs = sorted(instname.__dict__.keys())
    if len(attrs) < 2:
        attrs_result = attrs[0]
    else:
        attrs_result = []
        for k in attrs[:-1]:
            attrs_result.append(k)
        attrs_result = ", ".join(attrs_result) + " and " + attrs[-1]
    info = f"Hi, I'm one of those {instname.__class__.__name__}s! Have a look at my {attrs_result}."
    return info
