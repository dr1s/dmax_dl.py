import mechanize
from bs4 import BeautifulSoup


class episode:
    def __init__(self, episode, season, title, url):
        self.episode = episode
        self.season = season
        self.title = title
        self.url = url


class season:
    def __init__(self, season):
        self.season = season
        self.episodes = []

    def add(self, episode):
        episode_found = False
        for e in self.episodes:
            if episode.title == e.title:
                episode_found = True
        if not episode_found:
            self.episodes.append(episode)


class series:
    def __init__(self, url, episodes=None):
        self.seasons = {}
        self.url = url

    def add(self, episodes=None):
        for e in episodes:
            if not e.season in self.seasons:
                self.seasons[e.season] = season(e.season)
            self.seasons[e.season].add(e)


class scraper:
    def __init__(self):
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        user_agent = [
            (
                "User-agent",
                "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0",
            )
        ]
        self.br.addheaders = user_agent

    def parse(self, url):
        page = self.br.open(url)

        soup = BeautifulSoup(page.read(), "lxml")
        episodes = []
        eps_tmp = soup.find_all(itemprop="itemListElement")
        for ep_tmp in eps_tmp:
            season_no = None
            episode_no = None

            season_tmp = ep_tmp.find_all("div")
            for s in season_tmp:
                if s["class"] == ["card-season"]:
                    season_no = int(s.string.split(":")[0].replace("S", ""))
                    episode_no = int(s.string.split(":")[1].replace("E", ""))

                if episode_no and season_no:
                    ep_dupe = False
                    for e in episodes:
                        if ep_tmp.a.get("href") == e.url:
                            ep_dupe = True
                    if not ep_dupe:
                        episode_tmp = episode(
                            episode_no,
                            season_no,
                            ep_tmp.a.h3.string,
                            ep_tmp.a.get("href"),
                        )
                        episodes.append(episode_tmp)

        return episodes
