import argparse
import typing
import matplotlib.pyplot as plt
import os.path
import json
import sys


def _existing_file(s: str):
    if os.path.isfile(s):
        return s
    raise argparse.ArgumentTypeError(f"file '{s}' does not exist")


frequencies_t = typing.Dict[str, float]


def get_frequencies(fname: str) -> frequencies_t:
    abs_f: frequencies_t = dict()
    with open(fname, "rt") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if c.isalpha():
                lower = c.lower()
                abs_f[lower] = abs_f.get(lower, 0) + 1
    total = sum(abs_f.values())
    relative_f = dict()
    for c, n in abs_f.items():
        relative_f[c] = abs_f[c] / total
    return relative_f


def plot_barchart(f: frequencies_t):
    array_f = list(f.items())
    array_f.sort(key=lambda x: x[1], reverse=True)
    plt.grid(linestyle="--", linewidth=1, axis="y", zorder=1)
    plt.bar(
        list(map(lambda x: x[0], array_f)),
        list(map(lambda x: x[1], array_f)),
        zorder=2,
    )
    plt.savefig("frequencies.png", dpi=300)


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-i",
        "--input",
        help="file name to be processed",
        type=_existing_file,
    )
    parser.add_argument(
        "-j",
        "--dump-json",
        help="print json object with frequencies",
        action="store_true",
    )
    args = parser.parse_args()
    f = get_frequencies(args.input)
    if args.dump_json:
        json.dump(f, sys.stdout)
    plot_barchart(f)


if __name__ == "__main__":
    main()
