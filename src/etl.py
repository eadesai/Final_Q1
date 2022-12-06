import os
import pandas as pd
from bed_reader import open_bed, sample_file
<<<<<<< HEAD
import numpy as np


def get_data(gene_exp_fp, pop_file, plink_bed, plink_bim, plink_fam, desired_pop):
    print("Getting Data")
=======

# def store_data(genotype_in, gene_exp_in, genotype_out, gene_exp_out):
#     '''
#     Reads the data by creating a symlink between the 
#     location of the downloaded data and /data
#     '''
#     # first create the data directory
#     directory = "data"
#     parent_dir = "./"
#     path = os.path.join(parent_dir, directory)

#     os.mkdir(path)

#     # create a convenient hierarchical structure of folders inside /data
#     directory1 = "genotype"
#     directory2 = "gene_expression"
#     parent_dir = "./data/"
    
#     os.mkdir(os.path.join(parent_dir, directory1))
#     os.mkdir(os.path.join(parent_dir, directory2))

    
#     # create the symlink
#     os.symlink(genotype_in, genotype_out)
#     os.symlink(gene_exp_in, gene_exp_out)
    
        
#     return 

def get_data(gene_exp_fp, pop_file, plink_bed, plink_bim, plink_fam, desired_pop):
>>>>>>> dd86d5c7a27bbc1eeaa6c3a7e5d91bd155aa49ad
    '''
    Reads the data by creating a symlink between the 
    location of the downloaded data and /data
    '''
<<<<<<< HEAD
    gene_exp_data = pd.read_csv(gene_exp_fp, index_col = 0)
    gene_exp_data['Chr'] = gene_exp_data['Chr'].astype(np.int)
    gene_expression_22 = gene_exp_data[gene_exp_data['Chr'] == 22]
    gene_t = gene_expression_22.melt(list(gene_expression_22.columns[:4]), var_name='sample_id', value_name='Value')
    pop = pd.read_csv(pop_file, sep = ' ')
    pop = pop.rename(columns ={'sample': 'sample_id'})
    exp_pop = gene_t.merge(pop, on = "sample_id", how = "outer").dropna()
    exp_pop  = exp_pop[['Gene_Symbol', 'Coord', 'sample_id', 'Value', 'group']]
    bed = open_bed(plink_bed)
    val2 = bed.read()
    bim_file = pd.read_csv(plink_bim, sep='\t', header=None, 
            names=['CHR', 'SNP', 'GP', 'POS', 'A1', 'A2'])
    gene_list = gene_expression_22['Gene_Symbol']
    sample_ids = bed.iid
    return gene_list, sample_ids, exp_pop, val2, bim_file, desired_pop
=======
    gene_exp_data = pd.read_csv(gene_exp_out)
    
    bed = open_bed(plink_bed)
    samples = bed.iid
    values = bed.read()
    pop = pd.read_csv("pop_file")
    sample_ids = pop.iloc[:, 0].str.split().str[0]
    pop_groups = pop.iloc[:, 0].str.split().str[2]
    pop_df = pd.DataFrame({'sample_ids':sample_ids, 'pop_groups':pop_groups})
    
    subset = pop_df[pop_df['pop_groups'] == desired_pop]
    
    idxs = []
    for i in af_subset['sample_ids']:
        idxs.append(list(samples).index(i))
    
    new_ind = values[idxs]
    
    bim_file = pd.read_csv(plink_bim, sep='\t', header=None, 
            names=['CHR', 'SNP', 'GP', 'POS', 'A1', 'A2'])
        
    return gene_exp_data, new_ind, bim_file, subset
>>>>>>> dd86d5c7a27bbc1eeaa6c3a7e5d91bd155aa49ad
