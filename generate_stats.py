def generate_stats(names, goals, goals_avoided, assists):
  stats = []

  names = names.split(',')
  
  for i in range(len(names)):
    tup = (names[i], goals[i], goals_avoided[i], assists[i])
    stats.append(tup)

  return stats