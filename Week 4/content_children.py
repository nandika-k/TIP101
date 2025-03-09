def find_content_children(s, g):
    p1 = p2 = 0
    count = 0
    while p1 < len(g):
      if s[p1] >= g[p2]:
        count += 1
      p1 += 1
      p2 += 1
    return count
    
g = [1, 2, 3]
s = [1, 1, 3]
print(find_content_children(s, g))
g = [1, 1]
s = [2, 2, 2]
print(find_content_children(s, g))