#!/usr/bin/python
# coding: utf-8

# In[89]:

import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime
import numpy as np
import parser


# In[90]:

months = dates.MonthLocator()  # every month
days = dates.DayLocator()
monthFmt = dates.DateFormatter('%b')
dayFmt = dates.DateFormatter('%d/%m')
fig, ax = plt.subplots()
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthFmt)
ax.xaxis.set_minor_locator(days)
ax.xaxis.set_minor_formatter(dayFmt)
ax.autoscale_view()


# In[91]:

file=open("scripts/wordcount.txt")


# In[92]:

file.seek(0)
data=np.array([x.rsplit() for x in file])


# In[93]:

datelist=data[:,0]
nwords=data[:,1]


# In[94]:

parseddates=[datetime.datetime.strptime(date, "%Y-%m-%d:%H:%M:%S") for date in datelist]


# In[95]:

ax.plot_date(parseddates,nwords,'-o')
fig.autofmt_xdate()
plt.savefig('scripts/phdwordcount.pdf', bbox_inches='tight', pad_inches=1)


# In[ ]:
