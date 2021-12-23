# На основе решения А. Кабанова

Fin = open("27-1b.txt")

N = int( Fin.readline() )

B = 3

INF = 10**10
sums = [0 for i in range(B)]
for i in range(N):
  ab = list(map( int, Fin.readline().split() ))
  sumsNext = [INF]*B
  for s in sums:
    for x in ab:
      r = s + x
      if r < sumsNext[r%B]:
        sumsNext[r%B] = r
  sums = sumsNext[:]

Fin.close()

print( min(sums[1:]) )
