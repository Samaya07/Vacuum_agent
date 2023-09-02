def vacuum_agent(location,environment,score):
  print_env(environment)
  print("Actions taken to clean--->")
  for i in range(1000): ## for 1000 time steps
    score=score+get_score(environment)
    if environment[location]==1:
      action='Suck dirt'
      print(action,end=', ')
      environment[location]=0
    else:
      score=score-1 ## penalizing one point for each movement
      if location==0:
        action="Turn right"
        location=1
      elif location==1:
        action="Turn left"
        location=0
      print(action,end=', ')
  return score

def print_env(environment):
  print("ENVIRONMENT-->")
  for ele in environment:
    print("|",ele,end=' ')
  print("|")

#calculates the score-number of clean tiles at each time step
def get_score(environment):
  score=0
  for ele in environment:
    if ele==0:
      score=score+1
  return score

environment=[1,1] ## Room A is at index 0, Room B is at index 1
agent_loc=0 ## Agents initial location is Room A
score=vacuum_agent(agent_loc,environment,0)
ideal_score=len(environment)*1000
print("\n\n")
print("Performance score:",score)
print("Considering both the rooms always clean as the ideal state--->\nIdeal performance score:",ideal_score)
print("Performance percentage:",round((score/ideal_score)*100,2),"%")