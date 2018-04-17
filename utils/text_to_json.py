import glob, re, json, os
from collections import *
for fname in glob.glob("./*.txt"):

	try: os.mkdir("json")
	except FileExistsError:
		pass


	# Create key-value map
	_map = OrderedDict()
	with open(fname, "rb") as f:
		for line in f:
			line=line.decode("utf-8")
			line=line.strip()

			# Regex to the line
			_re = re.search(r"^(\d+).?\s(.*)", line)
			if _re is None:
				continue
			
			# Get KEY
			key = _re.group(1)
			
			# Get VAL
			val = _re.group(2)
			val = val.strip("-")
			val = val.strip()
			#to ascii correction
			val = val.replace("\u2011", "-") 

			# Store key-val
			_map[key] = {
				"label": val
			}
	
	_id = fname[:-3].strip("./").replace(" ", "_").lower()
	title = fname[:-3].strip("./").replace("_", " ")
	fname_out = _id+".json"
	fpath_out = os.path.realpath(os.path.join("./json/"+fname_out))

	# Create the JSON
	the_json = {
		"id": _id,
		"title": title,
		"fieldType": ["number"],
		"map": _map
	}

	with open(fpath_out, "wb") as f:
		out = json.dumps(the_json, indent=4)
		print(fpath_out)
		print(out)
		f.write(json.dumps(the_json, indent=4).encode("utf-8"))
