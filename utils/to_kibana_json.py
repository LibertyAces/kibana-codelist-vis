import glob, json, os
for fname in glob.glob("./*.json"):

	try: os.mkdir("json")
	except FileExistsError:
		pass

	print("Parsing " + fname)
	# Load the old JSON
	data = json.load(open(fname, "rb"))

	# Create the new JSON
	the_json = {
		"_index": ".kibana",
		"_type": "doc",
		"_id": "x-lff-lookup:" + data["id"],
		"_source": {
			"type": "x-lff-lookup",
			"config": {
				"lookupType": data["title"],
				"fieldType": data["fieldType"],
				"map": data["map"]
			}
		}
	}

	# Write the output JSON
	fpath_out = os.path.realpath(os.path.join("./json/" + fname))
	with open(fpath_out, "wb") as f:
		out = json.dumps(the_json, indent=4)
		print(fpath_out)
		print(out)
		f.write(json.dumps(the_json, indent=4).encode("utf-8"))
