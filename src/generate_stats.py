from scipy import stats 
import numpy as np
import pandas as pd

def generate_stats(gene_list, sample_ids, exp_pop, val2, bim_file, desired_pop):
    print("Generating Stats")
    my_output = []
    for i in gene_list:

        exp_pop.loc[exp_pop['Gene_Symbol'] == i][['sample_id', 'Value', 'group']]
        gene_coord = exp_pop.loc[exp_pop['Gene_Symbol'] == i]['Coord'].iloc[0]
        dists = abs(int(gene_coord) - bim_file['POS'])
        cis_dists_idx = dists[dists <= 500000].index
        for idx in cis_dists_idx:
        
            my_mini_output = []
            my_mini_output.append(i)
            my_mini_output.append(idx)
            my_val = val2[np.s_[::, idx]]
            snp_df = pd.DataFrame({'sample_id': sample_ids, 'snp': my_val})
            merged = exp_pop.merge(snp_df, on = 'sample_id')
            merged = merged[merged['group'] == desired_pop]
            merged = merged.dropna()
            slope, intercept, r, p, se = stats.linregress((merged['snp'].astype(np.float), merged['Value'].astype(np.float)))
            my_mini_output.append(p)
            my_mini_output.append(slope)
            my_output.append(my_mini_output)
        
    return pd.DataFrame(my_output, columns = ['gene', 'snp_idx', 'p', 'slope'])
