bac = 1000
ev = 100
pv = 100
ac = 120

sv = ev - pv
cv = ev - ac
spi = ev / pv
cpi = ev / ac

etc = (bac - ev) / cpi
eac = ac + etc
vac = bac - eac

print("-----------------")
print(f"BAC => {bac}")
print(f"EV => {ev}")
print(f"PV => {pv}")
print(f"AC => {ac}")
print("-----------------")
print(f"SV => {sv}")
print(f"CV => {cv}")
print(f"SPI => {spi:.2}")
print(f"CPI => {cpi:.2}")
print(f"ETC => {etc}")
print(f"EAC => {eac}")
print(f"VAC => {vac}")
