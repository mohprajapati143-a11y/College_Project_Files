def kruskal_algorithm():
    vertices = [0,1,2,3,4,5,6,7,8]
    edges = [
        (0, 1, 4), (0, 7 ,8), (1, 2, 8), (1, 7, 11),
        (2, 3, 7), (2, 5, 4), (2, 8, 2), (3, 4, 9),
        (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1),
        (6, 8, 6), (7, 8, 7),
    ]

    print("STEP 1: Sort all edges by weight")
    print("="*50)
    edges.sort(key=lambda x: x[2])
    for i, edge in enumerate(edges,1):
        print(f"{i}. Edge {edge[0]}-{edge[1]} = {edge[2]}")

    # Step 2: Initialize parent dictionary
    parent = {v: v for v in vertices}
    print("\nSTEP 2: Start with empty MST")
    print("="*50)
    print(f"Parent: {parent}")
    print("Each vertex is in its own group\n")

    # Function to find parent
    def find_parent(vertex):
        if parent[vertex] == vertex:
            return vertex
        else:
            return find_parent(parent[vertex])

    # Step 3: Process edges
    mst = []
    total_cost = 0
    step = 1

    print("STEP 3: Process each edge (smaller first)")
    print("="*50)

    for edge in edges:
        v1, v2, weight = edge
        parent1 = find_parent(v1)
        parent2 = find_parent(v2)

        print(f"\n--- Step {step} ---")
        print(f"Checking edge: {v1}-{v2} (weight = {weight})")
        print(f"Group of {v1}: {parent1}")
        print(f"Group of {v2}: {parent2}")

        if parent1 != parent2:
            print(f"Different Group! ADD this edge")
            mst.append(edge)
            total_cost += weight
            parent[parent1] = parent2
            print(f"Merge: Group {parent1} -> Group {parent2}")
        else:
            print(f"Same group! SKIP (creates cycle)")

        step += 1

    print("\n" + "="*50)
    print("FINAL MINIMUM SPANNING TREE")
    print("="*50)
    for edge in mst:
        print(f"Edge {edge[0]}-{edge[1]} = {edge[2]}")
    print(f"\nTotal Cost: {total_cost}")

    return mst, total_cost


# Run the algorithm
kruskal_algorithm()
