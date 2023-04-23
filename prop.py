from ctREFPROP.ctREFPROP import REFPROPFunctionLibrary
RP = REFPROPFunctionLibrary('C:/Program Files (x86)/REFPROP')

iUnits = 21
iMass = 2
iFlag = 0

def crit(fluid):
    comp=[]
    for i in range(1, len(fluid.split(";")),2): comp.append(float(fluid.split(";")[i]))
    res = RP.REFPROPdll(fluid, 'CRIT', 'T;P', iUnits, iMass, iFlag, 0, 0, comp)
    T = res.Output[0]
    P = res.Output[1]
    return {'T':T,'P':P}

def triple(fluid):
    comp=[]
    for i in range(1, len(fluid.split(";")),2): comp.append(float(fluid.split(";")[i]))
    res = RP.REFPROPdll(fluid, 'TRIP', 'T;P', iUnits, iMass, iFlag, 0, 0, comp)
    T = res.Output[0]
    P = res.Output[1]
    return {'T':T,'P':P}

def R(fluid):
    comp=[]
    for i in range(1, len(fluid.split(";")),2): comp.append(float(fluid.split(";")[i]))
    res = RP.REFPROPdll(fluid, 'TP', 'R', iUnits, iMass, iFlag, 0, 0, comp)
    R = res.Output[0]
    return {'R':R}

def t_p(T,P,fluid):
    comp=[]
    for i in range(1, len(fluid.split(";")),2): comp.append(float(fluid.split(";")[i]))
    res = RP.REFPROPdll(fluid, 'TP', 'T;P;H;W;V;CV;CP;DPDD;S;VIS;TCX', iUnits, iMass, iFlag, T, P, comp)
    T = res.Output[0]
    P = res.Output[1]
    H = res.Output[2]
    W = res.Output[3]
    V = res.Output[4]
    Cv = res.Output[5]
    Cp = res.Output[6]
    dPdV = -res.Output[7] / res.Output[4]**2
    S = res.Output[8]
    mu = res.Output[9]*res.Output[4]
    lamda = res.Output[10]
    return {'T':T, 'P':P, 'H':H, 'W':W, 'V':V, 'Cv':Cv,'Cp':Cp,'dPdV':dPdV,'S':S,'mu':mu,'lamda':lamda}

def p_q(P,Q,fluid):
    comp=[]
    for i in range(1, len(fluid.split(";")),2): comp.append(float(fluid.split(";")[i]))
    res = RP.REFPROPdll(fluid, 'PQ', 'T;P;H;W;V;CV;CP;DPDD;S;VIS;TCX', iUnits, iMass, iFlag, P, Q, comp)
    T = res.Output[0]
    P = res.Output[1]
    H = res.Output[2]
    W = res.Output[3]
    V = res.Output[4]
    Cv = res.Output[5]
    Cp = res.Output[6]
    dPdV = -res.Output[7] / res.Output[4]**2
    S = res.Output[8]
    mu = res.Output[9]*res.Output[4]
    lamda = res.Output[10]
    return {'T':T, 'P':P, 'H':H, 'W':W, 'V':V, 'Cv':Cv,'Cp':Cp,'dPdV':dPdV,'S':S,'mu':mu,'lamda':lamda}
