from random import randint

def head_or_tail(array):
	index=randint(-1,0)
	return array[index]

a=head_or_tail(["foo", "bar", "claude"])
b=head_or_tail([0,1])
c=head_or_tail([["foo"],["bar"], ["claude"]])
print(a)
print(b)
print(c)
