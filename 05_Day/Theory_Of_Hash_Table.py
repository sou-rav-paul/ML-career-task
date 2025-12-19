user={'id':1, 'name': 'Admin'}
# Safe Access (.get())
# Return None if key missing, prevents crash
email=user.get('email','No Email Found')
print(email)
# Iteration 
for key , val in user.items():
    print(f'{key}: {val}')