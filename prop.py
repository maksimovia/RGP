from CoolProp.CoolProp import PropsSI
import json, CoolProp.CoolProp as CP
CP.set_config_string(CP.ALTERNATIVE_REFPROP_PATH, 'C:/Program Files (x86)/REFPROP')


def crit(fluid):
    T = PropsSI('TCRIT', fluid)
    P = PropsSI('PCRIT', fluid)
    return {'T':T,'P':P}

def triple(fluid):
    T = PropsSI('TTRIPLE', fluid)
    P = PropsSI('PTRIPLE', fluid)
    return {'T':T,'P':P}

def R(fluid):
    R = PropsSI('GAS_CONSTANT', fluid)
    return R

def t_p(T,P,fluid):
    H = PropsSI('H','T', T, 'P', P, fluid)
    A = PropsSI('A','T', T, 'P', P, fluid)
    v = 1/PropsSI('D','T', T, 'P', P, fluid)
    cv = PropsSI('CVMOLAR','T', T, 'P', P, fluid)
    cp = PropsSI('CPMOLAR','T', T, 'P', P, fluid)
    dPdv = PropsSI('d(P)/d(1/D)|T','T', T, 'P', P, fluid)
    s = PropsSI('S','T', T, 'P', P, fluid)
    mu = PropsSI('V','T', T, 'P', P, fluid)
    lamda = PropsSI('L','T', T, 'P', P, fluid)
    return {'T':T, 'P':P, 'H':H, 'A':A, 'v':v, 'cv':cv,'cp':cp,'dPdv':dPdv,'s':s,'mu':mu,'lamda':lamda}

def p_q(P,Q,fluid):
    T = PropsSI('T', 'P', P,'Q', Q, fluid)
    H = PropsSI('H', 'P', P,'Q', Q, fluid)
    A = PropsSI('A', 'P', P,'Q', Q, fluid)
    v = 1/PropsSI('D','P', P,'Q', Q, fluid)
    
    cv = PropsSI('CVMOLAR','P', P,'Q', Q, fluid)
    cp = PropsSI('CPMOLAR','P', P,'Q', Q, fluid)
    dPdv = 1
    s = PropsSI('S','P', P,'Q', Q, fluid)
    mu = PropsSI('V','P', P,'Q', Q, fluid)
    lamda = PropsSI('L','P', P,'Q', Q, fluid)

    return {'T':T, 'P':P, 'H':H, 'A':A, 'v':v, 'cv':cv,'cp':cp,'dPdv':dPdv,'s':s,'mu':mu,'lamda':lamda}
