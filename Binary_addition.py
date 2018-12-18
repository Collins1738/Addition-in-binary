def add_binary(num1, num2):
  list_a=[num1, num2]
  if list_a.count("0")==2:
    return "0"
  elif list_a.count("0")==1:
    return "1"
  elif list_a.count("0")==0:
    return "10"

def long_add(num1, num2): #num1 and 2 are strings
  if len(num1)==len(num2)==1:
    return add_binary(num1, num2)
  else:
    str_numss=balance_length(num1, num2)
    list_numss=str_numss.split(" ")
    num1=list_numss[0]
    num2=list_numss[1]
    index=len(num1)-1
    Answer=[]
    carry="0"
    while index>-1:
      ans=long_add(num1[index], num2[index])
      ans=long_add(ans, carry)
      if len(ans)>1:
        Answer.append(ans[len(ans)-1])
        carry=ans[0]
      elif len(ans)==1:
        Answer.append(ans[0])
        carry="0"
      index-=1
    Answer.append(carry)
    Answer=Answer[::-1]
    Answer="".join(Answer)
    return str(int(Answer))

def balance_length(num1, num2):
  if len(num1)==len(num2):
    return num1+" "+num2
  elif len(num1)<len(num2):
    amount=len(num2)-len(num1)
    while amount>0:
      num1="0"+num1
      amount-=1
    return num1+" "+num2
  elif len(num2)<len(num1):
    amount=len(num1)-len(num2)
    while amount>0:
      num2="0"+num2
      amount-=1
    return num1+" "+num2

# print(long_add("1", "10"))


# This program adds numbers in binary
# x=input("Type the first number you wish to add")
number=int(input("Type in the number of binary numbers you wish to add\n"))
list_numbers=[]
count=0
print("Type in each binary number, after each number, press Enter, then type the next")
while count<number:
  x=input()
  list_numbers.append(x)
  count+=1
index=len(list_numbers)-1

while index>0:
  x=long_add(list_numbers[index], list_numbers[index-1])
  list_numbers[index-1]=x
  list_numbers.pop(index)
  index-=1

print(list_numbers[index])
