''' Instructions:
================================================================================================== C H A L L E N G E =========================================================================================================================
Fizz Buzz is a children's word game that teaches division. It's also a classic technical interview question at countless companies. 🐝

Though this challenge may appear simple to experienced coders, it is designed to weed out 90% of job candidates who cannot apply their coding knowledge to a new problem creatively. Want to give it a try?

Create a fizz_buzz.py program that outputs numbers from 1 to 100.

Here's the catch:

    For multiples of 3, print "Fizz" instead of the number.
    For multiples of 5, print "Buzz" instead of the number.
    Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".

The output should look like:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...

Btw, it's totally okay if you can't get this one... it's a tough problem! Take a look at the solution below '''

#========================================================================================= C O D E - I N - P Y T H O N ====================================================================================================================

#fizz buzz.py
print("========================================= FIZZ BUZZ =====================================")

for num in range(1, 101):
  #num = int(input("enter the value from 1-100 : "))
 if num % 3 == 0 and num % 5 == 0:
  print("FizzBuzz")
 elif num % 3 == 0:
   print("Fizz")
 elif num % 5 == 0:
   print("Buzz")
 else:
   print(num)    



#============================================================================================= o u t p u t - i n - t e r m i n a l =========================================================================================================

========================================= FIZZ BUZZ =====================================
''' 
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
'''
