# Demo 1
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"The key {error_msg} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError

# Demo 2
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pei")
    else:
        print(fruit + " pie")


make_pie(4)

# Demo 3
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
    finally:
        print(total_likes)
