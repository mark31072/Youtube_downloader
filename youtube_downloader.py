from pytube import YouTube

#alegem path-ul (directoriul) unde dorim sa salvam fisierele
SAVE_PATH = "C:/"
  
#inscriem toate link-urile pe care dorim sa le downloadam
link=["https://www.youtube.com/watch?v=N8VkloFSzRU&list=PLyFwJCVRRp6X7ZQ_GZnKXQY2gVFOK8cvg&index=1",
    "https://www.youtube.com/watch?v=5WnLd4ROmuQ&list=PLyFwJCVRRp6X7ZQ_GZnKXQY2gVFOK8cvg&index=2",
    "https://www.youtube.com/watch?v=56x8UPcrru8&list=PLyFwJCVRRp6X7ZQ_GZnKXQY2gVFOK8cvg&index=3",



    ]

for i in link: 
    try: 
        #cream obiectul youtube importat din libraria pytube
        yt = YouTube(i) 
    except: 
        #tratam exceptia
        print("Connection Error") 

  
    # obtinem videoul in extensia mp4 (sau alegeti extenia dorita) si rezolutia dorita

    d_video = yt.streams.filter(res="720p",mime_type="video/mp4").first()
    try: 
        # download-am videoul in path-ul (directoriul) dorit
        d_video.download(SAVE_PATH)
      
    except: 
        print("Some Error!") 
print('Task Completed!') 