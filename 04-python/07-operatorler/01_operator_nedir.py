# 7.1 Operator Nedir?
# Operatorler, degiskenler ve degerler uzerinde islem yapmamizi saglayan sembollerdir.
# Ornek: 5 + 3 ifadesinde 5 ve 3 "operand", + ise "operator"dur.

a = 10
b = 3

# Aritmetik operatorler: + - * / // % **
print("Aritmetik:", a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

# Atama operatorleri: = += -= *= /= //= %= **=
c = a
c += 5
print("Atama:", c)

# Karsilastirma operatorleri: == != > < >= <=
print("Karsilastirma:", a == b, a != b, a > b, a < b, a >= b, a <= b)

# Mantiksal operatorler: and or not
print("Mantiksal:", a > 5 and b > 5, a > 5 or b > 5, not a > 5)

# Kimlik operatorleri: is, is not
liste1 = [1, 2]
liste2 = liste1
print("Kimlik:", liste1 is liste2, liste1 is not liste2)

# Uyelik operatorleri: in, not in
print("Uyelik:", 2 in liste1, 5 not in liste1)

# Bit operatorleri: & | ^ ~ << >>
print("Bit:", a & b, a | b, a ^ b, ~a, a << 1, a >> 1)

# Operatorler farkli veri tiplerinde farkli davranabilir
print("Sayilarda +:", 2 + 3)
print("Stringlerde +:", "2" + "3")
print("Listelerde +:", [1] + [2])
print("Stringlerde *:", "ab" * 3)
print("Listelerde *:", [0] * 3)

# Operator onceligi: () > ** > * / // % > + - > karsilastirma > not > and > or
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 ** 2)            # us alma sagdan sola: 2 ** 9
print(10 > 5 and 3 > 4 or True)
