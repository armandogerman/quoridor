# token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYXJtYW5kb2dlcm1hbkBob3RtYWlsLmNvbSJ9.uUrFiFUJIRRD4BHXOkK4_XUCUefyuFFAEhKNPt9P6ms"
# token_botar: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYm90YXIifQ.HKYNh23NsF4ips3M73gUoq4dLv5hPmKCdglCW2ZfJHc"

def position(i):
  for j in range(17):
    col = i-(j*34)
    acu=0
    if col<=17:
      while col>=0:
        if col==0:
          return j,acu
        elif col>0:
          col-=2
          acu+=1  

i=0
for i in range(289):
    print("****i",i,"position:",position(i))