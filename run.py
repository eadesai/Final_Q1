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
        gene_list, sample_ids, exp_pop, val2, bim_file, desired_pop = get_data(**data_cfg)

    if 'stats' in targets:
        #with open('config/stats-params.json') as fh:
            #feats_cfg = json.load(fh)

        my_stats = generate_stats(gene_list, sample_ids, exp_pop, val2, bim_file, desired_pop)
    if 'test' in targets:
        
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)

        # make the data target
        
        gene_list, sample_ids, exp_pop, val2, bim_file, desired_pop = get_data(**data_cfg)
        my_stats = generate_stats(gene_list, sample_ids, exp_pop, val2, bim_file, desired_pop)
        my_stats.to_csv("results.csv")

    return my_stats

if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)
