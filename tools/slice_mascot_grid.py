from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def build_positions(full: int, cell: int, count: int) -> list[int]:
    if count <= 1:
        return [0]
    span = full - cell
    return [round(index * span / (count - 1)) for index in range(count)]


def alpha_area(image: Image.Image) -> int:
    alpha = image.getchannel("A")
    return sum(1 for value in alpha.getdata() if value)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Slice a transparent mascot sheet by a fixed grid without including inter-cell gaps."
    )
    parser.add_argument("--input", required=True, help="Source PNG path.")
    parser.add_argument("--output-dir", required=True, help="Directory to write mascot PNG files.")
    parser.add_argument("--rows", type=int, required=True, help="Grid row count.")
    parser.add_argument("--cols", type=int, required=True, help="Grid column count.")
    parser.add_argument("--cell-width", type=int, required=True, help="Single mascot crop width.")
    parser.add_argument("--cell-height", type=int, required=True, help="Single mascot crop height.")
    parser.add_argument("--start-index", type=int, default=1, help="First mascot index to write.")
    parser.add_argument(
        "--min-alpha-area",
        type=int,
        default=600,
        help="Skip cells whose visible pixel count is below this threshold.",
    )
    args = parser.parse_args()

    src_path = Path(args.input)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    image = Image.open(src_path).convert("RGBA")
    width, height = image.size

    xs = build_positions(width, args.cell_width, args.cols)
    ys = build_positions(height, args.cell_height, args.rows)

    index = args.start_index
    saved: list[tuple[int, int, int, int]] = []
    skipped: list[tuple[int, int, int]] = []

    for row, top in enumerate(ys):
        for col, left in enumerate(xs):
            crop = image.crop((left, top, left + args.cell_width, top + args.cell_height))
            visible_area = alpha_area(crop)
            if visible_area < args.min_alpha_area:
                skipped.append((row, col, visible_area))
                continue

            out_path = out_dir / f"mascot-{index:02d}.png"
            crop.save(out_path)
            saved.append((index, row, col, visible_area))
            index += 1

    print(f"source={src_path}")
    print(f"grid={args.rows}x{args.cols} cell={args.cell_width}x{args.cell_height}")
    print(f"saved={len(saved)} next_index={index}")
    print("x_positions=" + ",".join(str(value) for value in xs))
    print("y_positions=" + ",".join(str(value) for value in ys))
    for item in saved:
        print(f"saved mascot-{item[0]:02d} row={item[1]} col={item[2]} alpha_area={item[3]}")
    for item in skipped:
        print(f"skipped row={item[0]} col={item[1]} alpha_area={item[2]}")


if __name__ == "__main__":
    main()
