INF = 999

loop = 0

names = ["S", "A", "B", "C", "G"]

dists = {
    "S": 0,
    "A": INF,
    "B": INF,
    "C": INF,
    "G": INF
}

edges = {
    "S" : {"A" : 1, "B" : 2, "C" : 8},
    "A" : {"B" : 7, "C" : 4, "G" : 9},
    "B" : {"G" : 6},
    "C" : {"G" : 3},
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
            min_dist = d    # 距離が出ているノードの中で最小のものを選択

    checked[names[cur_node]] = True
    print(f"【{names[cur_node]}】")
    print(f"min_dist = {min_dist}")

    # ゴールノードに到達したら終了
    if names[cur_node] == "G":
        print("--- GOAL ---")
        print(f"各ノード最短距離:{dists}")
        print("")
        break

    # 選択したノードの隣接ノードを取得
    for dest in edges[names[cur_node]]:
        # 隣接ノードのコストを計算 
        # = 選択したノードの最短コスト + 選択したノードから隣接ノードの辺のコスト
        new_dist = min_dist + edges[names[cur_node]][dest]

        # 隣接ノードのコストが現在のコストよりも小さければ更新
        if new_dist < dists[dest]:
            dists[dest] = new_dist
            print(f"dist[{dest}] = {new_dist}")
    
    print("***")

