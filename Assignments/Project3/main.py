members = []
posts = []


class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def __repr__(self):
        return f'Your name is {self.name} and your username is {self.username}'

    def display(self):
        print(f"name: {self.name}, username: {self.username}")


class Post(Member):
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f'{self.author}\'s post title is {self.title}'


member1 = Member('JaeYoonLee', 'UNIBRo', 'sparta')
members.append(member1)
print(members)

member1post1 = Post('TIL1', 'Very Hard Day', member1.username)
member1post2 = Post('TIL2', 'Wonderful Day!!', member1.username)
member1post3 = Post('WIL1', 'Camping Time', member1.username)
posts.append(member1post1)
posts.append(member1post2)
posts.append(member1post3)

member2 = Member('SeulALee', 'Sara', 'love')
members.append(member2)
print(members)

member2post1 = Post('TIL3', 'Lesson1', member2.username)
member2post2 = Post('WIL1', 'Vacation', member2.username)
member2post3 = Post('TIL4', 'Lesson2', member2.username)
posts.append(member2post1)
posts.append(member2post2)
posts.append(member2post3)

member3 = Member('Dal', 'Dari', 'byul')
members.append(member3)
print(members)

member3post1 = Post('TIL11', 'Lesson14', member3.username)
member3post2 = Post('WIL8', 'Happy mothers day', member3.username)
member3post3 = Post('TIL4', 'Lesson15', member3.username)
posts.append(member3post1)
posts.append(member3post2)
posts.append(member3post3)

for post in posts:
    if post.author == "Dari":
        print(post.title)

certain_word = input('search on contents: ')
for post in posts:
    if certain_word in post.content:
        print(f'title: {post.title}, author: {post.author}')


def create_user():
    my_name = input('Please enter your name: ')
    my_username = input('Please enter your username: ')
    my_password = input('Please enter your password: ')

    members.append(Member(my_name, my_username, my_password))


print(members)


def create_post(my_name):
    my_title = input('Posting Title: ')
    my_content = input('Posting Content: ')

    posts.append(Post(my_title, my_content, my_name))


print(posts)
# 해설강의 1:53 부터 다시!!
