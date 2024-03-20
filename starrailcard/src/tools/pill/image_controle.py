# Copyright 2024 DEViantUa <t.me/deviant_ua>
# All rights reserved.

from PIL import Image
from io import BytesIO

import re
import json


from .. import cashe, http

_caches = cashe.Cache.get_cache()

async def resize_image(image, scale):
    width, height = image.size
    new_width = int(width * scale)
    new_height = int(height * scale)
    resized_image = image.resize((new_width, new_height))
    return resized_image


async def get_centr_size(size, file_name): #get_centr_honkai_art
    background_image = Image.new('RGBA', size, color=(0, 0, 0, 0))
    foreground_image = file_name.convert("RGBA")

    scale = max(size[0] / foreground_image.size[0], size[1] / foreground_image.size[1])
    foreground_image = foreground_image.resize((int(foreground_image.size[0] * scale), int(foreground_image.size[1] * scale)))

    background_size = background_image.size
    foreground_size = foreground_image.size

    x = background_size[0] // 2 - foreground_size[0] // 2

    if foreground_size[1] > background_size[1]:
        y_offset = max(int(0.3 * (foreground_size[1] - background_size[1])), int(0.5 * (-foreground_size[1])))
        y = -y_offset
    else:
        y = background_size[1] // 2 - foreground_size[1] // 2

    background_image.alpha_composite(foreground_image, (x, y))

    return background_image


async def get_centr_scale(size, file_name):
    
    background_image = Image.new('RGBA', size, color=(0, 0, 0, 0))
    foreground_image = file_name.convert("RGBA")
    
    scale = 0.65
    foreground_image = await resize_image(foreground_image, scale)

    background_size = background_image.size
    foreground_size = foreground_image.size

    x = background_size[0] // 2 - foreground_size[0] // 2
    y = background_size[1] // 2 - foreground_size[1] // 2

    background_image.alpha_composite(foreground_image, (x, y))

    return background_image


async def get_dowload_img(link,size = None, thumbnail_size = None, gif = False):
    cache_key = json.dumps((link, size, thumbnail_size), sort_keys=True)
        
    if not gif:
        if cache_key in _caches:
            return _caches[cache_key]
    
    headers_p = None
    
    if "pximg" in link:
        headers_p = {
            "referer": "https://www.pixiv.net/",
        }
    try:
        image = await http.AioSession.get(link,headers=headers_p, response_format= "bytes")
    except:
        raise
    
    if gif:
        return image
        
    image = Image.open(BytesIO(image)).convert("RGBA")
    if size:
        image = image.resize(size)
        _caches[cache_key] = image
        return image
    elif thumbnail_size:
        image.thumbnail(thumbnail_size)
        _caches[cache_key] = image
        return image
    else:
        _caches[cache_key] = image
        return image

async def crop_image(img):
    width, height = img.size
    target_pixel_x = 275
    target_pixel_y = height // 2
    crop_size = 8
    left = max(0, target_pixel_x - crop_size // 2)
    right = min(width, target_pixel_x + crop_size // 2 + 1)
    cropped_img = img.crop((left, 0, right, height))
    
    return cropped_img

async def get_user_image(img):
    if type(img) != str:
        img = img
    elif type(img) == str:
        linkImg = re.search("(?P<url>https?://[^\s]+)", img)
        if linkImg:
            try:
                if "gif" in linkImg.group():
                    img = await get_dowload_img(linkImg.group(), gif = True)
                    return img
                else:
                    img = await get_dowload_img(linkImg.group())
            except:
                return None
        else:
            img = Image.open(img)
    else:
        return None
    return img.convert("RGBA")
