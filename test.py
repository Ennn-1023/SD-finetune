from diffusers import StableDiffusionPipeline
pipeline = StableDiffusionPipeline.from_pretrained("./stable-diffusion-2-inpainting", use_safetensors=True)
print('inchannel = ', pipeline.unet.config["in_channels"])