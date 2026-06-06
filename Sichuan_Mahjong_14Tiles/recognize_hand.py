import cv2
import os

TILE_W = 70
TILE_H = 108

def load_templates():
    templates = {}

    for suit in ["B", "C", "D"]:
        folder = os.path.join("templates", suit)

        for file in os.listdir(folder):
            if file.lower().endswith(".png"):
                name = os.path.splitext(file)[0]
                path = os.path.join(folder, file)

                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

                if img is not None:
                    img = cv2.resize(img, (TILE_W, TILE_H))
                    templates[name] = img

    return templates


def split_hand(image):
    image = cv2.resize(image, (image.shape[1], TILE_H))

    tiles = []
    os.makedirs("debug_split_tiles", exist_ok=True)

    # First 13 connected tiles from the left
    for i in range(13):
        x1 = i * TILE_W
        x2 = (i + 1) * TILE_W

        tile = image[:, x1:x2]
        tiles.append(tile)
        cv2.imwrite(f"debug_split_tiles/tile_{len(tiles)}.png", tile)

    # Extra 14th tile from the far right
    x1 = image.shape[1] - TILE_W
    x2 = image.shape[1]

    tile = image[:, x1:x2]
    tiles.append(tile)
    cv2.imwrite(f"debug_split_tiles/tile_{len(tiles)}.png", tile)

    return tiles


def classify_tile(tile_img, templates):
    gray = cv2.cvtColor(tile_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (TILE_W, TILE_H))

    best_tile = None
    best_score = -1

    for name, template in templates.items():
        result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        score = result.max()

        if score > best_score:
            best_score = score
            best_tile = name

    return best_tile, best_score


def recognize_hand(image_path="screenshots/test.png", show_scores=True):
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not load {image_path}")

    templates = load_templates()

    if len(templates) != 27:
        print(f"Warning: loaded {len(templates)} templates, expected 27")

    tiles = split_hand(image)

    detected_hand = []

    for i, tile_img in enumerate(tiles, start=1):
        tile_name, score = classify_tile(tile_img, templates)
        detected_hand.append(tile_name)

        if show_scores:
            print(f"Tile {i}: {tile_name} score={score:.3f}")

    return detected_hand


def main():
    hand = recognize_hand("screenshots/test.png", show_scores=True)

    print()
    print("Detected hand:", hand)


if __name__ == "__main__":
    main()