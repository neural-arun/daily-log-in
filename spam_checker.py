# a spam comment is defined as a text containing following keywords
spam1 = "make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"
comment = input("Enter your comment :")
if (spam1 in comment) or (spam2 in comment) or (spam3 in comment):
    print("This comment is a spam")
else:
    print("This is a fair comment")