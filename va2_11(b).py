import random
def perf_measure(n,m,x,y,environ):
  score=0
  for i in range(1000):
    score=score+get_score(n,m,environ) ## increases the score for each time step
    if environ[x][y]==1:
      environ[x][y]=0
    elif environ[x][y]==2:
      return "The agent just bumped into an obstacle."
    if x>0 and y>0 and x<n-1 and y<m-1:
      direction=random.randrange(1,5)
      if direction==1:
        x=x-1
      elif direction==2:
        y=y+1
      elif direction==3:
        x=x+1
      elif direction==4:
        y=y-1
    elif x==0:
      if y>0 and y<m-1:
        direction=random.randrange(2,5)
        if direction==2:
          y=y+1
        elif direction==3:
          x=x+1
        elif direction==4:
          y=y-1
      elif y==0:
        direction=random.randrange(2,4)
        if direction==2:
          y=y+1
        elif direction==3:
          x=x+1
      elif y==m-1:
        direction=random.randrange(3,5)
        if direction==3:
          x=x+1
        elif direction==4:
          y=y-1
    elif x==n-1:
      if y>0 and y<m-1:
        direction=random.randrange(1,4)
        if direction==1:
          y=y-1
        elif direction==2:
          x=x-1
        elif direction==3:
          y=y+1
      elif y==0:
        direction=random.randrange(2,4)
        if direction==2:
          y=y+1
        elif direction==3:
          x=x-1
      elif y==m-1:
        direction=random.randrange(3,5)
        if direction==3:
          x=x-1
        elif direction==4:
          y=y-1
    elif y==0:
      if x>0 and x<n-1:
        direction=random.randrange(2,5)
        if direction==2:
          x=x+1
        elif direction==3:
          x=x-1
        elif direction==4:
          y=y+1
    elif y==m-1:
      if x>0 and x<n-1:
        direction=random.randrange(2,5)
        if direction==2:
          x=x+1
        elif direction==3:
          x=x-1
        elif direction==4:
          y=y-1

  return score


def get_score(n,m,environ):
  score=0
  for r in range(n):
    for c in range(m):
      if environ[r][c]==0:
        score=score+1     ## increments score for each clean square
  return score


def environment():
  print("Enter the number of rows and columns")
  n=int(input())
  m=int(input())
  environ=[]

  #initializing the environment array to 0
  for i in range(n):
    row=[]
    for j in range(m):
      row.append(0)
    environ.append(row)

  #placing dirt in the environment- the probability of finding dirt for each square is 15%- the square containing dirt is represented by 1
  for i in range(n):
    for j in range(m):
      environ[i][j]=1 if random.random()<=0.15 else 0

  #placing obstacles in the environment- the probability of a square being an obstacle is 5%- the square containing an obstacle is represented by 2
  for i in range(n):
    for j in range(m):
      if environ[i][j]!=1:
        environ[i][j]=2 if random.random()<=0.05 else 0
  return n,m,environ


def print_env(n,m,environ):
  print("Environment--->")
  print()
  for i in range(n):
    for j in range(m):
      print(environ[i][j],end=' ')
    print()


def findAgentLoc(n,m,environ):
  for i in range(n):
    for j in range(m):
      if environ[i][j]==0 or environ[i][j]==1: ## agent's initial location can be a clean tile or a dirty tile
        agent_loc=[i,j]
        return agent_loc

n,m,environ=environment() ##creating the environment
print_env(n,m,environ)    ## printing the environment
agent_loc=findAgentLoc(n,m,environ)   ## making the first square without a bump as the agent location
x=agent_loc[0]
y=agent_loc[1]
point=perf_measure(n,m,x,y,environ) # calculating the score
if type(point)==str:
  print(point)
else:
  ideal_score=(n*m)*1000  ## ideal score is the score we get if the squares are always clean
  percentage=(point/ideal_score)*100
  print("Performance score:",point)
  print("Ideal score:",ideal_score)
  print("Performance Percentage=",round(percentage,2),"%")