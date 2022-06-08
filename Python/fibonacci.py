


n=int(input("Introduce numero para fibonacci: "))
#los primeros dos terminos son el primero y el ultimo
first=0
second=1
sum=0
count=1
print("Seuencia Fibonacci: ")

while(count<=n):    
  print(sum)
  count+=1
  first=second
  second=sum
  sum=first+second