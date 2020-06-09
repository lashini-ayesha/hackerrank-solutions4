if __name__ == '__main__':
    clas =[]
    scor=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        clas.append([name, score])
        scor.append(score)

scor = list(set(scor))
b=sorted(scor)[1] 

for a,c in sorted(clas):
    if c==b:
        print(a)
      
