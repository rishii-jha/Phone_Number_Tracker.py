import qrcode
link = "https://www.youtube.com/@TriggeredgamerYoutuber"
img=qrcode.make(link)
img.save("qrcode.png")