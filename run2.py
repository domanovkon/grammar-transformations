gr_file = open('g3.txt')
gr = {}
for line in gr_file:
    line = line.strip()
    if not line:
        continue
    l_product, r_product = line.split('=')
    l_product = l_product.strip()
    r_product = r_product.strip()
    r_product = tuple(r_product.split())
    if l_product in gr:
        gr[l_product].add(r_product)
    else:
        gr[l_product] = {r_product}

print("Исходная грамматика")
for l_product in sorted(gr):
    for r_product in sorted(gr[l_product]):
        print(l_product, '=', *r_product)

parent_non_terminal = {()}
non_terminal = sorted(gr)
for NT in non_terminal:
    for r_product in gr[NT].copy():
        if not any(nt in non_terminal for nt in r_product):
            parent_non_terminal.add(NT)

parent_non_terminal.remove(())

while True:
    start_len_parent = len(parent_non_terminal)
    for NT in non_terminal:
        for r_product in gr[NT].copy():
            cnt = 0
            t_cnt = 0
            for alpha in r_product:
                if non_terminal.__contains__(alpha):
                    if parent_non_terminal.__contains__(alpha):
                        cnt = 1
                    else:
                        cnt = 0
                        break
            if cnt == 1:
                parent_non_terminal.add(NT)
    if start_len_parent == len(parent_non_terminal):
        break

for l_product in sorted(gr):
    if not (parent_non_terminal.__contains__(l_product)):
        gr.pop(l_product)

for l_product in sorted(gr):
    for r_product in gr[l_product].copy():
        for alpha in r_product:
            if non_terminal.__contains__(alpha):
                if not parent_non_terminal.__contains__(alpha):
                    gr[l_product].remove(r_product)

    # if not (parent_non_terminal.__contains__(r_product)):
    #     gr.pop()

print("Удалим правила, содержащие непорождающие нетерминалы")
for l_product in sorted(gr):
    for r_product in sorted(gr[l_product]):
        print(l_product, '=', *r_product)
