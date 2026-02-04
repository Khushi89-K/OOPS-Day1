class Instagram:
    def __init__(self,title, description,user_name,location):  
        self.title = title
        self.description = description
        self.user_name = user_name
        self.location = location
        self.comments = [] 
        self.likes = 0
    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The likes of the reel is ",self.likes)
    def display_name(self):
        print("username:", self.user_name)
    def display_location(self):
        print("location:",self.location)
    def comment(self,c_t):
        self.comments.append(c_t)
    def display_comment(self):
        print("comment section")
        for i in self.comments:
            print(i)
    def delete_comment(self):
        d_c = self.comments.pop()
        print("the comment deleted", d_c)
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes-=1


# reel1=Instagram("dancing","dancing with friends","dkd" , "banglore")
# reel1.disliked() 
# reel1.liked() 
# reel2=Instagram("finance minister conference","finance minister conference with friends", "times_of_india", "india")
# reel1.liked() 
# reel2.liked() 
# reel1.disliked() 
# reel1.display_likes()
# reel2.display_likes()
reel3 = Instagram("ssp","scolorship for student","search_creator", "karanataka")
reel3.display_name()
reel3.display_title()
reel3.display_description()
reel3.liked()
reel3.display_likes()
reel3.comment("thank for information")
reel3.comment("when will they provide scolorship")
reel3.display_comment()
reel3.delete_comment()


# print(id(reel1))
# print(id(reel2))