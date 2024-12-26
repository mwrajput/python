import json

data_file = 'youtube.txt'
def load_data():
    try:
        with open(data_file, 'r') as file:  # Open in read mode
            return json.load(file)
    except FileNotFoundError:  # If the file doesn't exist, return an empty list
        return []
    except json.JSONDecodeError:  # If the file is empty or corrupted, return an empty list
        return []

def save_data_helper(videos):
    with open(data_file, 'w') as file:  # Open in write mode
        json.dump(videos, file)

def list_all_videos(video):
    print("\n\nItems in the list are :")
    print("*"*70)
    for index, video in enumerate(video, start=1):
        print(f"{index}) Name :{video['name']}, Duration:{video['time']} ")  
    
    print("*"*70)

def add_video(videos):
    name = input("Enter Video Name : ")
    time = input("Enter Video Time : ")
    videos.append({'name':name ,'time':time})
    save_data_helper(videos)
    
def update_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to update : '))
    if 1 <= index <= len(videos):
       name =input('Enter the new video name : ')
       time = input('Enter the new video time ')
       videos[index-1] = {'name':name, 'time':time}
       save_data_helper(videos)
    else:
        print("Invalid Text selected")
        
def remove_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to be deleted : '))
    if 1<=index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid Index selected")
def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose an Option\n")
        print(" 1. List a Fav youtube Video ")
        print(" 2. Add a Youtube Video ")
        print(" 3. Update a youtube Video ")
        print(" 4. Delete a Youtube Video ")
        print(" 5. Exit the App \n")
        
        # input for user choice
        Choice = input("Enter Your Choice : ")
        # print(videos)
        
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
                # exit()
                break
            case _:
                print("Invalid Choice")
                
if __name__  == "__main__":
    main()