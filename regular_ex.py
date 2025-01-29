import re
email_data="akshatharajshekar<akshatharajshekar@gmail.com>"
result= re.search(r"aksha", email_data)
print(result)

result = re.search(r"akshat", email_data)
print(result)

result = re.search(r"aks", email_data)
print(result)

result = re.search(r"aksh[r,j]", email_data)
print(result)

result = re.search(r"aksh[a-z]", email_data)
print(result)

result = re.search(r"aksha[a-z]{2}", email_data)
print(result)

result= re.search(r"aksh[a-z]+", email_data)
print(result)

result= re.search(r"aksh[a-z,A-Z,0-9]+", email_data)
print(result)

print("With search function")
result= re.search(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)

print("With find function")
result= re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)

print("------------")
result= re.findall(r"aks[a-zA-z@.]+", email_data)
print(result)

print("------------")
result= re.search(r"aks[a-zA-z@.]+", email_data)
print(result)


print("------------\w")
result= re.search(r"\w+@\w+\.\w+", email_data)
print(result)

result= re.search(r"(\w+)@(\w+)\.(\w+)", email_data)
print(result)
print(result[0])

result= re.findall(r"(\w+)@(\w+)\.(\w+)", email_data)
print(result)
print(result[0])
