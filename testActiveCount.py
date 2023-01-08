
import json
# a='{"Index":"","FlagConfig":2}{"Index":"","FlagConfig":1,"Status":"01"}{"Index":"","CheckConnection":0}'
# z=a.count("}{")
# x=a[:(a.rfind("}{")+1)]
# # x=a[a.index("}{"):]
# y=x[(x.rfind("}{")+1):]


# # y=x[1:]
# # z=y[(y.rfind("}")+1):]

# print('a',a)
# print('z',z==2)

# print('x',y)
a='{"Index":"z","FlagConfig":2}{"Index":"891256123","FlagConfig":1,"Status":"01"}'
x=a.replace("}{","},{")
x="["+x+"]"
z=json.loads(x)

for i in z:
    if i['FlagConfig'] == 1:
        print(type(i))
        
        break

# x=a[(a.rfind("}{")+1):]




# y=x[1:]
# z=y[(y.rfind("}")+1):]

# print('a',a)


# print('x',x)
# print('z',z)


# print('aa',y["Index"])


