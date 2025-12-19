# Creating the dict
user={}

user['id']=1

# Accessing value using get()
key_val=user.get('id')
print(key_val)

# Safely accessed the key which doesn't exist
val=user.get('name', 'name is not a key here')
print(val)