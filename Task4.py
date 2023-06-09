import math

graph = {
    'Algeria': {'Libya': 989, 'Mali': 1359, 'Mauritania': 463, 'Morocco': 1559, 'Niger': 956, 'Tunisia': 622, 'Western Sahara': 240},
    'Angola': {'Namibia': 1370, 'Zambia': 1112},
    'Benin': {'Burkina Faso': 1267, 'Niger': 1207, 'Nigeria': 676, 'Togo': 205},
    'Botswana': {'Namibia': 824, 'South Africa': 1526, 'Zambia': 977, 'Zimbabwe': 834},
    'Burkina Faso': {'Cote d\'Ivoire': 1005, 'Ghana': 962, 'Mali': 965, 'Niger': 472, 'Togo': 663},
    'Burundi': {'Rwanda': 213},
    'Cabo Verde': {'Senegal': 1256},
    'Cameroon': {'Central African Republic': 1301, 'Chad': 1102, 'Congo': 1142, 'Equatorial Guinea': 684, 'Gabon': 1104, 'Nigeria': 1594},
    'Central African Republic': {'Chad': 1176, 'Congo': 1743, 'South Sudan': 1163, 'Sudan': 1501},
    'Chad': {'Libya': 1400, 'Niger': 1165, 'Nigeria': 1485, 'Sudan': 969},
    'Comoros': {'Madagascar': 875},
    'Congo': {'Gabon': 1079, 'Democratic Republic of the Congo': 1298},
    'Democratic Republic of the Congo': {'Uganda': 765, 'Rwanda': 223, 'Tanzania': 1453, 'Zambia': 2163},
    'Djibouti': {'Eritrea': 126},
    'Egypt': {'Libya': 1115, 'Sudan': 1276},
    'Equatorial Guinea': {'Gabon': 234, 'Cameroon': 684},
    'Eritrea': {'Ethiopia': 982, 'Sudan': 682},
    'Eswatini': {'Mozambique': 1055, 'South Africa': 441},
    'Ethiopia': {'Djibouti': 982, 'Kenya': 867, 'Somalia': 1655, 'South Sudan': 1299, 'Sudan': 1071},
    'Gabon': {'Cameroon': 1104, 'Congo': 1079, 'Equatorial Guinea': 234},
    'Gambia': {'Senegal': 740},
    'Ghana': {'Ivory Coast': 1371, 'Burkina Faso': 962, 'Togo': 546},
    'Guinea': {'Ivory Coast': 1087, 'Liberia': 847, 'Mali': 1013, 'Senegal': 673, 'Sierra Leone': 1172},
    'Guinea-Bissau': {'Senegal': 449, 'Guinea': 386},
    'Kenya': {'Ethiopia': 867, 'Somalia': 682, 'South Sudan': 232, 'Tanzania': 1015, 'Uganda': 812},
    'Lesotho': {'South Africa': 160},
    'Liberia': {'Cote d\'Ivoire': 814, 'Guinea': 847, 'Sierra Leone': 446},
    'Libya': {'Sudan': 1636, 'Tunisia': 1092},
    'Madagascar': {'Mozambique': 595},
    'Malawi': {'Mozambique': 734, 'Tanzania': 475, 'Zambia': 837},
    'Mali': {'Algeria': 1359, 'Burkina Faso': 965, 'Cote d\'Ivoire': 1113, 'Guinea': 1013, 'Mauritania': 1241, 'Niger': 838, 'Senegal': 703},
    'Mauritania': {'Mali': 1241, 'Morocco': 1657, 'Senegal': 661, 'Western Sahara': 469},
    'Mauritius': {},
    'Morocco': {'Algeria': 1559, 'Mauritania': 1657},
    'Mozambique': {'Malawi': 734, 'South Africa': 491, 'Swaziland': 1055, 'Tanzania': 1512, 'Zambia': 1377, 'Zimbabwe': 1230},
    'Namibia': {'Angola': 1370, 'Botswana': 824, 'South Africa': 1447, 'Zambia': 2106},
    'Niger': {'Algeria': 956, 'Benin': 1207, 'Chad': 1165, 'Libya': 1415, 'Mali': 838, 'Nigeria': 1367},
    'Nigeria': {'Benin': 676, 'Cameroon': 1594, 'Chad': 1485, 'Niger': 1367},
    'Rwanda': {'Burundi': 213, 'Democratic Republic of the Congo': 223, 'Tanzania': 217},
    'Sao Tome and Principe': {},
    'Senegal': {'Gambia': 740, 'Guinea': 673, 'Guinea-Bissau': 449, 'Mauritania': 661, 'Mali': 703},
    'Seychelles': {},
    'Sierra Leone': {'Guinea': 1172, 'Liberia': 446},
    'Somalia': {'Djibouti': 180, 'Ethiopia': 1655, 'Kenya': 682},
    'South Africa': {'Botswana': 1526, 'Eswatini': 441, 'Lesotho': 160, 'Namibia': 1447, 'Mozambique': 491, 'Zimbabwe': 225},
    'South Sudan': {'Central African Republic': 1163, 'Democratic Republic of the Congo': 628},
    'Sudan': {'Central African Republic': 1589, 'Chad': 1373, 'Egypt': 1276, 'Eritrea': 605, 'Ethiopia': 1293, 'Libya': 1636, 'South Sudan': 1174},
    'Tanzania': {'Burundi': 451, 'Kenya': 1015, 'Malawi': 475, 'Mozambique': 1512, 'Rwanda': 217, 'Uganda': 858, 'Zambia': 338, 'Democratic Republic of the Congo': 1979},
    'Togo': {'Benin': 126, 'Burkina Faso': 638, 'Ghana': 877},
    'Tunisia': {'Algeria': 965, 'Libya': 1092},
    'Uganda': {'Democratic Republic of the Congo': 777, 'Kenya': 812, 'Rwanda': 362, 'South Sudan': 452, 'Tanzania': 858},
    'Zambia': {'Angola': 1065, 'Malawi': 734, 'Mozambique': 1377, 'Namibia': 2106, 'Tanzania': 338, 'Zimbabwe': 389},
    'Zimbabwe': {'Botswana': 866, 'Mozambique': 1230, 'South Africa': 225, 'Zambia': 389}
}
nodes = ('Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon',
         'Central African Republic', 'Chad', 'Comoros', 'Congo', 'Democratic Republic of the Congo',
         'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea',
         'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius',
         'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles',
         'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia',
         'Uganda', 'Zambia', 'Zimbabwe')




def arg_min(T, S):
    amin = -1
    m = max(T)  # максимальное значение
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i

    return amin

def get_link_v(v, D):
    for i, weight in enumerate(D[v]):
        if weight > 0:
            yield i



D=((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 989, 0, 0, 1359, 463, 0, 1559, 0, 0, 956, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 622, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1370, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1112, 0),
   (0, 0, 0, 0, 1267, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1207, 676, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 824, 0, 0, 0, 0, 0, 0, 0, 0, 1526, 0, 0, 0, 0, 0, 0, 977, 834),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 962, 0, 0, 0, 0, 0, 0, 0, 0, 965, 0, 0, 0, 0, 0, 472, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 663, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 213, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1256, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 1301, 1102, 0, 1142, 0, 0, 0, 684, 0, 0, 0, 1104, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1594, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 1176, 0, 1743, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1163, 1501, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1400, 0, 0, 0, 0, 0, 0, 0, 0, 1165, 1485, 0, 0, 0, 0, 0, 0, 0, 0, 969, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 875, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1298, 0, 0, 0, 0, 0, 0, 1079, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 223, 0, 0, 0, 0, 0, 0, 0, 0, 1453, 0, 0, 765, 2163, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 126, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1276, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 684, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 234, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 982, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 682, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1055, 0, 0, 0, 0, 0, 0, 0, 0, 0, 441, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 982, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 867, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1655, 0, 1299, 1071, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 1104, 0, 0, 0, 1079, 0, 0, 0, 234, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 740, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 962, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 546, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 847, 0, 0, 0, 1013, 0, 0, 0, 0, 0, 0, 0, 0, 0, 673, 0, 1172, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 386, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 449, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 867,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 682, 0, 232, 0, 1015, 0, 0, 812, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 847, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 446, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1636, 0, 0, 1092, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 595, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 734, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 475, 0, 0, 0, 837, 0),
   (1359, 0, 0, 0, 965, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1013, 0, 0, 0, 0, 0, 0, 0, 0, 1241, 0, 0, 0, 0, 838, 0, 0, 0, 703, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1241, 0, 0, 1657, 0, 0, 0, 0, 0, 0, 661, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (1559, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1657, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 734, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 491, 0, 0, 1512, 0, 0, 0, 1377, 1230),
   (0, 1370, 0, 824, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1447, 0, 0, 0, 0, 0, 0, 2106, 0),
   (956, 0, 1207, 0, 0, 0, 0, 0, 0, 1165, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1415, 0, 0, 838, 0, 0, 0, 0, 0, 0, 1367, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 676, 0, 0, 0, 0, 1594, 0, 1485, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1367, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 213, 0, 0, 0, 0, 0, 0, 223, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 217, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 740, 0, 673, 449, 0, 0, 0, 0, 0, 0, 703, 661, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1172, 0, 0, 0, 446, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180, 0, 0, 0, 0, 1655, 0, 0, 0, 0, 0, 682, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 1526, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 441, 0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 0, 0, 0, 0, 0, 0, 491, 1447, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 225),
   (0, 0, 0, 0, 0, 0, 0, 0, 1163, 0, 0, 0, 628, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 1589, 1373, 0, 0, 0, 0, 1276, 0, 605, 0, 1293, 0, 0, 0, 0, 0, 0, 0, 0, 1636, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1174, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 451, 0, 0, 0, 0, 0, 0, 1979, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1015, 0, 0, 0, 0, 475, 0, 0, 0, 0, 1512, 0, 0, 0, 217, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 858, 338, 0),
   (0, 0, 126, 0, 638, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 877, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (965, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1092, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 777, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 812, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 362, 0, 0, 0, 0, 0, 0, 452, 0, 858, 0, 0, 0, 0, 0),
   (0, 1065, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 734, 0, 0, 0, 0, 1377, 2106, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 338, 0, 0, 0, 0, 389),
   (0, 0, 0, 866, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1230, 0, 0, 0, 0, 0, 0, 0, 0, 0, 225, 0, 0, 0, 0, 0, 0, 389, 0))
N = len(D)  # число вершин в графе
T = [math.inf]*N   # последняя строка таблицы

v = 0       # стартовая вершина (нумерация с нуля)
S = {v}     # просмотренные вершины
T[v] = 0    # нулевой вес для стартовой вершины
#M = [0]*N   # оптимальные связи между вершинами

while v != -1:          # цикл, пока не просмотрим все вершины
    for j in get_link_v(v, D):   # перебираем все связанные вершины с вершиной v
        if j not in S:           # если вершина еще не просмотрена
            w = T[v] + D[v][j]
            if w < T[j]:
                T[j] = w

    v = arg_min(T, S)            # выбираем следующий узел с наименьшим весом
    if v > 0:                    # выбрана очередная вершина
        S.add(v)                 # добавляем новую вершину в рассмотрение

print(T)

