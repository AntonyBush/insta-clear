from instagrapi import Client

USERNAME='ABC'
PASSWORD='PASS'
MAX_FOLLOWERS_THRES=10000

client = Client()
client.login(USERNAME, PASSWORD)

followers = client.user_followers(client.user_id)
following = client.user_following(client.user_id)
users_to_unfollow = [user for user in following if user not in followers]

snakes = []
for user in users_to_unfollow:
    userInfo = client.user_info_v1(user)
    #if you want to follow celebs who don't follow you
    if userInfo.follower_count < MAX_FOLLOWERS_THRES:
        snakes.append(userInfo.pk)

print("Total users who don't follow you: ", snakes)
for user_to_unfollow in snakes:
    client.user_unfollow(user_to_unfollow)
    print("UNFOLLOWED: ", user_to_unfollow)

print("Cleaned!!")
client.logout()