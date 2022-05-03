#!/usr/bin/env python3

import sys
import dmax_dl.dmax
import argparse

class YTDLLogger:
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def download_episode(folder, series, season_no, episode_no=None):
    episodes = series.seasons[season_no].episodes
    for e in range(0, len(episodes)):
        ep = episodes[e]
        print("S%iE%i - %s: %s" % (ep.season, ep.episode, ep.title, ep.url))
        if ep.episode == episode_no or episode_no == None:
            ep.download(folder)

def main():

    parser = argparse.ArgumentParser(description="automatic dmax.de episode download")
    parser.add_argument("-s", "--season", help="Season No.", default=0, type=int)
    parser.add_argument("-e", "--episode", help="Episode No.", default=0, type=int)
    parser.add_argument("series_url", type=str, help="DMAX Series videos URL")
    parser.add_argument("output_dir", type=str, help="Output dir")
    args = parser.parse_args()

    series = dmax_dl.dmax.series(args.series_url)

    if args.season == 0 and args.episode == 0:
        for s in range(1, len(series.seasons)):
            download_episode(args.output_dir, series, s)
    elif args.season > 0 and args.episode > 0:
        if args.season in series.seasons:
            download_episode(args.output_dir, series, args.season, args.episode)
    elif args.season > 0 and args.episode == 0:
        download_episode(args.output_dir, series, args.season)



if __name__ == "__main__":
    main()
