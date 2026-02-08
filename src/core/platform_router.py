from connectors.facebook import facebook_post
from connectors.instagram import instagram_post
from connectors.telegram import telegram_post
from connectors.whatsapp_business import whatsapp_post
from connectors.x_twitter import x_post
from connectors.tiktok import tiktok_post
from connectors.pinterest import pinterest_post
from connectors.youtube import youtube_post

PLATFORM_MAP = {
    "facebook": facebook_post,
    "instagram": instagram_post,
    "telegram": telegram_post,
    "whatsapp": whatsapp_post,
    "x": x_post,
    "tiktok": tiktok_post,
    "pinterest": pinterest_post,
    "youtube": youtube_post
}

def get_platform_handler(name):
    name = name.lower().strip()
    return PLATFORM_MAP.get(name)

