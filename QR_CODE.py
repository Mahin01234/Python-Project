import qrcode
from PIL import Image
import os


qr = qrcode.QRCode(
    version=5,                      
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # allows logo overlay
    box_size=10,
    border=4,
)
qr.add_data("http://www.google.com")
qr.make(fit=True)


qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")


logo_path = "logo.png"
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    # Resize logo (max 100x100, but adaptive to QR size)
    logo_size = min(100, qr_img.size[0] // 4)   # logo covers at most 1/4 of QR
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
    
    
    pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)
    
    
    if logo.mode == 'RGBA':
        qr_img.paste(logo, pos, mask=logo)
    else:
        qr_img.paste(logo, pos)
else:
    print(f"Warning: {logo_path} not found. Generating QR code without logo.")


qr_img.save("qr_with_logo.png")
qr_img.show()
print("QR code saved as 'qr_with_logo.png'")