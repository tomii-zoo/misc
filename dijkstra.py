INF = 999


names = ["S", "A", "B", "C", "G"]

dists = {
    "S": 0,
    "A": INF,
    "B": INF,
    "C": INF,
    "G": INF
}

edges = {
    "S" : {"A" : 1, "B" : 2, "C" : 3},
    "A" : {"G" : 9},
    "B" : {"G" : 6},
    "C" : {"G" : 7},
    "G" : {},
}

checked = {
    "S": False,
    "A": False,
    "B": False,
    "C": False,
    "G": False
}

while True:
    # 距離が最も近い未チェックのノードを選択する
    min_dist = INF
    for i in range(len(names)):
        d = dists[names[i]]
        if d < min_dist and not checked[names[i]]:
            cur_node = i
            min_dist = d

    print(f"調査対象のノード：{names[cur_node]}")
    print(f"{names[cur_node]}までの移動コスト：{min_dist}")
    checked[names[cur_node]] = True

    if names[cur_node] == "G":
        print("")
        print("*** ゴールに到達しました ***")
        print(f"各ノード最短距離:{dists}")
        break

    # 選択したノードの隣接ノードを取得
    for key in edges[names[cur_node]]:
        # 隣接ノードのコストを計算 
        new_dist = min_dist + edges[names[cur_node]][key]

        # 隣接ノードのコストが現在のコストよりも小さければ更新
        if new_dist < dists[key]:
            dists[key] = new_dist
            print(f"{key} までのコストを更新しました：{new_dist}")
    # break

