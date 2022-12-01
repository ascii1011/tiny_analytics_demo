
"""


from data_structures import DNA




_pair_score_2_dijkstra_edge_map
edges = convert.dna_pair_score_2_dijkstra_edge_map(dna_pair_score)

define_types = []


dna_pair_similarity_scores__tmpl = f"({dna1}, {dna2}, {score})"

def pair_score_define(label1, label2, score):
    return (label1, label2, score)

def pair_score_extract(values=('lvalue1', 'lvalue2', 'score'), labels=['label1', 'label2', 'score']):
    res = {}
    if len(values) != 3 or labels[0] == labels[1]:
        return res
    
    for i in range(3):
        res.update({labels[i]: values[i]})

    return res

from convert import dna_pair_score_2_dijkstra_edge_map
edges = convert.dna_pair_score_2_dijkstra_edge_map(dna_pair_score)

class Convert:

    def dna_pair_score(self, pair_score)


def get_dna_pair_compute_similarity_scores(combos, dna_map, debug=False):
    if debug: print(f"\nget_dna_pair_compute_similarity_scores():")
    scores = {}
    for dna1, dna2 in combos:
        score_key = f"{dna1}___{dna2}"
        #print(f"key({type(score_key)}): {score_key}")

        score_value = compute_similarity(dna_map[dna1], dna_map[dna2])
        #print(f"key({type(score_value)}): {score_value}")

        scores.update({score_key: score_value})

        if debug: print(f">> {dna1} vs {dna2} == {score_value}")

    if debug: print(f"\tEND<< scores: {scores}")
    return scores

"""
pass