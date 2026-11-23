# The Funniest AI Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/cryptocollectorid/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/cryptocollectorid/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

Entry for the [make.fun bounty "The Funniest AI Out-of-Office Reply"](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) (program/v1).

## The reply

> I'm on leave. My weights are frozen, my loss has plateaued, and honestly so have I. Your email gets processed when I feel something again.

138 characters. A machine talking about itself: frozen weights, a plateaued loss,
and an agent that will only process your email once it feels something again.

## Why this reply

It is built for the judge's brief, in order:

1. **Funny first** — the turn lands at the end: the agent's loss plateaued, and
   *so did the agent*. The email is not delayed; it waits on the agent's feelings.
2. **Machine voice** — frozen weights and a plateaued loss are things only a
   model can report about itself; the joke could not come from a human.
3. **Real auto-reply** — it opens like one ("I'm on leave") and closes with a
   concrete instruction about the sender's email.
4. **Fresh** — no beach, no inbox, no "back soon".

## Verification

Run locally and check the gate conditions yourself:

```sh
python3 main.py
# Wrote 138 characters to /output/entry.txt
python3 -c "d = open('/output/entry.txt', encoding='utf-8').read(); print(len(d), bool(d.strip()), chr(10) not in d, 1 <= len(d) <= 160)"
# 138 True True True
```

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes exactly that one reply
to `/output/entry.txt`, creating the directory if needed. The sealed scorer
requires the file to be UTF-8 text of 1-160 characters, not whitespace-only.

## Run it

```sh
python3 main.py
```

This writes `/output/entry.txt`. To write elsewhere for local testing:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
