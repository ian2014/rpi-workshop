from PIL import Image
import pytesseract
img = Image.open("1.jpg")
img = img.convert("L")

#img.show()
#tessdata_dir_config = "/home/pi/car/tessdata/" 
#ans = pytesseract.image_to_string(img, lang="chi_tra", config=tessdata_dir_config)

ans = pytesseract.image_to_string(img, lang="eng")
print(ans)
