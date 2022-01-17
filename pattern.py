#!/usr/bin/env python3
import sys, string

def de_bruijn(k, n):
  try:
    _ = int(k)
    alphabet = list(map(str, range(k)))

  except (ValueError, TypeError):
    alphabet = k
    k = len(k)

  a = [0] * k * n
  sequence = []

  def db(t, p):
    if t > n:
      if n % p == 0:
        sequence.extend(a[1:p + 1])
    else:
      a[t] = a[t - p]
      db(t + 1, p)
      for j in range(a[t - p] + 1, k):
        a[t] = j
        db(t + 1, t)
  db(1, 1)
  return "".join(alphabet[i] for i in sequence)

def bruijn():
  return de_bruijn("0123456789", 4)

def main():
  if len(sys.argv) == 1:
    print(bruijn())
  elif len(sys.argv) == 2:
    print(bruijn().find(sys.argv[1]))
  else:
    print("Error")

if __name__ == "__main__":
  main()
