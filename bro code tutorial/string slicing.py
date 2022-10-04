# slicing = create a substring by extracting elements from another string
#       indexing[] or slice{}
#       [start:stop:step]

# name = "Hubert Fronczek"
# [String początkowy : string koncowy : co ile liter ma pokazywac nasz string]
# first_name = name[0:6]
# last_name = name[7:]
# funky_name = name[0::2]
# reversed_name = name[::-1]
#
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print (website[slice])
print (website2[slice])