import json

# Intersection and union of two sets.

# tup1=(6,-2,3,4,40)
# max = 0
# min =10
#
# for i in tup1:
#    if max < i:
#        max=i
#
# print("Max Number is", max)

# Find the intersection and union of two sets.

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
#
# setuni = set1.union(set2)
# print(setuni)

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}

# setuni = set1.intersection(set2)
# print(setuni)

# Remove duplicate elements from a list.

# List1 = [ 2, 2, 3, 3, 4, 5]

# Remove_Dup = set(List1)
# set.union(Remove_Dup)
# print(Remove_Dup)

# Remove a key-value pair from the dictionary.
# my_dict = {"Batman": 1234, "Age": 123, "Phone": 979867857}
# temp =(my_dict.pop("Phone"))
# print(temp)

# Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data

Travel_dictionary = {

    "bookingid": 2384,

    "booking": {

        "firstname": "PRAMOD",

        "lastname": "Dutta",

        "totalprice": 432,

        "depositpaid": False,

        "bookingdates": {

            "checkin": "2022-01-01",

            "checkout": "2022-01-01"

        },

        "additionalneeds": "Lunch"

    }

}

Travel_json = json.dumps(Travel_dictionary, indent=3)

val1 = Travel_dictionary["bookingid"]
val2 = Travel_dictionary["booking"].get("bookingdates")
val3 = Travel_dictionary["booking"]["bookingdates"].get("checkin")

print(val1)
print(val2)
print(val3)
