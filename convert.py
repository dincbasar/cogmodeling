S = """(A ISA outline s0 c01 d0 c10 s1 c10 d1 c20 s2 c01 d2 c12 s3 c12 d3 c22 s4 c10 d4 c12)
(B ISA outline s0 c00 d0 c02 s1 c00 d1 c02 s2 c02 d2 c12 s3 c12 d3 c10 s4 c10 d4 c12 s5 c12 d5 c22 s6 c22 d6 c20)
(C ISA outline s0 c02 d0 c00 s1 c00 d1 c20 s2 c20 d2 c22)
(D ISA outline s0 c00 d0 c02 s1 c00 d1 c01 s2 c01 d2 c12 s3 c12 d3 c21 s4 c21 d4 c20)
(E ISA outline s0 c00 d0 c20 s1 c00 d1 c02 s2 c10 d2 c12 s3 c20 d3 c22)
(F ISA outline s0 c00 d0 c20 s1 c00 d1 c02 s2 c10 d2 c12)
(G ISA outline s0 c02 d0 c00 s1 c00 d1 c20 s2 c20 d2 c22 s3 c22 d3 c12 s4 c12 d4 c11)
(H ISA outline s0 c00 d0 c20 s1 c10 d1 c12 s2 c02 d3 c22)
(I ISA outline s0 c00 d0 c02 s1 c01 d1 c21 s2 c20 d2 c22)
(J ISA outline s0 c00 d0 c02 s1 c01 d1 c21 s2 c21 d2 c20)
(K ISA outline s0 c00 d0 c20 s1 c02 d1 c10 s2 c10 d2 c22)
(L ISA outline s0 c00 d0 c20 s1 c20 d1 c22)
(M ISA outline s0 c00 d0 c20 s1 c00 d1 c21 s2 c21 d2 c02 s3 c02 d3 c22)
(N ISA outline s0 c00 d0 c20 s1 c00 d1 c22 s2 c02 d2 c22)
(O ISA outline s0 c00 d0 c20 s1 c02 d1 c22 s2 c22 d2 c02 s3 c02 d3 c00)
(P ISA outline s0 c00 d0 c20 s1 c00 d1 c02 s2 c02 d2 c12 s3 c12 d3 c10)
(Q ISA outline s0 c00 d0 c20 s1 c20 d1 c21 s2 c21 d2 c12 s3 c12 d3 c02 s4 c02 d4 c00 s5 c11 d5 c22)
(R ISA outline s0 c00 d0 c20 s1 c00 d1 c02 s2 c02 d2 c12 s3 c12 d3 c10 s4 c10 d4 c22)
(S ISA outline s0 c02 d0 c00 s1 c00 d1 c10 s2 c10 d2 c12 s3 c12 d3 c22 s4 c22 d4 c20)
(T ISA outline s0 c00 d0 c02 s1 c01 d1 c21)
(U ISA outline s0 c00 d0 c20 s1 c20 d1 c22 s2 c22 d2 c02)
(V ISA outline s0 c00 d0 c10 s1 c10 d1 c21 s2 c21 d2 c12 s3 c12 d3 c02)
(W ISA outline s0 c00 d0 c20 s1 c20 d1 c11 s2 c11 d2 c22 s3 c22 d3 c02)
(X ISA outline s0 c00 d0 c22 s1 c20 d1 c02)
(Y ISA outline s0 c00 d0 c11 s1 c02 d1 c11 s2 c11 d2 c21)
(Z ISA outline s0 c00 d0 c02 s1 c02 d1 c20 s2 c20 d2 c22)"""

# (A-first letter A count first s c01 d c10)

def convert():
    l = S.split("\n")
    for i in range(len(l)):
        l[i] = l[i][1:-1]
        l[i] = l[i].split(" ")
    newL = [[""] * 6 for row in range(len(l))]
    for i in range(len(l)):
        row = l[i]
        newL.append([])
        letter = row.pop(0)
        row = row[2:]
        counts = ["first", "second", "third", "fourth", "fifth", "sixth"]
        for j in range(6):
            strx = "[\'" + letter +  "-" + counts[j] + "\', "
            strx += "\'isa\', " + "\'outline\', "
            strx += "\'letter\', " + "\"\'" + letter.lower() + "\'\", \'count\', \'" + counts[j]
            strx += "\', \'start-coor\', \'" + row[1] + "\', \'dest-coor\', \'" + row[3] + "\'],"
            newL[i][j] = strx
            row = row[4:]
            if (row == []): break
        while "" in newL[i]:
            newL[i].remove("")

    while [] in newL:
        newL.remove([])

    f = open("out.txt", "wt")

    for row in newL:
        for elt in row:
            f.write(elt + "\n")
        # f.write("\n")

    f.close()

convert();
