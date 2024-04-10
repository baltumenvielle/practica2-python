def top_scorer(stats):
  highest_scorer = max(stats, key=lambda stat:stat[1])
  player = (highest_scorer[0], highest_scorer[1])

  return player