def writeJSON(data):
	json_data = open('phcorner.json','w')
	json_data.write(data)
	json_data.close()