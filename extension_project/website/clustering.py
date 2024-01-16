import pandas as pd
import os

# REMOVE THE OLD AUDIO FILE
def override_old_excel():
    try:
        os.remove('CLUSTER1.xlsx')
        os.remove('CLUSTER2.xlsx')
        os.remove('clusters.zip')
    except OSError as e:
        print('File Not Found!')

#load the excel files
master_list_path = 'masterlist.xlsx'

def cluster(file):
    master_list = pd.read_excel(master_list_path)
    cluster_file = pd.read_excel(file)

    master_list.fillna("No name", inplace=True)
    cluster_file.fillna("No name", inplace=True)
    
    resident = cluster_file['name']

    master_list_C1 = master_list['CLUSTER1']
    master_list_C2 = master_list['CLUSTER2']

    clustered_cluster1 = []
    clustered_cluster2 = [] 

    for name in resident:
        name = name.lower()
        name = name.strip()
        
        for master in master_list_C1:
            master = master.lower()
            master = master.strip()
            if name == master:
                clustered_cluster1.append(name)
            
        for master2 in master_list_C2:
            master2 = master2.lower()
            master2 = master2.strip()
            if name == master2:
                clustered_cluster2.append(name)
    clustered_cluster1 = sorted(set(clustered_cluster1))
    clustered_cluster2 = sorted(set(clustered_cluster2))

    index_contacts1 = []
    contacts1 = []

    index_contacts2 = []
    contacts2 = []
    for i, name in enumerate(resident):
        name = name.lower()
        name = name.strip()
        
        for cluster1_name in clustered_cluster1:
            if name == cluster1_name: 
                index_contacts1.append(cluster_file['contact'][i])
                contacts1.append(name)
                
        for cluster2_name in clustered_cluster2:
            if name == cluster2_name: 
                index_contacts2.append(cluster_file['contact'][i])
                contacts2.append(name)

    for i, name in enumerate(resident):
        name = name.lower()
        name = name.strip()
        
        for cluster1_name in clustered_cluster1:
            if name == cluster1_name: 
                index_contacts1.append(cluster_file['contact'][i])
                contacts1.append(name)
                
        for cluster2_name in clustered_cluster2:
            if name == cluster2_name: 
                index_contacts2.append(cluster_file['contact'][i])
                contacts2.append(name)

    df_cluster1 = pd.DataFrame({'Name' : contacts1,
                           'Number' : index_contacts1})

    df_cluster1_no_duplicates = df_cluster1.drop_duplicates(subset='Name', keep='last')
    df_cluster1_no_duplicates.to_excel('CLUSTER1.xlsx', index=False)

    df_cluster2 = pd.DataFrame({'Name' : contacts2,
                            'Number' : index_contacts2})
    df_cluster2_no_duplicates = df_cluster2.drop_duplicates(subset='Name', keep='last')
    df_cluster2_no_duplicates.to_excel('CLUSTER2.xlsx', index=False)



