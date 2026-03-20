# 1. sum_nested_list
def sum_nested_list(root):
    total = 0
    for item in root:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += sum_nested_list(item)  # recursive call
    return total


# ტესტები
root1 = [1, 2, [3, 4]]
print(sum_nested_list(root1))  # 10

root2 = [5, [6, 7], [[8, 9], 10]]
print(sum_nested_list(root2))  # 45


# 2. count_nested_levels
def count_nested_levels(nested_documents, target_document_id, current_level=0):
    for doc_id, children in nested_documents.items():
        if doc_id == target_document_id:
            return current_level
        # recursive search in children
        result = count_nested_levels(children, target_document_id, current_level + 1)
        if result != -1:
            return result
    return -1


# ტესტები
docs = {
    1: {
        3: {}
    },
    2: {}
}

print(count_nested_levels(docs, 3))  # 2
print(count_nested_levels(docs, 2))  # 1
print(count_nested_levels(docs, 99)) # -1
