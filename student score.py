sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
totalmarks=sub1+sub2+sub3+sub4+sub5
percentage=totalmarks/500*100
print(percentage)
if percentage>=75:
    print("grade A")
elif percentage>=60 and percentage<=74:
    print("grade B")
elif percentage>=35 and percentage<=59:
    print("grade C")
else:
    print("fail")