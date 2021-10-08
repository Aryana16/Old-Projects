def DFS(friends_matrix, v, found):
    L = len(friends_matrix)
    for i in range(L):
        if friends_matrix[v][i] == "Y" and not found[i]:
            found[i] = True
            DFS(friends_matrix, i, found)

def count_friend_circles(friends_matrix):
    num_circles = 0
    L = len(friends_matrix)
    found = [0] * L
    for i in range(L):
        if not found[i]:
           found[i] = 1
           DFS(friends_matrix, i, found)
           num_circles += 1
    return num_circles
