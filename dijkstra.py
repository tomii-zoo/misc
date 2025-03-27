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

print("--- BEGIN ---")

while True:
    # 最も距離が近いノードを選択する
    min_dist = INF
    for i in range(len(names)):
        d = dists[names[i]]
        if d < min_dist and not checked[names[i]]:
            cur_node = i
            min_dist = d

    checked[names[cur_node]] = True
    print(f"checked[{names[cur_node]}] = True")
    print(f"mindist = {min_dist}")

    if names[cur_node] == "G":
        print("--- GOAL ---")
        print(f"各ノード最短距離:{dists}")
        print("")
        break

    # 選択したノードの隣接ノードを取得
    for key in edges[names[cur_node]]:
        # 隣接ノードのコストを計算
        new_dist = min_dist + edges[names[cur_node]][key]

        # 隣接ノードのコストが現在のコストよりも小さければ更新
        if new_dist < dists[key]:
            dists[key] = new_dist
            print(f"total_dist[{key}] = {new_dist}")
    
    print("***")

