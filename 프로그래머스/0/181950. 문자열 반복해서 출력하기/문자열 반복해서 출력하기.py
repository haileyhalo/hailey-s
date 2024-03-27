str, n = input().strip().split(' ')
n = int(n)
if len(str) >= 1 and len(str) <= 10 and n >= 1 and n <= 5: 
    repeat = str*n
    print(repeat)
    
else : 
    print("다시 입력")