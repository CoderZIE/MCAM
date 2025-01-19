
def AND(A,B):
    A=int(A)
    B=int(B)
    return A&B
def nand(a, b):
    return 0 if (a == 1 and b == 1) else 1
def xnor(a,b):
    return 1 if a==b else 0
def nor(a, b):
    return 1 if (a == 0 and b == 0) else 0
def half_adder(A, B):
    A=int(A)
    B=int(B)
    sum_bit = A ^ B  # XOR operation
    carry = A & B    # AND operation
    return [sum_bit, carry]

def full_adder(A,B,C):
    A=int(A)
    B=int(B)
    sum = A^B^C
    carry = (A&B) | (B&C) | (A&C)
    return [sum,carry]
#############################ACFGI############################
def ACFGII_1(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = A
    carry = B
    return [sum,carry]
def ACFGII_5(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = B
    carry = C
    return [sum,carry]
def ACFGII_10(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = D
    carry = A
    return [sum,carry]
def ACFGII_11(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = D
    carry = B
    return [sum,carry]
######################################AC6G#####################

def AC6G_12(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|C)|(B|D))
    carry = ((C&(B|D))|(A&D))
    return [sum,carry]
def AC6G_14(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|D)|(B|C))
    carry = ((A&(B|C))|(C&D))
    return [sum,carry]
def AC6G_7(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|B)|(C|D))
    carry = ((C&(A|B))|(A&B))
    return [sum,carry]

############################### Ahmad and akabari ##################
def akbari(A,B,C,D):
  A=int(A)
  B=int(B)
  C=int(C)
  D=int(D)
  sum = nand(xnor(A,B),xnor(C,D))
  carry = nand(nand(A,B),nand(C,D))
  return [sum,carry]

def ahmad(A,B,C,D):
  A=int(A)
  B=int(B)
  C=int(C)
  D=int(D)
  sum = nand(nor(A,B),nor(C,D))
  carry = nor(nor(A,B),nor(C,D))
  return [sum,carry]
###############################MULTIPLIER##################
def multiply2(A,B):
    A=bin(A)[2:]
    B=bin(B)[2:]
    A=A.zfill(8)
    B=B.zfill(8)
    L=[]
    N=len(A)
    M=len(B)

    for i in range(M):
        k = []
        for j in range(N):
            k.append(AND(A[j],B[M-1-i]))
        L.append(k)

    ##column 5
    (x20,y20) = ACFGII_1(L[0][3],L[1][4],L[2][5],L[3][6])
    (x21,y21) = ACFGII_1(L[4][7],x20,0,0)


    ##column 6
    (x0,y0)   = ACFGII_1(L[0][2],L[1][3],L[2][4],L[3][5])
    (x19,y19) = ACFGII_1(L[4][6],L[5][7],x0,y20)
    (m5,c5)   = half_adder(x19,y21)

    ##column 7
    (x1,y1) = ACFGII_1(L[0][1],L[1][2],L[2][3],L[3][4])
    (x2,y2) = ACFGII_1(L[4][5],L[5][6],L[6][7],0)
    (x3,y3) = ACFGII_1(x1,x2,y0,0)
    (m6,c6) = full_adder(x3,y19,c5)

    ##column 8
    (x4,y4) = ahmad(L[0][0],L[1][1],L[2][2],L[3][3])
    (x5,y5) = ahmad(L[4][4],L[5][5],L[6][6],L[7][7])
    (x6,y6) = ahmad(x4,x5,y1,y2)
    (m7,c7) = full_adder(x6,y3,c6)

    ##column 9
    (x7,y7) = ACFGII_5(L[1][0],L[2][1],L[3][2],L[4][3])
    (x8,y8) = ACFGII_5(L[5][4],L[6][5],L[7][6],0)
    (x9,y9) = ACFGII_1(x7,x8,y4,y5)
    (m8,c8) = full_adder(x9,y6,c7)

    ##column 10
    (x10,y10) = ACFGII_11(L[2][0],L[3][1],L[4][2],L[5][3])
    (x11,y11) = ACFGII_11(L[6][4],L[7][5],0,0)
    (x12,y12) = ACFGII_10(x10,x11,y7,y8)
    (m9,c9)   = full_adder(x12,y9,c8)

    ##column 11
    (x13,y13) = AC6G_12(L[3][0],L[4][1],L[5][2],L[6][3])
    (x14,y14) = AC6G_7(L[7][4],x13,y10,y11)
    (m10,c10) = full_adder(x14,y12,c9)

    ##column 12
    (x15,y15) = AC6G_14(L[4][0],L[5][1],L[6][2],L[7][3])
    (x16,y16) = half_adder(x15,y13)
    (m11,c11) = full_adder(x16,y14,c10)

    ##column 13
    (x17,y17) = AC6G_7(L[5][0],L[6][1],L[7][2],y15)
    (m12,c12) = full_adder(x17,y16,c11)

    ##column 14
    (x18,y18) = half_adder(L[6][0],L[7][1])
    (m13,c13) = full_adder(x18,y17,c12)

    ##column 15
    (m14,c14) = full_adder(L[7][0],c13,y18)

    m15 = c14
    m0 = m1 = m2 = m3 = 0
    m4 = x21
    out=[m15,m14,m13,m12,m11,m10,m9,m8,m7,m6,m5,m4,m3,m2,m1,m0]
    result = ''.join(map(str, out))
    return(int(result,2))

