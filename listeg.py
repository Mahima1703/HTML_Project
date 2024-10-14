list= []
a=int(input("Enter a no. of elements"))

for i in range(0,a):
    g=int(input("Enter a value -"))
    list.append(g)
largest=list[0]

smallest=list[0]

for i in list:
    print(i)
    if i > largest:

        largest = list

    if i < smallest:

        smallest = list

print("Largest element is ",largest) 
print("Smallest element is", smallest)