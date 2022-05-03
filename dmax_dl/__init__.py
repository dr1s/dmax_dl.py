import argparse
from dmax_dl.dmax_dl import dlmgr

__NAME__ = "dmax_dl"
__VERSION__ = "0.1.dev0"
__AUTHOR__ = "dr1s"


def main():

    parser = argparse.ArgumentParser(description="automatic dmax.de episode download")
    parser.add_argument("-s", "--season", help="Season No.", default=0, type=int)
    parser.add_argument(
        "-e",
        "--episode",
        help="Episode No. (Only works in combination with season filter)",
        default=0,
        type=int,
    )
    parser.add_argument("series_url", type=str, help="DMAX Series videos URL")
    parser.add_argument("output_dir", type=str, help="Output dir")
    args = parser.parse_args()

    mgr = dlmgr(args.series_url, args.output_dir)
    mgr.process(args.season, args.episode)


if __name__ == "__main__":
    main()
