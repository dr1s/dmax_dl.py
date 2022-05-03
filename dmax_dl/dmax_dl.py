#!/usr/bin/env python3
import dmax_dl.dmax


class YTDLLogger:
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class dlmgr:
    def __init__(self, series_url, output_dir):
        self.url = series_url
        self.series = dmax_dl.dmax.series(series_url)
        self.output_dir = output_dir

    def download_episodes(self, season_no, episode_no=None):
        episodes = self.series.seasons[season_no].episodes
        for e in range(0, len(episodes)):
            ep = episodes[e]
            print("S%iE%i - %s: %s" % (ep.season, ep.episode, ep.title, ep.url))
            if ep.episode == episode_no or episode_no == None:
                ep.download(self.output_dir)

    def process(self, season=0, episode=0):

        if season == 0 and episode == 0:
            for s in range(1, int(sorted(self.series.seasons.keys())[-1]) + 1):
                if s in self.series.seasons.keys():
                    self.download_episodes(s)
        elif season > 0 and episode > 0:
            if season in self.series.seasons:
                self.download_episodes(season, episode)
            else:
                print("Error: Season %i not found!" % season)
        elif season > 0 and episode == 0:
            if season in self.series.seasons:
                self.download_episodes(season)
            else:
                print("Error: Season %i not found!" % season)
