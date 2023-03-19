import pandas as pd

data = pd.read_csv('input_vehicles2.csv').to_dict('records')
ref = pd.read_csv('vehicle_reference.csv').to_dict('records')

for entry in data:
	for match in ref:
		if entry['Asset Type'] == match['Asset Type']:
			print(str(entry['Asset Type']) + ' ' + str(entry['Model Name']) + ': ' + str(match['Asset Type']) + ' ' + str(match['Model']))
