import math
import csv
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

# -------------------------------------------------
# Load Dataset from CSV
# -------------------------------------------------
data = []
with open("play_tennis_dataset.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        data.append(row)

attributes = ['Outlook','Temperature','Humidity','Wind']
target_index = -1

# -------------------------------------------------
# Entropy Function
# -------------------------------------------------
def entropy(dataset):
    labels = [row[target_index] for row in dataset]
    counts = Counter(labels)
    total = len(labels)

    ent = 0
    for c in counts.values():
        p = c / total
        ent -= p * math.log2(p)
    return ent

# -------------------------------------------------
# Print Subset in Tabular Format (like handwritten)
# -------------------------------------------------
def print_subset_table(subset, title, indent=""):
    print(f"\n{indent}{title}")
    print(f"{indent}" + "-" * 60)
    print(f"{indent}Day  Outlook    Temp     Humidity   Wind     Play")

    for i, row in enumerate(subset, start=1):
        print(
            f"{indent}{i:<4} "
            f"{row[0]:<10} "
            f"{row[1]:<8} "
            f"{row[2]:<10} "
            f"{row[3]:<8} "
            f"{row[4]}"
        )

    print(f"{indent}" + "-" * 60)

# -------------------------------------------------
# Information Gain (with subset printing)
# -------------------------------------------------
def information_gain(dataset, attr_index, attr_name, indent=""):
    base_entropy = entropy(dataset)
    subsets = defaultdict(list)

    for row in dataset:
        subsets[row[attr_index]].append(row)

    # PRINT SUBSETS IN REQUIRED FORMAT
    for value, subset in subsets.items():
        print_subset_table(
            subset,
            f"Subset for {attr_name} = {value}",
            indent
        )
        print(f"{indent}Entropy = {round(entropy(subset), 3)}")

    weighted_entropy = 0
    for subset in subsets.values():
        weighted_entropy += (len(subset)/len(dataset)) * entropy(subset)

    return base_entropy, weighted_entropy, base_entropy - weighted_entropy, subsets

# -------------------------------------------------
# ID3 Algorithm with Full Trace + Subsets
# -------------------------------------------------
def id3(dataset, attrs, level=0):
    indent = "│   " * level
    labels = [row[target_index] for row in dataset]

    print(f"\n{indent}DATASET (size={len(dataset)})")
    print(f"{indent}Yes = {labels.count('Yes')}, No = {labels.count('No')}")
    print(f"{indent}Entropy = {round(entropy(dataset), 3)}")

    if len(set(labels)) == 1:
        print(f"{indent}→ Leaf Node: {labels[0]}")
        return labels[0]

    if not attrs:
        majority = Counter(labels).most_common(1)[0][0]
        print(f"{indent}→ Leaf Node (majority): {majority}")
        return majority

    print(f"\n{indent}Evaluating Features:")

    gains = []
    split_info = {}

    for attr in attrs:
        idx = attributes.index(attr)
        e, we, ig, subsets = information_gain(dataset, idx, attr, indent)
        gains.append((ig, attr))
        split_info[attr] = subsets

        print(f"{indent}- {attr}")
        print(f"{indent}  Weighted Entropy = {round(we,3)}")
        print(f"{indent}  Information Gain = {round(ig,3)}")

    best_attr = max(gains)[1]
    print(f"\n{indent}BEST SPLIT → {best_attr}")

    tree = {best_attr: {}}

    for value, subset in split_info[best_attr].items():
        print(f"\n{indent}{best_attr} = {value}")
        remaining_attrs = attrs[:]
        remaining_attrs.remove(best_attr)
        tree[best_attr][value] = id3(subset, remaining_attrs, level+1)

    return tree

# -------------------------------------------------
# Draw Decision Tree using Matplotlib
# -------------------------------------------------
def draw_tree_matplotlib(tree):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')

    def draw_node(text, x, y, color):
        ax.text(x, y, text, ha='center', va='center',
                bbox=dict(boxstyle='round', fc=color))

    def draw_edge(x1, y1, x2, y2, label=""):
        ax.plot([x1, x2], [y1, y2], 'k-')
        if label:
            ax.text((x1+x2)/2, (y1+y2)/2, label, ha='center')

    def recurse(tree, x, y, dx):
        if isinstance(tree, dict):
            root = list(tree.keys())[0]
            draw_node(root, x, y, 'lightblue')

            children = tree[root]
            n = len(children)
            start_x = x - dx * (n - 1) / 2

            for i, (value, subtree) in enumerate(children.items()):
                child_x = start_x + i * dx
                child_y = y - 0.15
                draw_edge(x, y - 0.03, child_x, child_y + 0.03, value)
                recurse(subtree, child_x, child_y, dx / 1.5)
        else:
            draw_node(tree, x, y, 'lightgreen')

    recurse(tree, 0.5, 0.9, 0.3)
    plt.savefig("id3_tree.png", dpi=300, bbox_inches='tight')
    plt.show()

# -------------------------------------------------
# Run ID3
# -------------------------------------------------
print("\n========== ID3 DECISION TREE CONSTRUCTION ==========")
decision_tree = id3(data, attributes)

print("\nGenerating Decision Tree Image using Matplotlib...")
draw_tree_matplotlib(decision_tree)
