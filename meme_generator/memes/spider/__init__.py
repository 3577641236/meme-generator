from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def spider(
    images: list[BuildImage], texts, args
):
    user_size = (75, 75)
    user_locs = [
        (178, 27),
        (178, 27),
        (168, 27),
        (158, 27),
        (148, 27),
        (138, 27),
        (133, 27),
        (118, 27),
        (110, 27),
        (105, 27),
        (95, 27),
        (90, 27),
        (78, 27),
        (78, 27),
        (78, 27),
        (78, 27),
        (90, 27),
        (95, 27),
        (105, 27),
        (110, 27),
        (119, 27),
        (131, 27),
        (136, 27),
        (146, 27),
        (156, 27),
        (168, 27),
        (176, 27),
        (176, 27),
    ]

    frames = []
    user = images[0].resize(user_size).circle()

    for i in range(len(user_locs)):
        frame = BuildImage.open(img_dir / f"{i}.png")
        frame.paste(user, user_locs[i], alpha=True)
        frames.append(frame.image)

    return save_gif(frames, 0.05)


add_meme(
    "spider",
    spider,
    min_images=1,
    max_images=1,
    keywords=["蜘蛛"],
    date_created=datetime(2025, 4, 26),
    date_modified=datetime(2025, 4, 26),
)
