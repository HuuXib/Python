# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Hubert",17,"male")

print(student.count("Hubert"))
print(student.index("male"))

for x in student:
    print(x)

if "Hubert" in student:
    print("Hubert is here!")


