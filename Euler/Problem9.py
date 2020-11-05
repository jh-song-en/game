a = "onetwothreefourfivesixseveneightnine"
b = "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen"
c = "twentythirtyfortyfiftysixtyseventyeightyninety"
d = "hundred"
e = "and"
f = "onethousand"

lenb = len(b)
lena = len(a)
lenc = len(c)
lend = len(d)
lene = len(e)
lenf = len(f)

one_to_99 = lena + lenb + 8 * lena + lenc * 10
hundred_to_999 = 100 * (lena + (lend * 9)) + 891 * lene + 9 * one_to_99
one_to_999 = one_to_99 + hundred_to_999
print(one_to_999 + lenf)
print(lena)