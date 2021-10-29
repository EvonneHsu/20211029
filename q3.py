N=int(input())
for i in range (2,N):
if N % i ==0:
print(N,"不是質數")
break
else:
print(N,"是質數")
