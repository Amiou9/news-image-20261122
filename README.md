[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Amiou9/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Amiou9/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# The world on Sunday, 22 November 2026

One broadsheet front page for a single day's world news: Sunday,
22 November 2026. The front page leads with the COP31 talks stuck
in overtime in Antalya, Iran's strike on an industrial site in
Bahrain and the tankers hit near the Strait of Hormuz, and the
candy-factory fire in Cikande, Indonesia that killed 3 and left
36 missing. Around them: the FBI crime-database breach, Amazon's
near-$7.5B deal for Decart, India declaring 720/9 against New
Zealand, GTA 6's $3.79B launch day, and 25 more stories from
every region -- 35 in all, each with its own drawn illustration,
plus a realistic world map numbering where each story happened
and a date check naming the previous day's news that was left out.

How it runs: `main.py` is Python 3.13, standard library only, no
network, deterministic. It checks `entry.png` is a PNG inside the
size limits and copies it unchanged to `/output/entry.png`.
