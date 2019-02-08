
lucky_numbers =[1,3,5,4,6]
friends = ["Kevin","John","Jenny","Amy","Chris"]


friends[4] = "Owen"
print(friends[-2])
print(friends[1:3])

friends.extend(lucky_numbers)

friends.append("Steve")
friends.insert(0,"Harry")

pop_value = friends.pop(1)

friends = ["Kevin","John","Jenny","Amy","Chris"]
friends.sort()
friends.sort(key = len, reverse = True)

print(friends[4])
print(friends)


