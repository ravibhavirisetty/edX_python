def vowelCount(s):
   count = 0
   for i in s:
      test = 'aeiou'
      if i in test:
         count += 1
   return count

s = raw_input('Enter a string to know the number of vowels in it: ')

print 'Number of vowels: ' + str(vowelCount(s))