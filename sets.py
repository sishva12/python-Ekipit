set1={"banana","kiwi","pineapple","apple"};
set1.add("grape");
print(set1);
set1.remove("banana");
print(set1);
set2 = {"a", "b" , "c"}
set3 = {1, 2, 3}

set4 = set2.union(set3)
print(set4);
setx = {"a", "b" , "c"}
sety = {1, 2, 3}

setx.update(sety)
print(setx)
fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y) 

print(x)
fruits1 = {"apple", "banana", "cherry"}

fruits1.discard("banana")

print(fruits1)
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}

z1 = x1.intersection(y1)

print(z1)
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}

x2.intersection_update(y2)

print(x2)

x3 = {"apple", "banana", "cherry"}
y3 = {"google", "microsoft", "facebook"}

z3 = x3.isdisjoint(y3)

print(z3)
x4 = {"a", "b", "c"}
y4 = {"f", "e", "d", "c", "b", "a"}

z4 = x4.issubset(y4)

print(z4)
x5 = {"f", "e", "d", "c", "b", "a"}
y5 = {"a", "b", "c"}

z5 = x5.issuperset(y5)

print(z5)
fruits6 = {"apple", "banana", "cherry"}

fruits6.pop()

print(fruits6)
x7 = {"apple", "banana", "cherry"}
y7 = {"google", "microsoft", "apple"}

z7 = x7.symmetric_difference(y7)

print(z7)

fruitsy = {"apple", "banana", "cherry"}

fruitsy.remove("banana")

print(fruitsy)





