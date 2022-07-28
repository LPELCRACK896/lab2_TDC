
nodos = [
        ["q1","vacio","vacio","vacio","q1"],
        ["q1","q1_q4","q2","vacio"],
        ["q1_q4","q1_q4","q2_q3","vacio"],
        ["q2","q3","vacio","vacio"],
        ["q2_q3_q5","q3","vacio","vacio"],
        ["q2_q3_q5","q3","vacio","vacio"],
        ["q3_q5","q3","vacio","vacio"],
        ["q3_q5","q3","vacio","vacio"],
        ]

simbolos =  ["0","1","2","3","4","5","6","7","8","9","+","-","e", "."]

estados =   ["q0","q1","q1_q4","q2","q2_q3","q2_q3_q5","q3","q3_q5"]

F = "q5"

s = "q0"

def transition(q, a, d):
    if a not in simbolos:
        print(f"Trancision no valida: {a} ")
        return -1
    if q == "vacio":
        return "vacio"
    if q not in estados:
        print(f"Estado no valido: {q}")
        return -1
    index_simb = -1
    
    if simbolos.index(a)<=9 and simbolos.index(a)>=0: # 0....9
        index_simb = 1
    elif a=="e":
        index_simb = 0 
    elif a=="+" or a=="-":
        index_simb = 3
    elif a==".":
        index_simb = 2
    if index_simb==-1:
        return
    
    return list(d)[estados.index(q)][index_simb]
     
def final_state(q, w, δ):
    estado_actual = q
    for a in w:
        estado_temp = transition(estado_actual, a, δ)
        if estado_temp == -1:
            return
        estado_actual = estado_temp
    return estado_actual

def derivation(q: str, w: str, d: str):
    resultado = []
    for i in w:
        newState = (transition(q,i,d))
        if newState == -1:
            print("CADENA NO VALIDA")
            return 
        q = newState
        resultado.append(q)
    return resultado

def accepted(q: str, w: str, F: str, δ: str):
    return F in final_state(q, w, δ) 

#print(final_state("q0", "ee0L", nodos))

print(derivation("q0", "0.22", nodos))