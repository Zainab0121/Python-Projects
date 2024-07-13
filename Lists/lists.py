lucky_numbers =[4, 8, 15, 16, 23, 42]
friends = ["Kelvn", "Karen", "Jim", "Oscar","Oscar" "Toby"]
friends[1] = "Mike"
print(friends[1:3])
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.pop()
friends.clear()
friends2 = friends.copy()
print(friends.index("Oscar"))
print(friends.count("Oscar"))
lucky_numbers.sort()
lucky_numbers.reverse()

print(friends)
print(lucky_numbers)

#Code might not work. This is just a summary of list functions