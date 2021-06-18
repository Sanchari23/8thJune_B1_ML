Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6 == 6
True
>>> a=20;
>>> a+=30;
>>> a%=3;
>>> print(a)
2
>>> True*False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> 
>>> 
>>> 
>>> #Q3-
>>> s1 = "Nice to have it"
>>> s2 = "here"
>>> print( s1 + " " + s2 )
Nice to have it here
>>> 
>>> 
>>> 
>>> #Q4-
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> print(a[3][1][2][0])
hello
>>> 
>>> 
>>> 
>>> #Q5-
>>> s1 = "Nice to have it"
>>> s2 = "here"
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a.insert(0,s1)
>>> a.append(s2)
>>> print(a)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> 
>>> 
>>> 
>>> #Q6-
>>> color_list_1 = set(["White","Black","Red"])
>>> color_list_2 = set(["Red","Green"])
>>> print(color_list_1 - color_list_2 )
{'Black', 'White'}
>>> 
>>> 
>>> 
>>> #Q7-
>>> import string
>>> def ispangram(str):
	alphapet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in str.lower():
			return False
		return True
	string = 'the quick brown fox jumps over the lazy dog'
	if (ispangram(string) == True):
		print("YES")
	else:
		print("NO")

		
>>> def ispangram(str):
	alphapet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in str.lower():
			return False
		return True
	string = 'the quick brown fox jumps over the lazy dog'
	if (ispangram(string) == True):
		print("YES")
	else:
		print("NO")

		
>>> 
>>> 
>>> 
>>> #Q8-
>>> a = int(input("enter an integer:"))
enter an integer:5
>>> n1 = int("%s" %a)
>>> n2 = int("%s%s" % (a,a))
>>> n3 = int("%s%s%s" % (a,a,a))
>>> value = n1 + n2 + n3
>>> print(value)
615
>>> 
>>> 
>>> 
>>> #Q9-
>>> items = input("Input comma separeted sequence of words")
Input comma separeted sequence of words without,hello,bag,world
>>> words = [word  for word in items.split(",")]
>>> print(",".join(sorted(list(set(words)))))
 without,bag,hello,world
>>> items = input("Enter comma separeted sequence of words :")
Enter comma separeted sequence of words : without, hello, bag, world
>>> words = [word  for word in items.split(",")]
>>> print(",".join(sorted(list(set(words)))))
 bag, hello, without, world
>>> 
>>> 
>>> 
>>> #Q10-
>>> d = {'Student': ["Rahul", "Kishore", "Vidhya", "Raakhi"], "Marks": [57,87,67,79]}
>>> print(d["student"][1])
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    print(d["student"][1])
KeyError: 'student'
>>> d = {'Student': ["Rahul", "Kishore", "Vidhya", "Raakhi"], "Marks": [57,87,67,79]}
>>> print(d['student'][1])
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    print(d['student'][1])
KeyError: 'student'
>>> d = {'Student': ["Rahul", "Kishore", "Vidhya", "Raakhi"], "Marks": [57,87,67,79]}
>>> print(d['Student'][1])
Kishore
>>> 