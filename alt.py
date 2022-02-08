string = input()

num = []
count = 0
for i in string:
    if i.isalpha():
        continue
    elif i.isdigit():
        num.append(int(i))
    else:
        count+=1
 
even = list(filter(lambda x:x%2 == 0,num))
odd = list(filter(lambda x:x%2 != 0,num))

if count&1 == 1:
    odd,even = even,odd
   
for i in range(max(len(even),len(odd))):
    if i < len(even):
        print(even[i],end=" ")
    if i < len(odd):
        print(odd[i],end=" ") 
