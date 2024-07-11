#sida loo sameeyo Video downloader youtube
import yt_dlp

print("\033[32mpleas sxp soo booqo telegram channelkena mahadsanid ")
print("https://t.me/hackingbooking1")
#gali websitka
url = input("\033[31mGali linkiga: ")
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("\033[31mHowsha way kuu dhamaatey mahadsanid")
print("waad ku mahadsanthy sida aad noo dhiiri galisey mahadsanid")
