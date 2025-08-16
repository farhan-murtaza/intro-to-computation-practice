x=24.43452
y=24

print( "x={} and y={}".format(x,y))

print( "x=%.2f and y=%d" % (x, y))



l = [1, 98, 23, 198]
for i in l:
    print("%03d" % i)      # we can use 0-padding 

for i in l:
    print("{:03}".format(i))



s = "Test"
print("[%s]" %s)
print("={:>10}=".format(s))