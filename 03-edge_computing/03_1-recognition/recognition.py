from PIL import Image
import pytesseract
img = Image.open("1.jpg")
img = img.convert("L")

#img.show()

# config path
#tessdata_dir_config = "sample_data/" 

# lang="FILE_NAME", config="CONFIG_PATH"
#ans = pytesseract.image_to_string(img, lang="abc", config=tessdata_dir_config)

ans = pytesseract.image_to_string(img, lang="eng")
print(ans)
