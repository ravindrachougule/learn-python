names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]


#nested list that paired each name height and
nameHight = zip(names,heights)
print(nameHight)
print(list(nameHight))

#see inner list are actually tuple and don't have [] brackets

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners,dogs_names)
print(list(names_and_dogs_names))


for i in range(3):
  print(i)