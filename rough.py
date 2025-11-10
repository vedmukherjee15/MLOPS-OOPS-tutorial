from oops_proj import chatbook

# Ensure IDs restart from zero for each run of this script


user1 = chatbook()
print(user1.id)

# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)

# using static method directly from class raather than object
chatbook.set_id(10)
user2 = chatbook()
print(user2.id)


