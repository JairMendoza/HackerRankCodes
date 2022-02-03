s = 'babb' 
n = 15

count = s.count( "a" )  *  ( n  //  len ( s ))
count += s [: n  %  len ( s )] . count ( "a" )

print(count)
print(count)