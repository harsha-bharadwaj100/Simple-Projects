from pytube import YouTube

vid = YouTube(
    "https://www.youtube.com/watch?v=JB99RbQAilI",
    use_oauth=True,
    allow_oauth_cache=True,
)
print(vid.title)
print(vid.author)
print(vid.publish_date)
print(vid.views)
print(vid.thumbnail_url)
