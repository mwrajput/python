
def list_all_videos(video):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def remove_video(videos):
    pass


videos = []

while True:
    print("\n Youtube Manager | Choose an Option ")
    
    print("\n 1. List a Fav youtube Video ")
    print("\n 2. Add a Youtube Video ")
    print("\n 3. Update a youtube Video ")
    print("\n 4. Delete a Youtube Video ")
    
    print("\n 5.Exit the App ")
    
    # input for user choice
    Choice = input("Enter Your Choice : ")
    
    match Choice:
        case '1':
            list_all_videos(videos)
        case '2':
            add_video(videos)
        case '3':
            update_video(videos)
        case '4':
            remove_video(videos)
        case '5':
            exit()