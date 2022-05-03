# dmax_dl
Dowload series from dmax.de

## Setup

    pip3 install git+https://github.com/dr1s/dmax_dl.py

## Usage

    usage: dmax_dl [-h] [-s SEASON] [-e EPISODE] [-f FORMAT] series_url output_dir

    automatic dmax.de episode download

    positional arguments:
      series_url            DMAX series videos URL
      output_dir            output dir

    options:
      -h, --help            show this help message and exit
      -s SEASON, --season SEASON
                            season no.
      -e EPISODE, --episode EPISODE
                            episode no. (only works in combination with season filter)
      -f FORMAT, --format FORMAT
                            youtube-dl audio/video format string
