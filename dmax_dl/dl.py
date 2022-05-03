#!/usr/bin/env python3
import os
import youtube_dl
import dmax_dl.dmax


class YTDLLogger:
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class mgr:
    def __init__(self, series, output_dir, format):
        self.series = series
        self.output_dir = output_dir
        self.format = format

    def download(self, episode):

        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)

        filename = "S%02dE%02d - %s" % (episode.season, episode.episode, episode.title)
        output_dir = os.path.join(self.output_dir, "Season %02d" % episode.season)

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        output_file = os.path.join(output_dir, filename)

        ytdl_opts = {
            "format": self.format,
            "outtmpl": output_file + ".%(ext)s",
        }

        with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
            ydl.download([episode.url])

    def download_episodes(self, season_no, episode_no=None):
        episodes = self.series.seasons[season_no].episodes
        for e in range(0, len(episodes)):
            ep = episodes[e]
            print("S%iE%i - %s: %s" % (ep.season, ep.episode, ep.title, ep.url))
            if ep.episode == episode_no or episode_no == None:
                self.download(ep)

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
