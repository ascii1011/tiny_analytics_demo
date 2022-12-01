

from analysis.dna.caltech_edu.basic import get_dna_pair_compute_similarity_scores, get_dna_map_combination_pairs, map_dna_files
#list_filenames() >> dna_map() >> dna_combo_pairs() >> scores() >> dijkstra_eval()

class DNA:

    def __init__(self):
        self.scores = {}

    def update_score(self, seq1, seq2, score):
        self.scores.update({
            "seq1": seq1,
            "seq2": seq2,
            "score": score,
        })

    def dna_map_from_files(self, filenames):
        return map_dna_files(filenames)

    def dna_combo_pairs(self, dna_map):
        return get_dna_map_combination_pairs(dna_map)

    def scores(self, dna_combo_pairs, dna_map):  
        return get_dna_pair_compute_similarity_scores(dna_combo_pairs, dna_map)


