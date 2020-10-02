#pip install pytube3 ( becauase of this error :  cannot import name 'quote' from 'pytube.compat')

from pytube import YouTube

youtube_url = input("Please enter a YouTube link:")

YouTube(youtube_url).streams.first().download()
