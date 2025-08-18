from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from .image_caption import processor, model

def caption_from_url(url: str):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_elements = soup.find_all('img')
        results = []
        for img_element in img_elements:
            img_url = img_element.get('src')
            if not img_url:
                continue
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            elif not img_url.startswith('http'):
                continue
            try:
                resp = requests.get(img_url)
                raw_image = Image.open(BytesIO(resp.content)).convert('RGB')
                if raw_image.size[0] * raw_image.size[1] < 400:
                    continue
                inputs = processor(raw_image, return_tensors="pt")
                out = model.generate(**inputs, max_new_tokens=50)
                caption = processor.decode(out[0], skip_special_tokens=True)
                results.append(f"{img_url}: {caption}")
            except:
                continue
        if not results:
            return "No suitable images found or failed to process images."
        return "\n".join(results)
    except:
        return "Failed to fetch the webpage. Check the URL."
