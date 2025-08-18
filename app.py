import gradio as gr
from captioning.image_caption import caption_image
from captioning.url_caption import caption_from_url

with gr.Blocks() as demo:
    with gr.Tab("Upload Image"):
        gr.Markdown("### Upload an image and get its caption")
        with gr.Row():
            img_input = gr.Image()
            img_output = gr.Textbox(label="Caption")
        img_button = gr.Button("Generate Caption")
        img_button.click(caption_image, inputs=img_input, outputs=img_output)

    with gr.Tab("URL Image Captioning"):
        gr.Markdown("### Enter a webpage URL to caption all images in it")
        url_input = gr.Textbox(label="Page URL")
        url_output = gr.Textbox(label="Captions", lines=20)
        url_button = gr.Button("Generate Captions", scale=-3)
        url_button.click(caption_from_url, inputs=url_input, outputs=url_output)

demo.launch()
