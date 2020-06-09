if __name__ == '__main__':
     n = int(input())
     arr = list(map(int, input().split()))
first = max(arr)

for x in range(n):
    if first == max(arr):
        arr.remove(max(arr))

print(max(arr))
