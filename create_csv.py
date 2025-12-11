import json
import csv

with open('final_context.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

triplets = data.get('final_knowledge_graph', [])

if triplets:
    with open('knowledge_graph.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['head', 'relation', 'tail']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(triplets)
    print("Successfully created knowledge_graph.csv")
else:
    print("No triplets found in final_context.json")
