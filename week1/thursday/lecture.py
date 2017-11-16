#len(array) == array.length()

num = [1,2,3,4,5,6,7,8,9]

# #doubling
# print("Doubling")
# for i in range(0,len(num)):
#     print(num[i]*2)
#
# # squares
# # print("Squaring")
# # for i in range(0,len(num)):
# #     print(num[i]*num[i])
#
# #foreach loop
# print("foreach loop")
# for x in num:
#     print(x)

#append to array == array.push
num.append(10)
print num

#delete items
#unlike pop or unshift, you must specify position
del num[1]
del num[-1]
print num

#inserting at specific position
num.insert(4,"insertion")
print num
