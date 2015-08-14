def ordered_substring(s):
   sb = ''
   c = ''
   for char in s:
      if c == '':
         c = char
      elif c[-1] <= char:
         c += char
      elif c[-1] > char:
         if len(sb) < len(c):
            sb = c
            c = char
         else:
            c = char
   if len(c) > len(sb):
     sb = c
   return sb

s = raw_input('Enter a string to get the longest ordered substring: ')
print 'Longest ordered substring is: 'ordered_substring(s)