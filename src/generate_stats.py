from scipy import stats 
<<<<<<< HEAD
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
=======

def generate_stats(gene_exp_data, bed_file, bim_file, subset):
    slope_list = []
    r_list = []
    p_list = []
    se_list = []
    dists = abs(59783540 - bim_file['POS'])
    cis_dists_idx = dists[dists <= 500000].index
    for index in cis_dists_idx:
        my_val = new_ind[np.s_[::,index]]
        id_val = subset['sample_ids']       
        df = pd.DataFrame(data = {'sample_id': id_val, 'snp': my_val.flatten()})
        my_gene_exp = gene_exp_data
        my_gene_exp.columns = ['sample_id', 'value']
        merged = pd.merge(df, my_gene_exp, on = 'sample_id')
        merged = merged.dropna()
        slope, intercept, r, p, se = stats.linregress((merged['snp'].astype(np.float), merged['value'].astype(np.float)))
        slope_list.append(slope)
        r_list.append(r)
        p_list.append(p)
        se_list.append(se)

    return pd.DataFrame({'slope':slope_list, 'corr':r_list, 'p_val':p_list, 'standard_error': se_list}) 
>>>>>>> dd86d5c7a27bbc1eeaa6c3a7e5d91bd155aa49ad
