ana = {
    "nome-comp": "ana camila santos",
    "idade": 26,
    "local-nasc": "campina grande-pb",
    "profissao": "front-end developer",
    "sobrinhos": ["anahuac", "felipe", "clara"]
}

print(type(ana))
print(ana["idade"])
print(ana["profissao"])
print(len(ana))
del ana["idade"]
print(ana)
ana["profissao"] = "front-end developer jr"
print(ana)

# for x in ana:
#     print(x)

# for x in ana:
#     print(x +": "+ ana[x])

print(ana.get("idade", "não existe essa info no cadastro"))

print(ana["sobrinhos"])
ana["sobrinhos"].append("laura")
print(ana["sobrinhos"])

ana.clear()

print(ana)



