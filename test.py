def test(**kwargs):
    print(kwargs)


p = {"t1": "s1", "t1": "s1"}
test(t1=p)

if not False:
    print("t")

if True:
    print("t")


print(p.get("t1"))
print(p.get("t2"))
print(p.get("t2", "no_pa"))
