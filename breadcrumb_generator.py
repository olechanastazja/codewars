import re

HOME = 'HOME'
SPAN = '<span class="active">{}</span>'
ENDINGS = ['.html', '.htm', '.asp', '.php']
ANCHORS_PARAMS = ['#', '?']
TO_IGNORE = ["the", "of", "in", "from", "by", "with", "and", "for", "or", "to", "at", "a"]


def generate_bc(url, separator):
    LINK = '<a href="{}">{}</a>' + separator
    result = ""
    path = ""
    url_r = remove_redundant(url)
    d = {k: v for k, v in enumerate(url_r.split('/'))}
    for k, v in d.items():
        if len(d) == 1:
            return SPAN.format(HOME)
        str_v = create_acronym(v) if len(v) > 30 else v
        str_v = str_v.replace('-', ' ').upper()
        if k == 0:
            result += LINK.format('/', HOME)
        elif k == len(d) - 1:
            result += SPAN.format(str_v)
        else:
            path += v + '/'
            result += LINK.format('/' + path, str_v)
    return result


def remove_redundant(txt):
    txt = check_anchor_and_params(txt)
    txt = remove_http(txt)
    if txt.endswith('/'):
        txt = re.sub('/$', '', txt)
    if is_index(txt):
        return "/".join(txt.split('/')[:-1])
    txt = shorten_ending(txt)
    return txt


def remove_http(txt):
    if re.match('^http[s]?://', txt):
        txt = re.sub('http[s]?://', '', txt)
    return txt


def shorten_ending(txt):
    for s in ENDINGS:
        if s in txt:
            txt = re.sub(s, "", txt)
    return txt


def check_anchor_and_params(txt):
    for o in ANCHORS_PARAMS:
        if o in txt:
            txt = txt.split(o, 1)[0]
    return txt


def is_index(txt):
    return 'index' in txt.split('/')[-1]


def create_acronym(txt):
    txt = re.sub('-', ' ', txt)
    return "".join([s[0].upper() for s in txt.split(' ') if s not in TO_IGNORE])


print(generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", '*'))
print(generate_bc("http://www.google.ca/skin-meningitis-surfer-pippi/in-bioengineering-research-a-paper-by-insider-diplomatic/index.htm?favourite=code", " * "))
print(generate_bc('https://www.google.ca/paper-cauterization-or-pippi-to-kamehameha/insider-surfer-in-skin-bed-paper-meningitis/most-viewed/to-bed-', ':'))
print(generate_bc('google.ca/users/of-transmutation-or-surfer-immunity/for-cauterization-bladder-research/issues/index.php?favourite=code', ':'))


