#creating a list
my_list = []

#appending 10, 20, 30, 40,

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting 15 to the list

my_list.insert(1, 15)

#extending my_list

my_list.extend([50, 60, 70])

#removing last element
my_list.pop()

#sorting my_list
my_list.sort()

#index of value 30

print(f"Index of 30: {my_list.index(30)}")
