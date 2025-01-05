"""
This is the project where we can create a QR_Code_Generator_Project
this is so simple python has given already a library named "qrcode"


pip install qrcode , pip install pillow

import libraries
os
qrcode 
datetime 


step 0 : create a folder check if not  

step 1 : initialize a variable that hold link 

step 2 : Generate a unique filename using the current timestamp
            stream str 
            format f
            time time
            year , month , day , hour , minute , second
            strftime("%Y-%m %d %H:%M:%S")

Step 3: Generate the QR code , Save that image in the folder

step 4: Step 4: Confirmation message


"""
import os
import qrcode 
from datetime import datetime

# Step 0: Create a folder named 'qrcodes' if it doesn't exist
folder_name = "qrcodes"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Step 1: Enter the link to be encoded
link = input("Enter the link to generate a QR code: ")

# Step 2: Generate a unique filename using the current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
filename = f"qrcode_{timestamp}.png"


# Step 3: Save the QR code image in qrcodes folder that we created 
image = qrcode.make(link)    # grenerating qrcode
image_path = os.path.join(folder_name,filename)
image.save(image_path)


# Step 4: Confirmation message
print("QR code successfully generated and saved as 'qrcode.png'.")