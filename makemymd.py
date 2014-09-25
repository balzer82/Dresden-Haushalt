# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os

# <codecell>

f=open('README.md','w')

# <codecell>

prestring="""
# Haushaltsentwurf Dresden 2015/2016
Gemacht mit einem Offenen Haushalt*
--------

*nein, eigentlich nicht, denn er ist in Dresden noch nicht offen

## Haushaltsentwurf 2015 (in mio EUR)

"""
f.write(prestring)

# <codecell>

baseurl = '![Abbildung](https://raw.githubusercontent.com/balzer82/Dresden-Haushalt/master/'
figs=[]
for path, dirs, files in os.walk('.'):
    for fileName in files:
        if fileName.endswith('.png'):
            
            figs.append(baseurl + fileName + ')')

figs.sort()
figs.reverse()

figstring='\n\n'.join(figs)
f.write(figstring)

# <codecell>

poststring ="""
## Datenquelle
[PDF Scraper](https://gist.github.com/Mic92/876d8fd0190df52ffb4c)

## Kontakt

[Open Knowledge Foundation / OKLab Dresden](http://OKDD.de)

## Disclaimer

*Kein Anspruch auf Richtigkeit!*
"""
f.write(poststring)
f.close()

print('Done.')

# <codecell>


