# Write a class to represent a tweet

class Tweet:
    max_chars = 140
    
    def __init__(self, msg_content, author):
        self.msg_content = self.check_char_limit(msg_content)
        self.author = author
        
    def delete(self):
        self.msg_content = ""
        
    def edit(self, new_tweet):
        self.msg_content = self.check_char_limit(new_tweet)

    def check_char_limit(self, ctx):
        if len(ctx) > self.max_chars:
            raise ValueError("Message too long")
        return ctx

tweet_1 = Tweet("Make Amerca Great Again!", "Donald Trump")
tweet_1.edit("Make America Great Again!")
print(tweet_1.msg_content)
