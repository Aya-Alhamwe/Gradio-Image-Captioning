from PIL import Image
import numpy as np
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load pretrained processor and model (shared for all functions)
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_image(input_image: np.ndarray):
    raw_image = Image.fromarray(input_image).convert('RGB')
    inputs = processor(raw_image, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=50)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption
