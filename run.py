
import sys
import os
import json

sys.path.insert(0, 'src')

from etl import get_data
from generate_stats import generate_stats

def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''

    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)

        # make the data target
<<<<<<< HEAD
        gene_list, sample_ids, exp_pop, val2, bim_file, desired_pop = get_data(**data_cfg)
=======
        gene_exp_data, bed_file, bim_file = get_data(**data_cfg)
>>>>>>> dd86d5c7a27bbc1eeaa6c3a7e5d91bd155aa49ad

    if 'stats' in targets:
        #with open('config/stats-params.json') as fh:
            #feats_cfg = json.load(fh)

<<<<<<< HEAD
        my_stats = generate_stats(gene_list, sample_ids, exp_pop, val2, bim_file, desired_pop)
=======
        my_stats = generate_stats(gene_exp_data, bed_file, bim_file)
>>>>>>> dd86d5c7a27bbc1eeaa6c3a7e5d91bd155aa49ad
    if 'test' in targets:
        
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)

        # make the data target
<<<<<<< HEAD
        
        gene_list, sample_ids, exp_pop, val2, bim_file, desired_pop = get_data(**data_cfg)
        my_stats = generate_stats(gene_list, sample_ids, exp_pop, val2, bim_file, desired_pop)
        my_stats.to_csv("results.csv")
=======
        gene_exp_data, bed_file, bim_file = get_data(**data_cfg)
        my_stats = generate_stats(gene_exp_data, bed_file, bim_file)

>>>>>>> dd86d5c7a27bbc1eeaa6c3a7e5d91bd155aa49ad

    return my_stats

if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)
