import pafy

url = str(raw_input('Paste the link of Youtube video: '))
video = pafy.new(url)
print 'Title: ' + video.title
print 'Rating: ' + str(video.rating)
print 'Author: '+ video.author
print 'Video Duration: '+ video.duration
print 'Length: '+ str(video.length)

print 'List available strams:'
streams=video.streams
for s in streams:
    print s

best=video.getbest(preftype="mp4")
print 'Best resolution and extension: '+best.resolution, best.extension
#print 'Best URL: '+best.url

res=raw_input('You want to download the video? (Y/N):')
if res=='Y' or res=='y':
    try:
        print 'Downloading...'
        #best.download(quiet=False)
        best.download(filepath="/Users/Aristos/Desktop")
        print
        print 'Done!'
    except Exception as e:
        print 'ERROR:Download Video Failed'
elif res=='N' or res=='n':
    print 'Done!'
else:
    print 'ERROR: Error of comand'
