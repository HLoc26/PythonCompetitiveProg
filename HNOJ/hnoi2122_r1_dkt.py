'''https://hnoj.edu.vn/problem/hnoi2122_r1_dkt'''
import sys
sys.stdin = open("DKT.INP",'r')
sys.stdout = open("DKT.OUT",'w')

n = int(input())
total = n*(n+1)//2
print(chr(total%26 + ord('A')))