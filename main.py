import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

map = [[0, 3, 1, 1, 1, 2, 2, 1, 1, 3, 1],
       [2, 1, 2, 2, 2, 1, 3, 3, 2, 1, 2],
       [1, 3, 1, 1, 3, 1, 2, 1, 3, 1, 1],
       [2, 3, 1, 1, 1, 2, 1, 3, 1, 10, 2],
       [1, 3, 2, 1, 2, 1, 2, 1, 2, 1, 3],
       [1, 3, 1, 1, 1, 3, 3, 1, 3, 1, 3],
       [3, 1, 1, 2, 1, 10, 1, 2, 1, 3, 1],
       [3, 2, 3, 1, 2, 1, 3, 1, 1, 2, 1],
       [1, 1, 1, 1, 2, 1, 1, 3, 2, 1, 3],
       [1, 1, 2, 3, 1, 2, 1, 1, 1, 2, 1],
       [3, 2, 1, 1, 2, 3, 2, 1, 3, 3, 0],
       ]
map = np.array(map)

waypoints =[]
index = 0
for i in range(11):
    for j in range(11):
        if map[i, j] == 0 and i != 0 and i != 10 and j != 10 and j != 10:
            new=[]
            new.append(i)
            new.append(j)
            waypoints.append(new)

waypoints=np.array(waypoints)
fig, ax = plt.subplots(figsize=(8, 8))
min_val, max_val = 0, 10




ax.matshow(map, cmap=plt.cm.Blues, vmin=0, vmax=40)


for i in range(11):
    for j in range(11):
        c = map[j, i]
        ax.text(i, j, str(c), va='center', ha='center')

distmap = np.ones((11, 11), dtype=int) * np.Infinity
distmap[0, 0] = 0
originmap = np.ones((11, 11), dtype=int) * np.nan
visited = np.zeros((11, 11), dtype=bool)
finished = False
x, y = int(0), int(0)
count = 0

# Loop Dijkstra until reaching the target cell
while not finished:
    # move to x+1,y
    if x < 11 - 1:
        if distmap[x + 1, y] > map[x + 1, y] + distmap[x, y] and not visited[x + 1, y]:
            distmap[x + 1, y] = map[x + 1, y] + distmap[x, y]
            originmap[x + 1, y] = np.ravel_multi_index([x, y], (11, 11))
    # move to x-1,y
    if x > 0:
        if distmap[x - 1, y] > map[x - 1, y] + distmap[x, y] and not visited[x - 1, y]:
            distmap[x - 1, y] = map[x - 1, y] + distmap[x, y]
            originmap[x - 1, y] = np.ravel_multi_index([x, y], (11, 11))
    # move to x,y+1
    if y < 11 - 1:
        if distmap[x, y + 1] > map[x, y + 1] + distmap[x, y] and not visited[x, y + 1]:
            distmap[x, y + 1] = map[x, y + 1] + distmap[x, y]
            originmap[x, y + 1] = np.ravel_multi_index([x, y], (11, 11))
    # move to x,y-1
    if y > 0:
        if distmap[x, y - 1] > map[x, y - 1] + distmap[x, y] and not visited[x, y - 1]:
            distmap[x, y - 1] = map[x, y - 1] + distmap[x, y]
            originmap[x, y - 1] = np.ravel_multi_index([x, y], (11, 11))

    visited[x, y] = True
    dismaptemp = distmap
    dismaptemp[np.where(visited)] = np.Infinity
    # now we find the shortest path so far
    minpost = np.unravel_index(np.argmin(dismaptemp), np.shape(dismaptemp))
    x, y = minpost[0], minpost[1]
    if x == 11 - 1 and y == 11 - 1:
        finished = True
    count = count + 1

# Start backtracking to plot the path
mattemp = map.astype(float)
x, y = 11 - 1, 11 - 1
path = []
mattemp[int(x), int(y)] = np.nan

while x > 0.0 or y > 0.0:
    path.append([int(x), int(y)])
    xxyy = np.unravel_index(int(originmap[int(x), int(y)]), (11, 11))
    x, y = xxyy[0], xxyy[1]
    mattemp[int(x), int(y)] = np.nan
path.append([int(x), int(y)])

# Output and visualization of the path
current_cmap = plt.cm.Blues
current_cmap.set_bad(color='red')

#current_cmap.waypoints(color='green')
fig, ax = plt.subplots(figsize=(8, 8))
ax.matshow(mattemp, cmap=plt.cm.Blues, vmin=0, vmax=20)
for i in range(11):
    for j in range(11):
        c = map[j, i]
        ax.text(i, j, str(c), va='center', ha='center')

print('The path length is: ' + str(distmap[11 - 1, 11 - 1]))
plt.show()