def sottrazione(x,y):
    return x - y

def sottrazione_infallibile(x=1 , y=1):
    return x - y

print("Sottrzione: ", sottrazione(10, 5))
print("Sottrazione:", sottrazione (x= 10, y = 5))
print("Sottrazione infallibile:", sottrazione_infallibile(10))
print("Sottrazione infallibile:", sottrazione_infallibile(10, 5), sep="")
print("Sottrazione infallibile:", sottrazione_infallibile(5, y=10))
print("Sottrazione infallibile:", sottrazione_infallibile(y=5))
