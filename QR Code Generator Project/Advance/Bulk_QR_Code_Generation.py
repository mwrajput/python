import os
import qrcode
from datetime import datetime
from PIL import Image
import zipfile

# step 0 : Creates a folder 
folder_name = "qrcodes"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Step 1: Accept multiple URLs (either from input or file)
urls_input = input("Enter multiple URLs separated by commas: ")
urls = [url.strip() for url in urls_input.split(',') if url.strip()]  # Strip empty URLs and extra spaces

# Alternatively, you could uncomment this block to accept URLs from a file:
# file_name = 'abc.txt'
# with open(file_name, 'r') as file:
#     urls = [line.strip() for line in file.readlines() if line.strip()]



# Ask user if they want to save QR codes in a folder or as a ZIP file
save_option = input("Do you want to save the QR codes in a folder or download them as a ZIP file? (folder/zip): ").lower()

# Step 2: Loop through each URL and generate QR codes
generated_files = []  # To store the paths of generated files for zipping later

# Step 2: Loop through each URL and generate QR codes
for index, url in enumerate(urls):
    # Generate a unique filename for each QR code
    try:
        # Check if URL is valid (basic check)
        if not url.startswith("http://") and not url.startswith("https://"):
            raise ValueError(f"Invalid URL: {url}")
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S") + f"_{index+1}"
        filename = f"qrcode_{timestamp}.png"
        
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,  # Size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction
            box_size=10,  # Box size
            border=2,  # Border size
        )
        
        qr.add_data(url)
        qr.make(fit=True)
        
        # Customize the colors and generate the image
        image = qr.make_image(fill_color="black", back_color="white")

        # Preview the QR code
        image.show()  # Show the image

         # Ask user if they want to save the QR code
        save_qr_code = input(f"Do you want to save the QR code for {url}? (yes/no): ").lower()

        if save_qr_code == "yes":
            image_path = os.path.join(folder_name, filename)
            image.save(image_path)
            generated_files.append(image_path)  # Add file to list for zipping
            print(f"QR code for {url} saved as '{filename}'")
        else:
            print(f"QR code for {url} not saved.")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Step 3: Handle saving the QR codes either in a folder or as a ZIP file
if save_option == "zip" and generated_files:
    zip_filename = f"qrcodes_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in generated_files:
            zipf.write(file, os.path.basename(file))  # Write each QR code to the ZIP file
    print(f"All QR codes have been saved in the ZIP file: {zip_filename}")
elif save_option == "folder":
    print(f"QR codes saved in the 'qrcodes' folder.")
else:
    print("Invalid option for saving QR codes.")


    
# Step 4: Confirmation message for all generated QR codes
print(f"Bulk QR code generation complete! {len(urls)} QR codes were successfully generated and saved in the 'qrcodes' folder.")
