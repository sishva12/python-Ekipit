#tuple=("banana","apple","apple");
#print(tuple.count("apple"));
#print(tuple.index("banana"));
x = ("apple", "banana", "cherry");
y = list(x);
y[1] = "kiwi";
x = tuple(y);

print(x);
a=(1,2,3,4,5,4);
b=(11,12,1,3);
z=a+b;
print(z);