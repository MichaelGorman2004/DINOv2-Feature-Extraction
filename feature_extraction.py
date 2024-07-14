import json
from io import BytesIO

import requests
import torch
from PIL import Image
from transformers import AutoImageProcessor, AutoModel


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
    return image.resize(size)


def process_features(features):
    processed_features = []
    for feature in features:
        # Get the average over spatial dimensions (excluding the batch dimension)
        avg_feature = torch.mean(feature.squeeze(0), dim=0)

        # Normalize the features
        normalized_feature = torch.nn.functional.normalize(avg_feature, p=2, dim=-1)

        processed_features.append(normalized_feature)

    return processed_features


def main():
    urls = get_urls()
    images = []
    features = []
    processor = AutoImageProcessor.from_pretrained("facebook/dinov2-base")
    model = AutoModel.from_pretrained("facebook/dinov2-base")

    for image_name, url in urls.items():
        print(f"Attempting to load {image_name} from {url}")
        image = download_load_image(url)

        if image:
            print(f"Successfully loaded image: {image_name}")
            print(f"Original Image Size: {image.size}")

            resized_image = resize_image(image)
            images.append(resized_image)

            print(f"Resized Image Size: {resized_image.size}")

            # Process the image for the model
            inputs = processor(images=resized_image, return_tensors="pt")

            # Extract features
            with torch.no_grad():
                outputs = model(**inputs)

            # Get last hidden state
            last_hidden_state = outputs.last_hidden_state
            features.append(last_hidden_state)

            print(f"Extracted features shape: {last_hidden_state.shape}")
        else:
            print(f"Failed to load image: {image_name}")

    print(f"Total images processed: {len(images)}")

    processed_features = process_features(features)

    for i, feature in enumerate(processed_features):
        print(f"Feature {i+1} shape: {feature.shape}")
        sum_of_elements = torch.sum(feature).item()
        print(f"Sum of elements: {sum_of_elements}")
        print(f"L2 norm: {torch.norm(feature, p=2).item()}")

    return processed_features


if __name__ == "__main__":
    main()
