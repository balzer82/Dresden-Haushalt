# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import seaborn as sns
sns.set_style("whitegrid")
%matplotlib inline

# <codecell>

data = pd.read_csv('./876d8fd0190df52ffb4c/haushaltsentwurf-2015_16.csv')

# <codecell>

data.tail(50)

# <headingcell level=2>

# Ab hier nur 2015!

# <codecell>

data2015 = data[data.time==2015]
data2015.head(5)

# <headingcell level=2>

# Direction

# <codecell>

def calcAnsatz(df):
    if df.direction=='Ertrag':
        return np.round(df['amount']/1e6, 2)
    elif df.direction=='Aufwendung':
        return np.round(1.0*df['amount']/1e6, 2)

# <codecell>

data2015['Ansatz'] = data2015.apply(calcAnsatz, axis=1)

data = data2015[['part-id', 'part-name', 'group-name', 'subgroup-name', 'row-name', 'Ansatz']]
data.columns = (['Produktbereich', 'Produktbereichsbezeichnung','Produktbezeichnung','Unterproduktbezeichnung', 'Amtsbudget','Ansatz'])

# <codecell>

data.head(20)

# <codecell>


# <codecell>


# <codecell>


# <codecell>

geldfluss = data.sort(['Ansatz'])

# <codecell>

top10minus = geldfluss.head(10)
top10minus

# <codecell>

top10plus = geldfluss.tail(10)
top10plus

# <codecell>


# <codecell>


# <codecell>

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12,8))
top10plus.plot(x='Produktbezeichnung', y='Ansatz', kind='barh', label='', ax=axes[0], title='Top 10 Einnahmen (in mio EUR)', color='#2ecc71')
top10minus.plot(x='Produktbezeichnung', y='Ansatz', kind='barh', label='', ax=axes[1], title='Top 10 Ausgaben (in mio EUR)', color='#e74c3c')
plt.tight_layout()
plt.savefig('Top10.png')

# <codecell>

Produktbereiche = data.groupby(['Produktbereichsbezeichnung','Produktbezeichnung'], sort=True)
Produktbereiche.sum()

# <codecell>

Produktbereiche.sum().to_csv('Haushaltsentwurf2015-Produktbereiche.csv', drop_index=True, float_format='%.2f')

# <headingcell level=2>

# Amtsbudgets

# <headingcell level=3>

# Barplots

# <codecell>

for i, ((Produktbereichsbezeichnung, Produktbezeichnung), group) in enumerate(Produktbereiche):
    colors = sns.blend_palette(["red", "mediumseagreen"], len(group['Ansatz']))

    Amtsa = group.sort('Ansatz')
    Amtsa.index = [s[:80] for s in Amtsa.Amtsbudget] # zu lange Namen shorten
    
    Amtsa['Ansatz'].plot(kind='barh', figsize=(10, 0.2*len(Amtsa)), label='', color=colors, title=Produktbezeichnung.decode('utf-8'))

    plt.tight_layout()
    plt.savefig('Amtsbudgets-%02d-%s.png' % (i, Produktbezeichnung), transparent=True)
    plt.close()

# <headingcell level=3>

# Pie Plots

# <codecell>


# <codecell>

for i, ((Produktbereichsbezeichnung, Produktbezeichnung), group) in enumerate(Produktbereiche):

    Amtsa = group.sort('Ansatz')
    Amtsa.index = [s[:80] for s in Amtsa.Amtsbudget] # zu lange Namen shorten
        
    plt.figure(figsize=(12,6))

    # Einnahmen
    plt.subplot(121)
    colors = sns.color_palette("pastel", len(Amtsa['Ansatz'][Amtsa.Ansatz>0.0]))
    p,t = plt.pie(Amtsa['Ansatz'][Amtsa.Ansatz>0.0], labeldistance=0.8, startangle=20, colors=colors)
    label = Amtsa['Ansatz'][Amtsa.Ansatz>0.0].index
    plt.legend(p, [l[:70].decode('utf-8') for l in label], loc="lower left")

    # Ausgaben
    plt.subplot(122)
    colors = sns.color_palette("pastel", len(Amtsa['Ansatz'][Amtsa.Ansatz<0.0]))
    p, t = plt.pie(-1.0*Amtsa['Ansatz'][Amtsa.Ansatz<0.0], labeldistance=0.8, startangle=20, colors=colors)
    label = Amtsa['Ansatz'][Amtsa.Ansatz<0.0].index
    plt.legend(p, [l[:70].decode('utf-8') for l in label], loc="lower left")

    # Annotations
    plt.text(-1.3, 1.2, Produktbezeichnung.decode('utf-8'), fontsize=16, ha='center')
    plt.text(-2.5, 1.08, 'Einnahmen', fontsize=12, ha='center')
    plt.text(0, 1.08, 'Ausgaben', fontsize=12, ha='center')
    
    plt.tight_layout()
    
    plt.savefig('Amtsbudgets-%02d-%s-Pie.png' % (i, Produktbezeichnung), transparent=True)
    plt.close()    

# <headingcell level=2>

# Gesamtübersicht Haushaltsentwurf

# <codecell>

ProduktbereicheSort = Produktbereiche.sum().sort('Ansatz')
ProduktbereicheSort

# <codecell>

ProduktbereicheSort.to_csv('Haushaltsentwurf2015.csv', drop_index=True, float_format='%.2f')

# <codecell>


# <codecell>

colors = sns.blend_palette(["red", "mediumseagreen"], len(Produktbereiche))
ProduktbereicheSort['Ansatz'].plot(kind='barh', figsize=(14,20), color=colors, label='', title='Dresden Entwurf Haushaltsplan 2015 (in mio EUR)')
plt.axvline(Produktbereiche['Ansatz'].sum().mean(), alpha=0.6)
plt.tight_layout()
plt.savefig('Haushaltsentwurf2015.png', dpi=150, transparent=True)

# <codecell>


# <codecell>


# <codecell>


# <codecell>


