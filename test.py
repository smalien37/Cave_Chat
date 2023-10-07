def maxPoints(points) -> int:
    m,mi = {},-1e9
    for i in range(len(points) - 1):
        for j in range(i+1,len(points)):
            if (points[j][0] - points[i][0]) == 0:
                r = points[j][0]
            else: r =  (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
            m[r] = 1 + m.get(r,0)
    
    for j in m:
        mi = max(mi,m[j])

    print(m)
    return mi
    //THIS IS TO CHECK WHETHER IT IS PULLING CORRECTLY!!!!!

print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
