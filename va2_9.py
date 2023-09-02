##building a 2x2 environment
def reflex_agent(location,initial_state):
  score=0
  copy_env=[i.copy() for i in initial_state]
  for i in range(1000):
    score=score+get_score(copy_env)
    if copy_env[location[0]][location[1]]==1:
      copy_env[location[0]][location[1]]=0
    if location[1]<2-1:
      location[1]=location[1]+1
    elif location[1]==2-1:
      if location[0]<2-1:
        location[0]=location[0]+1
        location[1]=0
      elif location[0]==2-1:
        location[0]=0
        location[1]=0

  return score

#increments the score for every clean tile
def get_score(environment):
  score=0
  for r in range(2):
    for c in range(2):
      if environment[r][c]==0:
        score=score+1
  return score

#prints the environment
def print_env(environment):
  for r in range(2):
    for c in range(2):
      print(environment[r][c],end=' ')
    print()

##defining initial dirt configurations and agent location, for 2x2 environment there are 16 different possibilities
def define_status(initial_states,i,score_list):
  for t in range(4):
    agent_loc=loc_index[i]
    score=reflex_agent(agent_loc,initial_states[t])

    print("Agent location:",agent_loc)
    print("Environment--->")
    print_env(initial_states[t])

    score_list.append(score)
    print("Performance score:",score)


initial_states=[[[1,0],[0,0]],[[0,1],[0,0]],[[0,0],[1,0]],[[0,0],[0,1]]]
loc_index=[[0,0],[0,1],[1,0],[1,1]]
score_list=[]
total_score=0
define_status(initial_states,0,score_list)
print("--------------------------------\n")
define_status(initial_states,1,score_list)
print("--------------------------------\n")
define_status(initial_states,2,score_list)
print("--------------------------------\n")
define_status(initial_states,3,score_list)
print("--------------------------------\n")
for score in score_list:
  total_score=total_score+score
print("Overall Average Score:",total_score/16)