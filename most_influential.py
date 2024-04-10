def calculate_points(player):
  return (player[0], player[1] * 1.5 + player[2] * 1.25 + player[3])

def most_influential(stats):
  points = tuple(map(calculate_points, stats))
  most_influential = max(points, key=lambda stat:stat[1])

  return most_influential[0]