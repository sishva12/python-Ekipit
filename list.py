list = [1,2,3,4,5,6,7,8];
print(len(list));
list1 = ["abc", 34, True, 40, "male"];
print(type(list1));
print(list1[3]);
#negative indexing
print(list1[-2]);
print(list1[1:3]);
print(list1[:3]);
print(list1[2:]);
print(list1[3:]);
print(list1[-3:-1]);
print(list1[-1:-3]);
list1.append("banana");
print(list1);
list1.clear();
print(list1);
x=list.copy();
print(x);
y=list.count(2);
print(y);
list3=[1,2,3,4];
list2=[11,12,13];
list3.extend(list2);
print(list3);
print(list3.index(11));
list3.insert(2,"banana");
print(list3);
list3.pop(2);
print(list3);
list3.remove(3);
print(list3);
list3.reverse();
print(list3);
list3.sort();
print(list3);

