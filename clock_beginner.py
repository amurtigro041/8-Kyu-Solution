def past(h, m, s):
    h_mil = h*36*10**5
    m_mil = m*60000
    s_mil = s*1000
    result = h_mil + m_mil + s_mil
    return(result)
print(past(0,1,1))
print(past(1,1,1))