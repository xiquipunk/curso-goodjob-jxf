letra_C = [
    "  ##### ",
    " ##     ",
    "##      ",
    "##      ",
    "##      ",
    " ##     ",
    "  ##### "
]

letra_I = [
    " ##### ",
    "   ##  ",
    "   ##  ",
    "   ##  ",
    "   ##  ",
    "   ##  ",
    " ##### "
]

letra_B = [
    "####   ",
    "## ##  ",
    "##  ## ",
    "####   ",
    "##  ## ",
    "## ##  ",
    "####   "
]

letra_E = [
    "##### ",
    "##    ",
    "##    ",
    "##### ",
    "##    ",
    "##    ",
    "##### "
]

letra_R = [
    "####   ",
    "## ##  ",
    "##  ## ",
    "####   ",
    "## ##  ",
    "##  ## ",
    "##  ###"
]

letra_P = [
    "##### ",
    "##  ##",
    "##  ##",
    "##### ",
    "##    ",
    "##    ",
    "##    "
]

letra_U = [
    "##  ##",
    "##  ##",
    "##  ##",
    "##  ##",
    "##  ##",
    "##  ##",
    " #### "
]

letra_N = [
    "##   ##",
    "###  ##",
    "#### ##",
    "## ####",
    "##  ###",
    "##   ##",
    "##   ##"
]

letra_K = [
    "##  ##",
    "## ## ",
    "###   ",
    "###   ",
    "## ## ",
    "##  ##",
    "##  ##"
]

for trazo_C, trazo_I, trazo_B, trazo_E, trazo_R, trazo_P, trazo_U, trazo_N, trazo_K in zip(letra_C, letra_I, letra_B, letra_E, letra_R, letra_P, letra_U, letra_N, letra_K):
    print(trazo_C + "  " + trazo_I + "  " + trazo_B + "  " + trazo_E + "  " + trazo_R + "  " + trazo_P + "  " + trazo_U + "  " + trazo_N + "  " + trazo_K)
