# # from turtle import *

# # bgcolor("black")
# # speed(0)
# # hideturtle()

# # for i in range(220):
# #     color("red")
# #     circle(i)
# #     color("orange")
# #     circle(i*0.8)
# #     right(3)
# #     forward(3)

# # done()


# import instaloader

# # Create Instaloader object
# ig = instaloader.Instaloader()

# # Take username as input
# username = input("Enter Instagram username: ")

# try:
#     # Fetch profile
#     profile = instaloader.Profile.from_username(ig.context, username)

#     # Print details
#     print("Username:", profile.username)
#     print("Posts:", profile.mediacount)
#     print("Followers:", profile.followers)
#     print("Following:", profile.followees)
#     print("Bio:", profile.biography)

#     # Download only profile picture
#     ig.download_profile(username, profile_pic_only=True)

#     print("Profile picture downloaded successfully!")

# except instaloader.exceptions.ProfileNotExistsException:
#     print("Error: Username does not exist.")

# except instaloader.exceptions.LoginRequiredException:
#     print("Error: Instagram requires login.")

# except Exception as e:
#     print("Error:", e)













import instaloader

ig = instaloader.Instaloader()

# Login
ig.login("your_username", "your_password")

profile = instaloader.Profile.from_username(ig.context, "instagram")
print(profile.followers)