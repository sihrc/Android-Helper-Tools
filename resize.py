from PIL import Image
import sys
import os

if __name__ == "__main__":
    img = Image.open(os.path.join(os.path.dirname(__file__), sys.argv[1]))
    folders = ["mipmap-mdpi", "mipmap-hdpi", "mipmap-xhdpi", "mipmap-xxhdpi", "mipmap-xxxhdpi"]
    imgs = []
    for i, size in enumerate([192, 144, 96, 72, 48][::-1]):
        resized = img.copy()
        resized.thumbnail((size, size), Image.ANTIALIAS)
        path = os.path.join("res", folders[i])
        if not os.path.exists(path):
            os.makedirs(path)
        resized.save(os.path.join(path, "ic_launcher.png"))
