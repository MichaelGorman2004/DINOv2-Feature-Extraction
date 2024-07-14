import json
import os
from io import BytesIO
from urllib.request import urlopen

import requests
import torch
import torchvision.transforms as transforms
from PIL import Image


def get_urls(config_file="image_urls.json"):
    with open(config_file, "r") as f:
        urls = json.load(f)
    return urls


def download_load_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        print(f"Failed to download image from {url}")
        return None


def resize_image(image, size=(100, 100)):
    transform = transforms.Compose([transforms.Resize(size), transforms.ToTensor()])
    return transform(image)





def main():
    urls = get_urls()
    images = []
    
    for image_name, url in urls.items():
        print(f"Attempting to load {image_name} from {url}")
        image = download_load_image(url)
        
        if image:
            print(f"Successfully loaded image: {image_name}")
            print(f"Original Image Size: {image.size}")
            
            resized_image = resize_image(image)
            images.append(resized_image)
            
            print(f"Resized Image Size: {resized_image.size}")
        else:
            print(f"Failed to load image: {image_name}")
    
    print(f"Total images processed: {len(images)}")

# TODO: Continue along project workflow
