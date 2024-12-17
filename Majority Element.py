def findMajority(arr):
    n = len(arr)
    res = []
    for i in range(n):
        cnt = 0
        for j in range(i, n):
            if arr[j] == arr[i]:
                cnt += 1
        if cnt > (n // 3):
            if len(res) == 0 or arr[i] != res[0]:
                res.append(arr[i])
        if len(res) == 2:
            if res[0] > res[1]:
                res[0], res[1] = res[1], res[0]
            break
    return res
if __name__ == "__main__":
    arr = [2, 2, 3, 1, 3, 2, 1, 1]
    res = findMajority(arr)
    for ele in res:
        print(ele, end=" ")