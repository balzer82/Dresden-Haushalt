# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os

# <codecell>

f=open('README.md','w')

# <codecell>

prestring="""
# Haushaltsentwurf Dresden 2015/2016
Gemacht mit einem Offenem Haushalt*
--------

*nein, eigentlich nicht, denn er ist in Dresden noch nicht offen

## Haushaltsentwurf 2015 (in mio EUR)

"""
f.write(prestring)

# <codecell>

figs=[]
imgExts = ["png"]
for path, dirs, files in os.walk('.'):
    for fileName in files:
        ext = fileName[-3:].lower()
        if ext not in imgExts:
            continue
        else:
            figs.append('![Abbildung](https://github.com/balzer82/DresdenData/blob/master/' + fileName + '?raw=true)')
            
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

# <codecell>


