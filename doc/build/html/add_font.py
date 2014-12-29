import os

to_add = "<link href='http://fonts.googleapis.com/css?family=PT+Sans' "
to_add += "rel='stylesheet' type='text/css'>\n"


files = os.listdir('.')

for f in files:
    if f.endswith('.html') and f[0] in ['0', 'i']:
        os.rename(f, f + '_old')
        r = open(f + '_old', 'r').readlines()
        r = [l.replace('65p6tn4p8i', 'token') for l in r]
        r = [l.replace('hilpisch13', 'username') for l in r]
        r = [l.replace('henrynikolaus06', 'password') for l in r]
        n = open(f, 'w')
        n.writelines(r[:12])
        n.write(to_add)
        n.writelines(r[12:])
        n.close()

for f in files:
    if f.endswith('.html_old'):
        os.remove(f)