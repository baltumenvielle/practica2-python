def most_influential(stats):
  max_points = 0

  for player in stats:
    points = player[1] * 1.5 + player[2] * 1.25 + player[3]
    if points > max_points:
      max_points = points
      most_influential = player[0]

  return most_influential