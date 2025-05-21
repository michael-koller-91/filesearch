import argparse
from pathlib import Path
import re
import sys


def main():
    parser = argparse.ArgumentParser(
        prog="filesearch",
        description="Find files and file contents in the current directory matching (Python) regex patterns.",
        epilog="examples:"
        """\n  * Find all files ending with ".py":"""
        """\n      filesearch ".*.py\\b" """
        """\n  * Find all files ending with ".py" but excluding files in the folder ".git":"""
        """\n      filesearch ".*.py\\b" ".git" """
        """\n  * In all files ending with ".py" but excluding files in the folder ".git", """
        """find lines containing "def":"""
        """\n      filesearch ".*.py\\b" ".git" "def" """
        """\n  * In the previous example, also print the 3 lines before and after the matching line:"""
        """\n      filesearch ".*.py\\b" ".git" "def" 3""",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "filename_pattern", type=str, help="Find filenames matching this regex pattern."
    )
    parser.add_argument(
        "path_exclude_pattern",
        type=str,
        help="Exclude filenames whose paths match this regex pattern.",
        default="$^",
        nargs="?",
    )
    parser.add_argument(
        "content_pattern",
        type=str,
        help="Find file contents matching this regex pattern.",
        default="",
        nargs="?",
    )
    parser.add_argument(
        "n",
        type=int,
        help="How many surrounding lines to display for a content match.",
        default=0,
        nargs="?",
    )
    parser.add_argument(
        "--no-r",
        action="store_true",
        help="If this flag is present, the search is not recursive.",
    )
    args = parser.parse_args(args=None if sys.argv[1:] else ["--help"])

    fpat = re.compile(args.filename_pattern)
    epat = re.compile(args.path_exclude_pattern)
    cpat = re.compile(args.content_pattern)

    fcounter = 0

    if args.no_r:
        iterator = Path(".").iterdir()
    else:
        iterator = Path(".").rglob("*")

    for f in iterator:
        if f.is_file() and fpat.match(f.name) and not epat.match(str(f)):
            fcounter += 1
            if args.content_pattern:
                first = True
                with open(f, "r", errors="ignore") as file:
                    lines = file.readlines()
                    pcounter = 0
                    for num, line in enumerate(lines):
                        if re.search(cpat, line):
                            if first:
                                first = False
                                print("\n", f)
                            else:
                                print()
                            pcounter += 1
                            for line_num in range(num - args.n, num + args.n + 1):
                                if 0 <= line_num and line_num < len(lines):
                                    print(f"\t{line_num+1}:", lines[line_num], end="")
                    if pcounter > 10:
                        print(f"({pcounter} content hits.)")
            else:
                print(f)

    print(f"({fcounter} file hits.)")


if __name__ == "__main__":
    main()
