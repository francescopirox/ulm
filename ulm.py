def rows(m):
    return len(m)


def columns(m):
    return len(m[0])


def inverts_matrix(m):
    n_cols = columns(m)
    n_rows = rows(m)
    j = 0
    m_inv = inizializes_matrix(n_cols)
    mart = [[], [0, 0, 0]]
    while j < n_cols:

        for i in range(n_rows):
            m_inv[j].append(int(m[i][j]))

        j += 1
        return m_inv


def inizializes_matrix(row):
    m = []
    for i in range(row):
        m.append([])
    return m


def matrixs_sums(m_1, m_2):
    M_S = inizializes_matrix(len(m_1))
    if True:
        for i in range(len(m_1)):
            for j in range(len(m_1[0])):
                M_S[i].append(m_1[i][j] + m_2[i][j])
    return M_S


def exchanges_rows(m, row_1, row_2):
    m_Ex = m
    ex = m[row_1]
    m[row_1] = m_Ex[row_2]
    m[row_2] = ex
    return m_Ex


def insert_rows(m, row, pos):
    m_ret = m
    m_ret[pos] = row
    return m_ret


def matrixs_equals(m_1, m_2):
    if len(m_1) == len(m_2):
        for i in range(len(m_1)):
            for j in range(len(m_1[0])):
                if m_1[i][j] != m_2[i][j]:
                    return False
    else:
        return False
    return True


def matrixs_rows_equals(m_1, m_2):
    if len(m_1) == len(m_2):
        for i in range(len(m_1)):
            if m_1[i] != m_2[i]:
                    return False
    else:
        return False
    return True
