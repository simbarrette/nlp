from syntax_aware_generate import generate

# inserts matching syntax subtrees from trump.txt into
# trees from austen-emma.txt
generate('text.txt', word_limit=10)