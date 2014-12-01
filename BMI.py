score1 = int(input("first score:"))
score2 = int(input("second score:"))
score3 = int(input("third score:"))
s=[score1, score2, score3]
s.sort()
print (s[0]*0.2+s[1]*0.3+s[2]*0.5)
