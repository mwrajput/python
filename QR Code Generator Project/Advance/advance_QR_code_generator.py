import os
import qrcode
from datetime import datetime
# import re

# step 0 : Creates a folder 
folder_name = "qrcodes"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
        
try:
    # Step 1: Enter the link to be encoded
    link = input("Enter the link to generate a QR code: ").strip()
    if not link:
        raise ValueError("The link cannot be empty.")

    # Validate the URL format (basic check)
    if not (link.startswith("http://") or  link.startswith("https://")):
        raise ValueError("The link must start with 'http://' or 'https://'.")
    
    # Step 2: Generate customization options
    print("Customize your QR code:")
    
    try:
        box_size = int(input("Enter the box size (default 10): ") or 10)
        if not (1 <=box_size <= 40):
            raise ValueError("Box size must be between 1 and 40.")
    except ValueError as e:
        raise ValueError(f"ٰInvalid box size. {e}") 
    
    try:
        border = int(input("Enter the border size (default 4): ") or 4)
        if not (1 <= border <= 10):
            raise ValueError("Border size must be between 1 and 10.")
    except ValueError as e:
        raise ValueError(f"Invalid border size. {e}") 
    
    
    fill_color = input("Enter the fill color (default black): ").strip() or "black"
    back_color = input("Enter the background color (default white): ").strip() or "white"

    # Step 3: Generate a unique filename using the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"qrcode_{timestamp}.png"


    # Step 4: Generate the QR code with customizations
    qr = qrcode.QRCode(
        version=1,  # Size of the QR Code (1 to 40, higher means larger)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=box_size,
        border=border,
    )

    qr.add_data(link)
    qr.make()
    image = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Step 5: Save the QR code image in the 'qrcodes' folder
    image_path = os.path.join(folder_name, file_name)
    image.save(image_path)

    # Step 6: Confirmation message
    print(f"QR code successfully generated and saved at '{image_path}'.")
    
except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")