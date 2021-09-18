# wapf to check if the given 
# number is even or odd

def check(num):
	if num % 2 == 0:
		return " yes"
	else:
		return "no"
num = int(input(" enter a number "))
ans = check(num)
print("ans = ", ans)