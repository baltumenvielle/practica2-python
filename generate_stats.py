def generate_stats(names, goals, goals_avoided, assists):
  for name in names:
    if name[0] == " " or name[0] == "\n":
      names = names.replace(name[0], '')
  names = names.capitalize().split(',')    
  

  stats = tuple(zip(names, goals, goals_avoided, assists))

  return stats