import pytube

url=input("enter video URL:")
#path=input("enter path of storage")
path="./"

pytube.YouTube(url).streams.get_highest_resolution().download(path)
