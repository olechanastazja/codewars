import re

'''
    As breadcrumb menùs are quite popular today, I won't digress much on explaining them, leaving the wiki link to do all the dirty work in my place.
    
    What might not be so trivial is instead to get a decent breadcrumb from your current url. For this kata, your purpose is to create a function that takes a url, strips the first part (labelling it always HOME) and then builds it making each element but the last a <a> element linking to the relevant path; last has to be a <span> element getting the active class.
    
    All elements need to be turned to uppercase and separated by a separator, given as the second parameter of the function; the last element can terminate in some common extension like .html, .htm, .php or .asp; if the name of the last element is index.something, you treat it as if it wasn't there, sending users automatically to the upper level folder.
    
    A few examples can be more helpful than thousands of words of explanation, so here you have them:
    
    generate_bc("mysite.com/pictures/holidays.html", " : ") == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
    generate_bc("www.codewars.com/users/GiacomoSorbi", " / ") == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
    generate_bc("www.microsoft.com/docs/index.htm", " * ") == '<a href="/">HOME</a> * <span class="active">DOCS</span>'
    
    Seems easy enough?
    
    Well, probably not so much, but we have one last extra rule: if one element (other than the root/home) is longer than 30 characters, you have to shorten it, acronymizing it (i.e.: taking just the initials of every word); url will be always given in the format this-is-an-element-of-the-url and you should ignore words in this array while acronymizing: ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]; a url composed of more words separated by - and equal or less than 30 characters long needs to be just uppercased with hyphens replaced by spaces.
    
    Ignore anchors (www.url.com#lameAnchorExample) and parameters (www.url.com?codewars=rocks&pippi=rocksToo) when present.
'''
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


