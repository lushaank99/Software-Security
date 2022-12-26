import os
from xml.dom.minidom import parseString
import csv
import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
from collections import Counter as ct

permission_count = {}  # number of times a permission is used
permission_max = {}  # number of permissions an app uses

with open('Permission_Data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for app_info in reader:
        m = 0
        for info in app_info:

            # number of permissions in an APP

            if info.__contains__('.permission') or  info.__contains__('_PERMISSION'):
                m += 1

            # number of times a permission is used

                if info in permission_count:
                    permission_count[info] += 1
                else:
                    permission_count[info] = 1
        permission_max[app_info[0]] = m

reverse_sort_permissioncount = lambda permissioncount_pair: \
    permissioncount_pair[1]
print ('top 10 most used permissions')
reverse_sorted_permissioncount = sorted(permission_count.items(),
        key=reverse_sort_permissioncount, reverse=True)


def take(n, iterable):
    '''Return first n items of the iterable as a list'''

    return dict(islice(iterable, n))


top_10_most_used_permissions = take(10, reverse_sorted_permissioncount)

for (keys, value) in top_10_most_used_permissions.items():
    print (keys)

reverse_sort_permissionmax = lambda permissionmax_pair: \
    permissionmax_pair[1]

print ('Top 10 apps with most permissions')
reverse_sorted_permissionmax = sorted(permission_max.items(),
        key=reverse_sort_permissionmax, reverse=True)
top_10_apps_with_most_permissions = take(10,
        reverse_sorted_permissionmax)

for (keys, value) in top_10_apps_with_most_permissions.items():
    print (keys)
d = dict(ct(permission_max.values()))

plot_data = sorted(d.items())
print(plot_data)
plt.plot(*zip(*plot_data))
plt.show()
