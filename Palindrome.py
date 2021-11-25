#Palindrome number check       

def isPalindrome(S):
		Stack=[]
		pal=0
		for i in S:
		    Stack.append(i)
		for char in S:
		    if char == Stack.pop():
		       pal = 1
		    else:
		       return 0
               
               
		return pal

ans=isPalindrome('malayalam')
print(ans)