from operator import attrgetter
from operator import itemgetter
currentUser = {
    "id": 24,
    "name": "John Doe",
    "website": "http://mywebsite.com",
    "description": "I am an actor",
    "gender": "M",
    "phone_number": "+12345678",
    "username": "johndoe",
    "birth_date": "1991-02-23",
    "followers": 46263,
    "following": 345,
    "like": 204,
    "comments": 9,
    "email": "example@example.com",
}
joeId, email, gender, username = itemgetter(
    'id', 'email', 'gender', 'username')(currentUser)
print("id:", joeId, email, gender, username)

# id, email, gender, username = attrgetter(
#     'id', 'email', 'gender', 'username')(currentUser)
# print(id, email, gender, username)


def multiple_yield():
    str1 = "First String"
    yield str1

    str2 = "Second string"
    yield str2

    str3 = "Third String"
    yield str3


obj = multiple_yield()
print(next(obj))
# print(next(obj))
# print(next(obj))


def simple():
    for i in range(10):
        if (i % 2 == 0):
            yield i


# Successive Function call using for loop
for i in simple():
    print(i)

print(next(obj))


