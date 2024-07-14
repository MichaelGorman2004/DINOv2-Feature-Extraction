import os
from io import BytesIO

import requests
from PIL import Image
import torch
import torchvision.transforms as transforms

def download_load_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        print(f"Failed to download image from {url}")
        return None

def resize_image(image, size=(100,100)):
    transform = transforms.Compose([
        transforms.Resize(size),
        transforms.ToTensor()
    ])
    return transform(image)

flower_url = os.getenv('FLOWER_URL')
bird_url = os.getenv('BIRD_URL')

if not flower_url or not bird_url:
    raise ValueError("Please set the environment variables FLOWER_URL and BIRD_URL")

image_urls = [flower_url, bird_url]

images = []
for url in image_urls:
    image = download_load_image(url)
    if image:
        print(f"Successfully loaded image from {url}")
        print(f"Original Image Size: {image.size}")
        resize_image = resize_image(image)
        images.append(image)
        print(f"Resized Image Size: {image.size}")
    else:
        print(f"Failed to load image from {url}")

# TODO: Continue along project workflow
