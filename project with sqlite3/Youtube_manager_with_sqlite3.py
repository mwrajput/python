import sqlite3
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY ,
            name TEXT NOT NULL,
            time Text NOT NULL
        )               
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)",(name,time))
    conn.commit()

def update_videos(vid_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ? ,time = ? where id = ?",(new_name, new_time,vid_id))
    conn.commit()

def delete_videos(vid_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(vid_id,))
    conn.commit()


def main():
        while True:
            print("\n Youtube Manager | Choose an Option\n")
            print(" 1. List a Fav youtube Video")
            print(" 2. Add a Youtube Video" )
            print(" 3. Update a youtube Video")
            print(" 4. Delete a Youtube Video ")
            print(" 5. Exit the App \n")
            
            # input for user choice
            choice = input("Enter Your Choice : ")
            # print(videos)
            
            if choice == '1':
                list_videos()
            elif choice == '2':
                name = input('Enter your video name : ')
                time = input('Enter your video time : ')
                add_videos(name,time)
            elif choice == '3':
                vid_id = input('Enter your video ID : ')
                name = input('Enter your video  name : ')
                time = input('Enter your video time : ')
                update_videos(vid_id,name,time)
            elif choice == '4':
                vid_id = input('Enter your video ID to delete : ')
                delete_videos(vid_id)
            elif choice == '5':
                break
            else:
                print("Invalid Choice")
    
        conn.close()   
        
        
                 
if __name__ == '__main__':
    main()