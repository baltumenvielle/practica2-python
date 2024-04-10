def generate_stats(names, goals, goals_avoided, assists):
  names = names.split(',')    

  stats = []

  for i in range(len(names)):
    player = (names[i], goals[i], goals_avoided[i], assists[i])
    stats.append(player)

  return stats