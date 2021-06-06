import json
import time

from PIL import Image
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

NUM_POKEMON = 151
POKEMON_DIR = "data/pokemon_pics"


def run():
    console = Console()

    with open("data/pokemon_data.json") as f:
        poke_infos = json.loads(f.read())

    for info, pokemon_id in zip(poke_infos, range(1, NUM_POKEMON + 1)):
        path = f"{POKEMON_DIR}/{pokemon_id}.png"
        with Image.open(path) as img:
            height, width = img.height, img.width
            rgba_img = img.convert("RGBA")
            img_text = []
            for y in range(height):
                this_row = []
                for x in range(width):
                    r, g, b, a = rgba_img.getpixel((x, y))
                    this_row.append(("  ", f"on rgb({r},{g},{b})" if a > 0 else ""))
                    should_newline = x % width == 0
                    if should_newline:
                        this_row.append(("\n", ""))

                if not all(t[1] == "" for t in this_row[:-1]):
                    img_text += this_row

            types = ", ".join(info["typeList"])
            console.print(
                Panel(
                    Text.assemble(*img_text),
                    title=f"[b]{info['name']} [dim]|[/] {info['id']} [dim]|[/] {types}",
                    title_align="left",
                    border_style="blue",
                )
            )
            time.sleep(1)


if __name__ == "__main__":
    run()
