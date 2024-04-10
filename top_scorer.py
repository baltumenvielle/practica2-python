def top_scorer(stats):
  player = max(stats, key=lambda e:e[1])
  highest_scorer = (player[0], player[1])
  
  return highest_scorer