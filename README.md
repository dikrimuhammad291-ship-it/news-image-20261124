[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/dikrimuhammad291-ship-it/news-image-20261124/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/dikrimuhammad291-ship-it/news-image-20261124/reward.svg)](https://make.fun/c/news-image-20261124)

# World news front page, 24 November 2026

Entry for the make.fun bounty [Sum up 24 November's world news in one
image](https://make.fun/bounty/news-image-20261124): a program that writes one
1024×1024 newspaper front page summing up the world news of Tuesday
24 November 2026.

## The front page

![Front page](entry.png)

**Lead story:** Yemen's Houthi fighters struck the PIF Tower, the tallest
skyscraper in Riyadh, for the second time in five days, wounding 11 people
(Saudi Civil Defence via Reuters).

**Also on the page:**

- Russian strike hits a Zaporizhzhia apartment block — 2 killed, dozens wounded
- Israeli strikes kill Hamas security chief Naeem Abu Nahel and six others in Gaza
- Senegal reinstated as 2025 Africa Cup of Nations winners after CAS upheld their appeal
- China probes Shanghai party boss Chen Jining, the fourth Politburo member to fall since 2025
- Germany becomes the first country to access Ukraine's Delta battlefield system
- Abu Dhabi peace talks end in stalemate as Russia rules out territorial concessions

Every story happened, or was first reported, on 24 November 2026. Sources:
Reuters, AP, Kyiv Independent, Al Arabiya, Wall Street Journal.

## How it is built

- `render.py` draws the front page with PIL (masthead, lead story with a flat
  night illustration of the PIF Tower, six story cards, footer) and writes
  `entry.png`. It is deterministic: fixed coordinates and fonts, no randomness,
  so repeated runs produce byte-identical output.
- `main.py` is the graded entrypoint (Python 3.13, standard library only): it
  copies the committed `entry.png` to the output directory.

Run locally:

```sh
python3 render.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
