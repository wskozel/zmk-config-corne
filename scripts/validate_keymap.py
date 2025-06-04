import json
from pathlib import Path

KEYMAP_PATH = Path(__file__).resolve().parents[1] / "config" / "keymap.json"

def main():
    with open(KEYMAP_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    layer_names = data.get("layer_names")
    layers = data.get("layers")

    if layer_names is None or layers is None:
        raise KeyError("layer_names or layers missing in keymap.json")

    assert len(layer_names) == len(layers), (
        f"Mismatch: {len(layer_names)} layer names vs {len(layers)} layers")

if __name__ == "__main__":
    main()
