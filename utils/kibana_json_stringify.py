import glob, json, os
for fname in glob.glob("./*.json"):

	try: os.mkdir("json")
	except FileExistsError:
		pass

	print("Parsing " + fname)
	# Load the old JSON
	data = json.load(open(fname, "rb"))

	# Map-specific JSON
	map_json = data["_source"]["config"]["map"]
	general_name = fname[:-5]
	map_json_fname = general_name + "@map.json"

	# General JSON
	the_json = data
	the_json["_source"]["config"]["map"] = "@ref-map"

	# Write the output JSON
	fpath_out = os.path.realpath(os.path.join("./json/" + fname))
	with open(fpath_out, "wb") as f:
		out = json.dumps(the_json, indent=4)
		print(fpath_out)
		print(out)
		f.write(json.dumps(the_json, indent=4).encode("utf-8"))

	# Write the output JSON
	fpath_out = os.path.realpath(os.path.join("./json/" + map_json_fname))
	with open(fpath_out, "wb") as f:
		out = json.dumps(map_json, indent=4)
		f.write(json.dumps(map_json, indent=4).encode("utf-8"))