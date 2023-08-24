members = []
posts = {}


class Member():
    def __init__(self, name):
        self.name = name
        members.append(self.name)

    def username(self, username):
        self.username = username

    def password(self, password):
        self.password = password

    def display(self):
        print(f"name: {self.name}, username: {self.username}")


class Post(Member):
    def __init__(self, title):
        self.title = title
        posts['title'] = self.title

    def content(self, content):
        self.content = content
        posts['content'] = self.content

    def author(self, author):
        self.author = author
        posts['author'] = self.author


member1 = Member(name='JaeYoonLee')
member1.username('UNIBRo')
member1.password('sparta')
member1.display()

member1post1 = Post(title='TIL1')
member1post1.content('Very Hard Day')
member1post1.author('UNIBRo')

member1post2 = Post(title='TIL2')
member1post2.content('Wonderful Day!!')
member1post2.author('UNIBRo')

member1post3 = Post(title='WIL1')
member1post3.content('Camping Time')
member1post3.author('UNIBRo')

member2 = Member(name='SeulALee')
member2.username('Sara')
member2.password('love')
member2.display()

member2post1 = Post(title='TIL3')
member2post1.content('Lesson1')
member2post1.author('Sara')

member2post2 = Post(title='WIL1')
member2post2.content('Vacation')
member2post2.author('Sara')

member2post3 = Post(title='TIL4')
member2post3.content('Lesson2')
member2post3.author('Sara')

member3 = Member(name='Dal')
member3.username('Dari')
member3.password('byul')
member3.display()

member3post1 = Post(title='TIL11')
member3post1.content('Lesson14')
member3post1.author('Dari')

member3post2 = Post(title='WIL8')
member3post2.content('Happy mothers day')
member3post2.author('Dari')

member3post3 = Post(title='TIL4')
member3post3.content('Lesson15')
member3post3.author('Dari')

print(members)

print(posts)
