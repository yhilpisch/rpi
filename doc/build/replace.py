import os

rpl = {
    '65p6tn4p8i': 'token',
    'hilpisch13': 'username',
    'henrynikolaus06': 'password',
    'rpi@hilpisch.com': 'rpi@mydomain.net',
    'yves@mydomain.net': 'me@mydomain.net',
    'ftp://rpi:pythonquants@quant-platform.com': 'ftp://user:password@mydomain.net',
    'smtp.hilpisch.com': 'smtp.mydomain.net'
}

path = './html/'
files = os.listdir(path)

for f in files:
    if f.endswith('.html') or f.endswith('.py') or f.endswith('.conf'):
        r = open(path + f, 'r').readlines()
        e = []
        for l in r:
            for k, v in rpl.items():
                l.replace(k, v)
            e.append(l)
        # r = [[l.replace(k, v) for k, v in rpl.items()] for l in r]
        n = open(path + f, 'w')
        n.writelines(e)
        n.close()

for f in files:
    if f.endswith('.html_old'):
        os.remove(f)