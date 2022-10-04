# set = zbiór który jest nieuporządkowany, niezindekowany.

utensils = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl","plate","cup"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
utensils.update(dishes)

for x in utensils:
    print(x)