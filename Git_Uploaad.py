import json
import csv

json_file_path = 'Your file in the same folder of script.json'
csv_file_path = 'Your file output in the same folder of script.csv'

# Opening JSON file and loading the data
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)
#taking the results out as variables
Results = data["results"]

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header row
    csv_writer.writerow(['seqName', 'nucKey', 'nucValue', 'substitutions'])

    for result in Results:
        seq_name = result['seqName']
        nuctoAA = result['nucToAaMuts']
        substitutions = result['substitutions']

        # Prepare a string containing all substitutions with seqName
        substitution_str = ', '.join([f"{seq_name}:{sub['refNuc']}{sub['pos']}{sub['qryNuc']}" for sub in substitutions])

        # Iterate over nucToAaMuts
        for nuc, values in nuctoAA.items():
            nuc_key = nuc
            nuc_value = values[0]
            # Write data to CSV
            csv_writer.writerow([seq_name, nuc_key, nuc_value, substitution_str])
