import requests
from prettytable import PrettyTable

# Setting the Qdrant Instance URL
qdrant_url = "https://a3fec95c-9e3c-4315-b633-1cbcc1cae97b.europe-west3-0.gcp.cloud.qdrant.io"
api_key = "WLFCIoeUU5s-el3zW2iOM3AXBj2Ab1tF1_ufI58s5tYB4l1Ea6kOkA"

headers = {'api-key': api_key}

response = requests.get(f"{qdrant_url}/collections", headers=headers)

if response.status_code == 200:
    collections_info = response.json()['result']['collections'] 

    # Creating a Table
    table = PrettyTable()
    table.field_names = ["Collection Name", "# Shards", "Shard ID"]

    
    for collection in collections_info:
        collection_name = collection['name']  # getting the collection name
        
        # collections shards
        cluster_response = requests.get(f"{qdrant_url}/collections/{collection_name}/cluster", headers=headers)

        if cluster_response.status_code == 200:
            cluster_info = cluster_response.json()['result']  # accesing to the cluster info

            shard_count = cluster_info['shard_count']  # shards 
            shard_ids = [shard['shard_id'] for shard in cluster_info['local_shards']]  # shards Ids

            # add info to the table
            table.add_row([collection_name, shard_count, ', '.join(map(str, shard_ids))])
        else:
            print(f"Error {collection_name}")

    # Mostrar la tabla
    print(table)
else:
    print(f"Error getting list of collections: {response.status_code} - {response.text}")
