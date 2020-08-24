'''
   Examples:

   accum("abcd") -> "A-Bb-Ccc-Dddd"
   accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
   accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''

def accum(s):
   return "-".join([(x*(i+1)).capitalize() for i, x in enumerate(s)])


print(accum("ZpglnRxqenU"))