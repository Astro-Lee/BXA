import numpy
"""
transform [0,1] using the inverse gaussian cdf
"""

"""
generated using
x = numpy.linspace(1e-16, 1-1e-16, 1000-1)
y = rv.ppf(x)         
for a, b, c in zip(y[::3], y[1::3], y[2::3]):
    print '\t%.8e, %.8e, %.8e,' % (a, b, c)

"""

interpy = numpy.array([ 
        -8.22208222e+00, -3.08963768e+00, -2.87753015e+00,
        -2.74712487e+00, -2.65139379e+00, -2.57513696e+00,
        -2.51143778e+00, -2.45654416e+00, -2.40818479e+00,
        -2.36487675e+00, -2.32559662e+00, -2.28960736e+00,
        -2.25635997e+00, -2.22543419e+00, -2.19650088e+00,
        -2.16929730e+00, -2.14361026e+00, -2.11926431e+00,
        -2.09611327e+00, -2.07403401e+00, -2.05292182e+00,
        -2.03268687e+00, -2.01325151e+00, -1.99454814e+00,
        -1.97651753e+00, -1.95910749e+00, -1.94227177e+00,
        -1.92596923e+00, -1.91016304e+00, -1.89482015e+00,
        -1.87991077e+00, -1.86540792e+00, -1.85128713e+00,
        -1.83752612e+00, -1.82410452e+00, -1.81100369e+00,
        -1.79820651e+00, -1.78569721e+00, -1.77346127e+00,
        -1.76148522e+00, -1.74975661e+00, -1.73826387e+00,
        -1.72699625e+00, -1.71594371e+00, -1.70509691e+00,
        -1.69444707e+00, -1.68398603e+00, -1.67370609e+00,
        -1.66360004e+00, -1.65366109e+00, -1.64388286e+00,
        -1.63425933e+00, -1.62478482e+00, -1.61545395e+00,
        -1.60626165e+00, -1.59720310e+00, -1.58827376e+00,
        -1.57946928e+00, -1.57078557e+00, -1.56221872e+00,
        -1.55376500e+00, -1.54542090e+00, -1.53718302e+00,
        -1.52904816e+00, -1.52101325e+00, -1.51307535e+00,
        -1.50523166e+00, -1.49747950e+00, -1.48981630e+00,
        -1.48223960e+00, -1.47474705e+00, -1.46733639e+00,
        -1.46000545e+00, -1.45275214e+00, -1.44557446e+00,
        -1.43847050e+00, -1.43143840e+00, -1.42447638e+00,
        -1.41758273e+00, -1.41075579e+00, -1.40399398e+00,
        -1.39729576e+00, -1.39065965e+00, -1.38408423e+00,
        -1.37756811e+00, -1.37110996e+00, -1.36470849e+00,
        -1.35836247e+00, -1.35207068e+00, -1.34583197e+00,
        -1.33964520e+00, -1.33350929e+00, -1.32742318e+00,
        -1.32138584e+00, -1.31539628e+00, -1.30945355e+00,
        -1.30355671e+00, -1.29770485e+00, -1.29189709e+00,
        -1.28613259e+00, -1.28041050e+00, -1.27473004e+00,
        -1.26909042e+00, -1.26349087e+00, -1.25793066e+00,
        -1.25240907e+00, -1.24692541e+00, -1.24147898e+00,
        -1.23606914e+00, -1.23069523e+00, -1.22535663e+00,
        -1.22005272e+00, -1.21478292e+00, -1.20954664e+00,
        -1.20434331e+00, -1.19917239e+00, -1.19403333e+00,
        -1.18892562e+00, -1.18384874e+00, -1.17880219e+00,
        -1.17378548e+00, -1.16879814e+00, -1.16383971e+00,
        -1.15890972e+00, -1.15400774e+00, -1.14913334e+00,
        -1.14428609e+00, -1.13946558e+00, -1.13467140e+00,
        -1.12990316e+00, -1.12516047e+00, -1.12044295e+00,
        -1.11575024e+00, -1.11108197e+00, -1.10643780e+00,
        -1.10181736e+00, -1.09722033e+00, -1.09264636e+00,
        -1.08809515e+00, -1.08356636e+00, -1.07905968e+00,
        -1.07457482e+00, -1.07011147e+00, -1.06566933e+00,
        -1.06124812e+00, -1.05684756e+00, -1.05246738e+00,
        -1.04810729e+00, -1.04376704e+00, -1.03944636e+00,
        -1.03514499e+00, -1.03086270e+00, -1.02659923e+00,
        -1.02235433e+00, -1.01812778e+00, -1.01391934e+00,
        -1.00972878e+00, -1.00555588e+00, -1.00140041e+00,
        -9.97262163e-01, -9.93140925e-01, -9.89036486e-01,
        -9.84948642e-01, -9.80877191e-01, -9.76821935e-01,
        -9.72782680e-01, -9.68759234e-01, -9.64751410e-01,
        -9.60759022e-01, -9.56781890e-01, -9.52819835e-01,
        -9.48872681e-01, -9.44940255e-01, -9.41022387e-01,
        -9.37118911e-01, -9.33229662e-01, -9.29354478e-01,
        -9.25493201e-01, -9.21645673e-01, -9.17811740e-01,
        -9.13991251e-01, -9.10184057e-01, -9.06390009e-01,
        -9.02608965e-01, -8.98840780e-01, -8.95085316e-01,
        -8.91342433e-01, -8.87611995e-01, -8.83893869e-01,
        -8.80187923e-01, -8.76494025e-01, -8.72812049e-01,
        -8.69141868e-01, -8.65483356e-01, -8.61836393e-01,
        -8.58200857e-01, -8.54576628e-01, -8.50963589e-01,
        -8.47361625e-01, -8.43770622e-01, -8.40190466e-01,
        -8.36621047e-01, -8.33062256e-01, -8.29513984e-01,
        -8.25976125e-01, -8.22448575e-01, -8.18931229e-01,
        -8.15423986e-01, -8.11926744e-01, -8.08439405e-01,
        -8.04961870e-01, -8.01494043e-01, -7.98035827e-01,
        -7.94587130e-01, -7.91147857e-01, -7.87717916e-01,
        -7.84297218e-01, -7.80885673e-01, -7.77483191e-01,
        -7.74089687e-01, -7.70705074e-01, -7.67329267e-01,
        -7.63962182e-01, -7.60603736e-01, -7.57253847e-01,
        -7.53912434e-01, -7.50579418e-01, -7.47254719e-01,
        -7.43938260e-01, -7.40629963e-01, -7.37329752e-01,
        -7.34037552e-01, -7.30753289e-01, -7.27476889e-01,
        -7.24208280e-01, -7.20947391e-01, -7.17694149e-01,
        -7.14448485e-01, -7.11210331e-01, -7.07979616e-01,
        -7.04756275e-01, -7.01540239e-01, -6.98331443e-01,
        -6.95129821e-01, -6.91935308e-01, -6.88747842e-01,
        -6.85567357e-01, -6.82393792e-01, -6.79227086e-01,
        -6.76067175e-01, -6.72914002e-01, -6.69767504e-01,
        -6.66627623e-01, -6.63494301e-01, -6.60367480e-01,
        -6.57247101e-01, -6.54133109e-01, -6.51025447e-01,
        -6.47924060e-01, -6.44828893e-01, -6.41739890e-01,
        -6.38656999e-01, -6.35580166e-01, -6.32509339e-01,
        -6.29444464e-01, -6.26385490e-01, -6.23332367e-01,
        -6.20285043e-01, -6.17243468e-01, -6.14207593e-01,
        -6.11177368e-01, -6.08152745e-01, -6.05133675e-01,
        -6.02120111e-01, -5.99112005e-01, -5.96109311e-01,
        -5.93111982e-01, -5.90119971e-01, -5.87133234e-01,
        -5.84151726e-01, -5.81175401e-01, -5.78204216e-01,
        -5.75238127e-01, -5.72277089e-01, -5.69321061e-01,
        -5.66369999e-01, -5.63423862e-01, -5.60482606e-01,
        -5.57546191e-01, -5.54614576e-01, -5.51687720e-01,
        -5.48765582e-01, -5.45848123e-01, -5.42935302e-01,
        -5.40027081e-01, -5.37123420e-01, -5.34224280e-01,
        -5.31329623e-01, -5.28439412e-01, -5.25553608e-01,
        -5.22672175e-01, -5.19795074e-01, -5.16922270e-01,
        -5.14053726e-01, -5.11189405e-01, -5.08329272e-01,
        -5.05473292e-01, -5.02621428e-01, -4.99773646e-01,
        -4.96929912e-01, -4.94090191e-01, -4.91254449e-01,
        -4.88422651e-01, -4.85594765e-01, -4.82770756e-01,
        -4.79950593e-01, -4.77134242e-01, -4.74321670e-01,
        -4.71512845e-01, -4.68707735e-01, -4.65906309e-01,
        -4.63108534e-01, -4.60314380e-01, -4.57523815e-01,
        -4.54736808e-01, -4.51953328e-01, -4.49173346e-01,
        -4.46396831e-01, -4.43623753e-01, -4.40854083e-01,
        -4.38087790e-01, -4.35324845e-01, -4.32565220e-01,
        -4.29808885e-01, -4.27055811e-01, -4.24305971e-01,
        -4.21559335e-01, -4.18815876e-01, -4.16075565e-01,
        -4.13338376e-01, -4.10604279e-01, -4.07873249e-01,
        -4.05145257e-01, -4.02420277e-01, -3.99698282e-01,
        -3.96979245e-01, -3.94263140e-01, -3.91549941e-01,
        -3.88839621e-01, -3.86132154e-01, -3.83427515e-01,
        -3.80725677e-01, -3.78026616e-01, -3.75330306e-01,
        -3.72636722e-01, -3.69945839e-01, -3.67257632e-01,
        -3.64572077e-01, -3.61889148e-01, -3.59208822e-01,
        -3.56531073e-01, -3.53855879e-01, -3.51183215e-01,
        -3.48513057e-01, -3.45845381e-01, -3.43180165e-01,
        -3.40517384e-01, -3.37857015e-01, -3.35199035e-01,
        -3.32543421e-01, -3.29890151e-01, -3.27239200e-01,
        -3.24590548e-01, -3.21944170e-01, -3.19300046e-01,
        -3.16658152e-01, -3.14018466e-01, -3.11380966e-01,
        -3.08745631e-01, -3.06112438e-01, -3.03481366e-01,
        -3.00852393e-01, -2.98225498e-01, -2.95600659e-01,
        -2.92977855e-01, -2.90357066e-01, -2.87738269e-01,
        -2.85121443e-01, -2.82506569e-01, -2.79893625e-01,
        -2.77282591e-01, -2.74673445e-01, -2.72066168e-01,
        -2.69460740e-01, -2.66857139e-01, -2.64255346e-01,
        -2.61655340e-01, -2.59057103e-01, -2.56460612e-01,
        -2.53865850e-01, -2.51272796e-01, -2.48681430e-01,
        -2.46091733e-01, -2.43503685e-01, -2.40917268e-01,
        -2.38332461e-01, -2.35749245e-01, -2.33167602e-01,
        -2.30587512e-01, -2.28008955e-01, -2.25431914e-01,
        -2.22856369e-01, -2.20282302e-01, -2.17709693e-01,
        -2.15138525e-01, -2.12568778e-01, -2.10000434e-01,
        -2.07433474e-01, -2.04867880e-01, -2.02303635e-01,
        -1.99740718e-01, -1.97179114e-01, -1.94618802e-01,
        -1.92059765e-01, -1.89501986e-01, -1.86945446e-01,
        -1.84390127e-01, -1.81836011e-01, -1.79283081e-01,
        -1.76731319e-01, -1.74180708e-01, -1.71631229e-01,
        -1.69082865e-01, -1.66535598e-01, -1.63989412e-01,
        -1.61444288e-01, -1.58900210e-01, -1.56357160e-01,
        -1.53815121e-01, -1.51274075e-01, -1.48734006e-01,
        -1.46194895e-01, -1.43656728e-01, -1.41119485e-01,
        -1.38583150e-01, -1.36047707e-01, -1.33513137e-01,
        -1.30979426e-01, -1.28446554e-01, -1.25914507e-01,
        -1.23383267e-01, -1.20852816e-01, -1.18323140e-01,
        -1.15794220e-01, -1.13266041e-01, -1.10738586e-01,
        -1.08211837e-01, -1.05685780e-01, -1.03160396e-01,
        -1.00635671e-01, -9.81115863e-02, -9.55881269e-02,
        -9.30652760e-02, -9.05430173e-02, -8.80213345e-02,
        -8.55002114e-02, -8.29796315e-02, -8.04595787e-02,
        -7.79400368e-02, -7.54209896e-02, -7.29024208e-02,
        -7.03843144e-02, -6.78666543e-02, -6.53494242e-02,
        -6.28326082e-02, -6.03161901e-02, -5.78001538e-02,
        -5.52844835e-02, -5.27691629e-02, -5.02541762e-02,
        -4.77395073e-02, -4.52251403e-02, -4.27110591e-02,
        -4.01972479e-02, -3.76836906e-02, -3.51703714e-02,
        -3.26572744e-02, -3.01443836e-02, -2.76316831e-02,
        -2.51191571e-02, -2.26067896e-02, -2.00945649e-02,
        -1.75824669e-02, -1.50704799e-02, -1.25585880e-02,
        -1.00467753e-02, -7.53502603e-03, -5.02332428e-03,
        -2.51165422e-03, -1.39145821e-16, 2.51165422e-03,
        5.02332428e-03, 7.53502603e-03, 1.00467753e-02,
        1.25585880e-02, 1.50704799e-02, 1.75824669e-02,
        2.00945649e-02, 2.26067896e-02, 2.51191571e-02,
        2.76316831e-02, 3.01443836e-02, 3.26572744e-02,
        3.51703714e-02, 3.76836906e-02, 4.01972479e-02,
        4.27110591e-02, 4.52251403e-02, 4.77395073e-02,
        5.02541762e-02, 5.27691629e-02, 5.52844835e-02,
        5.78001538e-02, 6.03161901e-02, 6.28326082e-02,
        6.53494242e-02, 6.78666543e-02, 7.03843144e-02,
        7.29024208e-02, 7.54209896e-02, 7.79400368e-02,
        8.04595787e-02, 8.29796315e-02, 8.55002114e-02,
        8.80213345e-02, 9.05430173e-02, 9.30652760e-02,
        9.55881269e-02, 9.81115863e-02, 1.00635671e-01,
        1.03160396e-01, 1.05685780e-01, 1.08211837e-01,
        1.10738586e-01, 1.13266041e-01, 1.15794220e-01,
        1.18323140e-01, 1.20852816e-01, 1.23383267e-01,
        1.25914507e-01, 1.28446554e-01, 1.30979426e-01,
        1.33513137e-01, 1.36047707e-01, 1.38583150e-01,
        1.41119485e-01, 1.43656728e-01, 1.46194895e-01,
        1.48734006e-01, 1.51274075e-01, 1.53815121e-01,
        1.56357160e-01, 1.58900210e-01, 1.61444288e-01,
        1.63989412e-01, 1.66535598e-01, 1.69082865e-01,
        1.71631229e-01, 1.74180708e-01, 1.76731319e-01,
        1.79283081e-01, 1.81836011e-01, 1.84390127e-01,
        1.86945446e-01, 1.89501986e-01, 1.92059765e-01,
        1.94618802e-01, 1.97179114e-01, 1.99740718e-01,
        2.02303635e-01, 2.04867880e-01, 2.07433474e-01,
        2.10000434e-01, 2.12568778e-01, 2.15138525e-01,
        2.17709693e-01, 2.20282302e-01, 2.22856369e-01,
        2.25431914e-01, 2.28008955e-01, 2.30587512e-01,
        2.33167602e-01, 2.35749245e-01, 2.38332461e-01,
        2.40917268e-01, 2.43503685e-01, 2.46091733e-01,
        2.48681430e-01, 2.51272796e-01, 2.53865850e-01,
        2.56460612e-01, 2.59057103e-01, 2.61655340e-01,
        2.64255346e-01, 2.66857139e-01, 2.69460740e-01,
        2.72066168e-01, 2.74673445e-01, 2.77282591e-01,
        2.79893625e-01, 2.82506569e-01, 2.85121443e-01,
        2.87738269e-01, 2.90357066e-01, 2.92977855e-01,
        2.95600659e-01, 2.98225498e-01, 3.00852393e-01,
        3.03481366e-01, 3.06112438e-01, 3.08745631e-01,
        3.11380966e-01, 3.14018466e-01, 3.16658152e-01,
        3.19300046e-01, 3.21944170e-01, 3.24590548e-01,
        3.27239200e-01, 3.29890151e-01, 3.32543421e-01,
        3.35199035e-01, 3.37857015e-01, 3.40517384e-01,
        3.43180165e-01, 3.45845381e-01, 3.48513057e-01,
        3.51183215e-01, 3.53855879e-01, 3.56531073e-01,
        3.59208822e-01, 3.61889148e-01, 3.64572077e-01,
        3.67257632e-01, 3.69945839e-01, 3.72636722e-01,
        3.75330306e-01, 3.78026616e-01, 3.80725677e-01,
        3.83427515e-01, 3.86132154e-01, 3.88839621e-01,
        3.91549941e-01, 3.94263140e-01, 3.96979245e-01,
        3.99698282e-01, 4.02420277e-01, 4.05145257e-01,
        4.07873249e-01, 4.10604279e-01, 4.13338376e-01,
        4.16075565e-01, 4.18815876e-01, 4.21559335e-01,
        4.24305971e-01, 4.27055811e-01, 4.29808885e-01,
        4.32565220e-01, 4.35324845e-01, 4.38087790e-01,
        4.40854083e-01, 4.43623753e-01, 4.46396831e-01,
        4.49173346e-01, 4.51953328e-01, 4.54736808e-01,
        4.57523815e-01, 4.60314380e-01, 4.63108534e-01,
        4.65906309e-01, 4.68707735e-01, 4.71512845e-01,
        4.74321670e-01, 4.77134242e-01, 4.79950593e-01,
        4.82770756e-01, 4.85594765e-01, 4.88422651e-01,
        4.91254449e-01, 4.94090191e-01, 4.96929912e-01,
        4.99773646e-01, 5.02621428e-01, 5.05473292e-01,
        5.08329272e-01, 5.11189405e-01, 5.14053726e-01,
        5.16922270e-01, 5.19795074e-01, 5.22672175e-01,
        5.25553608e-01, 5.28439412e-01, 5.31329623e-01,
        5.34224280e-01, 5.37123420e-01, 5.40027081e-01,
        5.42935302e-01, 5.45848123e-01, 5.48765582e-01,
        5.51687720e-01, 5.54614576e-01, 5.57546191e-01,
        5.60482606e-01, 5.63423862e-01, 5.66369999e-01,
        5.69321061e-01, 5.72277089e-01, 5.75238127e-01,
        5.78204216e-01, 5.81175401e-01, 5.84151726e-01,
        5.87133234e-01, 5.90119971e-01, 5.93111982e-01,
        5.96109311e-01, 5.99112005e-01, 6.02120111e-01,
        6.05133675e-01, 6.08152745e-01, 6.11177368e-01,
        6.14207593e-01, 6.17243468e-01, 6.20285043e-01,
        6.23332367e-01, 6.26385490e-01, 6.29444464e-01,
        6.32509339e-01, 6.35580166e-01, 6.38656999e-01,
        6.41739890e-01, 6.44828893e-01, 6.47924060e-01,
        6.51025447e-01, 6.54133109e-01, 6.57247101e-01,
        6.60367480e-01, 6.63494301e-01, 6.66627623e-01,
        6.69767504e-01, 6.72914002e-01, 6.76067175e-01,
        6.79227086e-01, 6.82393792e-01, 6.85567357e-01,
        6.88747842e-01, 6.91935308e-01, 6.95129821e-01,
        6.98331443e-01, 7.01540239e-01, 7.04756275e-01,
        7.07979616e-01, 7.11210331e-01, 7.14448485e-01,
        7.17694149e-01, 7.20947391e-01, 7.24208280e-01,
        7.27476889e-01, 7.30753289e-01, 7.34037552e-01,
        7.37329752e-01, 7.40629963e-01, 7.43938260e-01,
        7.47254719e-01, 7.50579418e-01, 7.53912434e-01,
        7.57253847e-01, 7.60603736e-01, 7.63962182e-01,
        7.67329267e-01, 7.70705074e-01, 7.74089687e-01,
        7.77483191e-01, 7.80885673e-01, 7.84297218e-01,
        7.87717916e-01, 7.91147857e-01, 7.94587130e-01,
        7.98035827e-01, 8.01494043e-01, 8.04961870e-01,
        8.08439405e-01, 8.11926744e-01, 8.15423986e-01,
        8.18931229e-01, 8.22448575e-01, 8.25976125e-01,
        8.29513984e-01, 8.33062256e-01, 8.36621047e-01,
        8.40190466e-01, 8.43770622e-01, 8.47361625e-01,
        8.50963589e-01, 8.54576628e-01, 8.58200857e-01,
        8.61836393e-01, 8.65483356e-01, 8.69141868e-01,
        8.72812049e-01, 8.76494025e-01, 8.80187923e-01,
        8.83893869e-01, 8.87611995e-01, 8.91342433e-01,
        8.95085316e-01, 8.98840780e-01, 9.02608965e-01,
        9.06390009e-01, 9.10184057e-01, 9.13991251e-01,
        9.17811740e-01, 9.21645673e-01, 9.25493201e-01,
        9.29354478e-01, 9.33229662e-01, 9.37118911e-01,
        9.41022387e-01, 9.44940255e-01, 9.48872681e-01,
        9.52819835e-01, 9.56781890e-01, 9.60759022e-01,
        9.64751410e-01, 9.68759234e-01, 9.72782680e-01,
        9.76821935e-01, 9.80877191e-01, 9.84948642e-01,
        9.89036486e-01, 9.93140925e-01, 9.97262163e-01,
        1.00140041e+00, 1.00555588e+00, 1.00972878e+00,
        1.01391934e+00, 1.01812778e+00, 1.02235433e+00,
        1.02659923e+00, 1.03086270e+00, 1.03514499e+00,
        1.03944636e+00, 1.04376704e+00, 1.04810729e+00,
        1.05246738e+00, 1.05684756e+00, 1.06124812e+00,
        1.06566933e+00, 1.07011147e+00, 1.07457482e+00,
        1.07905968e+00, 1.08356636e+00, 1.08809515e+00,
        1.09264636e+00, 1.09722033e+00, 1.10181736e+00,
        1.10643780e+00, 1.11108197e+00, 1.11575024e+00,
        1.12044295e+00, 1.12516047e+00, 1.12990316e+00,
        1.13467140e+00, 1.13946558e+00, 1.14428609e+00,
        1.14913334e+00, 1.15400774e+00, 1.15890972e+00,
        1.16383971e+00, 1.16879814e+00, 1.17378548e+00,
        1.17880219e+00, 1.18384874e+00, 1.18892562e+00,
        1.19403333e+00, 1.19917239e+00, 1.20434331e+00,
        1.20954664e+00, 1.21478292e+00, 1.22005272e+00,
        1.22535663e+00, 1.23069523e+00, 1.23606914e+00,
        1.24147898e+00, 1.24692541e+00, 1.25240907e+00,
        1.25793066e+00, 1.26349087e+00, 1.26909042e+00,
        1.27473004e+00, 1.28041050e+00, 1.28613259e+00,
        1.29189709e+00, 1.29770485e+00, 1.30355671e+00,
        1.30945355e+00, 1.31539628e+00, 1.32138584e+00,
        1.32742318e+00, 1.33350929e+00, 1.33964520e+00,
        1.34583197e+00, 1.35207068e+00, 1.35836247e+00,
        1.36470849e+00, 1.37110996e+00, 1.37756811e+00,
        1.38408423e+00, 1.39065965e+00, 1.39729576e+00,
        1.40399398e+00, 1.41075579e+00, 1.41758273e+00,
        1.42447638e+00, 1.43143840e+00, 1.43847050e+00,
        1.44557446e+00, 1.45275214e+00, 1.46000545e+00,
        1.46733639e+00, 1.47474705e+00, 1.48223960e+00,
        1.48981630e+00, 1.49747950e+00, 1.50523166e+00,
        1.51307535e+00, 1.52101325e+00, 1.52904816e+00,
        1.53718302e+00, 1.54542090e+00, 1.55376500e+00,
        1.56221872e+00, 1.57078557e+00, 1.57946928e+00,
        1.58827376e+00, 1.59720310e+00, 1.60626165e+00,
        1.61545395e+00, 1.62478482e+00, 1.63425933e+00,
        1.64388286e+00, 1.65366109e+00, 1.66360004e+00,
        1.67370609e+00, 1.68398603e+00, 1.69444707e+00,
        1.70509691e+00, 1.71594371e+00, 1.72699625e+00,
        1.73826387e+00, 1.74975661e+00, 1.76148522e+00,
        1.77346127e+00, 1.78569721e+00, 1.79820651e+00,
        1.81100369e+00, 1.82410452e+00, 1.83752612e+00,
        1.85128713e+00, 1.86540792e+00, 1.87991077e+00,
        1.89482015e+00, 1.91016304e+00, 1.92596923e+00,
        1.94227177e+00, 1.95910749e+00, 1.97651753e+00,
        1.99454814e+00, 2.01325151e+00, 2.03268687e+00,
        2.05292182e+00, 2.07403401e+00, 2.09611327e+00,
        2.11926431e+00, 2.14361026e+00, 2.16929730e+00,
        2.19650088e+00, 2.22543419e+00, 2.25635997e+00,
        2.28960736e+00, 2.32559662e+00, 2.36487675e+00,
        2.40818479e+00, 2.45654416e+00, 2.51143778e+00,
        2.57513696e+00, 2.65139379e+00, 2.74712487e+00,
        2.87753015e+00, 3.08963768e+00, 8.20953615e+00,
])
interpx = numpy.linspace(0, 1, len(interpy))

def get_invgauss_func(mu, sigma):
	return lambda x: mu + sigma * numpy.interp(x, interpx, interpy)
	
if __name__ == '__main__':
	import scipy.stats
	import matplotlib.pyplot as plt
	#x = numpy.linspace(1.5, 2.5, 400)
	q = numpy.linspace(0, 1, 400)
	a = scipy.stats.norm(1.95, 0.15).ppf(q)
	f = get_invgauss_func(1.95, 0.15)
	b = f(q)
	plt.plot(a, q, '-')
	plt.plot(b, q, '--')
	plt.show()
	


