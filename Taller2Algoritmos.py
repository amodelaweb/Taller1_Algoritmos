import math
def FindMaxCrossSubArray(A,l,m,h):
    vl,s,ml,mr= -math.inf , 0,-1,-1
    for i in range(m,(l-1),-1):
        s += A[i]
        if s > vl :
            vl ,ml = s,i
    vr,s = -math.inf,0
    for j in range((m+1),(h+1)):
        s += A[j]
        if s > vr:
            vr,mr = s , j
    return [ml,mr,(vl + vr)]
def FindMaxSubArrayAux(A,l,h):
    if h <= l : return [l,h,A[l]]
    else:
        m= int((l+h)/2)
        A,B,C = FindMaxSubArrayAux(A,l,m),FindMaxSubArrayAux(A,m+1,h),FindMaxCrossSubArray(A,l,m,h)
        if A[2] >= B[2] and A[2]>= C[2] : return A
        elif B[2] >= A[2] and B[2] >= C[2]: return B
        else: return C
def FindMaxSubArray(A):
    return FindMaxSubArrayAux(A,0,len(A)-1) ;
def main():
    #ESTA EN FORMATO RUN EXPERIMENT, SOLO SE QUITA EL MAIN, ESTA DE PRUEBA

    array = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
    change = [0,13,-3,-25,20,-3,-16,23,18,20,-7,12,-5,-22,15,-4,7]
    res = FindMaxSubArray(array)
    print(res)

main()
