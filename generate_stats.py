def generate_stats(names, goals, goals_avoided, assists):
  names = names.split(',')    

  stats = tuple(zip(names, goals, goals_avoided, assists))

  return stats