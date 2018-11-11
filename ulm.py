def rows(M):
    return len(M)

def columns(M):
    return len(M[0])

def inverts_matrix(M):
    n_cols=columns(M)
    n_rows=rows(M)
    j=0
    M_inv=inizializes_matrix(n_cols)
    Mart=[[],[0,0,0]]
    while j < n_cols:

        for i in range(n_rows):
            M_inv[j].append(int(M[i][j]))

        j += 1
        return M_inv


def inizializes_matrix(row):
    M=[]
    for i in range(row):
        M.append([])
    return (M)

def matrixs_sums(M_1,M_2):
    M_S = inizializes_matrix(len(M_1))
    if True:
        for i in range(len(M_1)):
            for j in range(len(M_1[0])):
                M_S[i].append(M_1[i][j] +M_2[i][j])
    return M_S

def exchanges_rows(M,row_1,row_2):
    M_Ex=M
    Ex=M[row_1]
    M[row_1]=M_Ex[row_2]
    M[row_2]=Ex
    return(M_Ex)

def insert_rows(M,row,pos):
    M_ret=M
    M_ret[pos]=row
    return(M_ret)

def matrixs_equals(M_1,M_2):
    if len(M_1)==len(M_2):
        for i in range(len(M_1)):
            for j in range(len(M_1[0])):
                if(M_1[i][j]!=M_2[i][j]):
                    return False
    else:
        return False
    return True

def matrixs_rows_equals(M_1,M_2):
    if len(M_1)==len(M_2):
        for i in range(len(M_1)):
            if(M_1[i]!=M_2[i]):
                    return False
    else:
        return False
    return True

def 
