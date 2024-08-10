import pygame
import PIL
import cv2
import subprocess
import pkg_resources

def check_installation():
    print("✅ Pygame versi:", pygame.__version__)
    print("✅ Pillow versi:", PIL.__version__)
    print("✅ OpenCV versi:", cv2.__version__)

    try:
        # Menggunakan pkg_resources untuk mendapatkan versi moviepy
        moviepy_version = pkg_resources.get_distribution("moviepy").version
        print("✅ MoviePy versi:", moviepy_version)
    except pkg_resources.DistributionNotFound:
        print("❌ MoviePy tidak terpasang.")

    try:
        # Menggunakan pkg_resources untuk mendapatkan versi pydub
        pydub_version = pkg_resources.get_distribution("pydub").version
        print("✅ Pydub versi:", pydub_version)
    except pkg_resources.DistributionNotFound:
        print("❌ Pydub tidak terpasang.")

    try:
        # Memeriksa apakah Tkinter terpasang
        import tkinter
        print("✅ Tkinter sudah terpasang.")
    except ImportError:
        print("❌ Tkinter tidak terpasang.")

check_installation()