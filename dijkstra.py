INF = 999


names = ["S", "A", "B", "G"]

dists = {
    "S": 0,
    "A": INF,
    "B": INF,
    "G": INF
}

edges = {
    "S" : {"A" : 1, "B" : 2},
    "A" : {"B" : 1, "G" : 5},
    "B" : {"G" : 3},
    "G" : {},
}

checked = {
    "S": False,
    "A": False,
    "B": False,
    "G": False
}

while True:
    # 最も距離が近いノードを選択する
    min_dist = INF
    for i in range(len(names)):
        d = dists[names[i]]
        if d < min_dist and not checked[names[i]]:
            cur_node = i
            min_dist = d

    print(f"計算対象のノード：{names[cur_node]}")
    print(f"コスト：{min_dist}")
    checked[names[cur_node]] = True

    if names[cur_node] == "G":
        print("*** ゴールに到達しました ***")
        print(dists)
        break

    # 選択したノードの隣接ノードを取得
    for key in edges[names[cur_node]]:
        # 隣接ノードのコストを計算
        new_dist = min_dist + edges[names[cur_node]][key]

        # 隣接ノードのコストが現在のコストよりも小さければ更新
        if new_dist < dists[key]:
            dists[key] = new_dist
            print(f"更新：{key} {new_dist}")
    # break

