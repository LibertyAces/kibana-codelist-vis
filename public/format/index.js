import { fieldFormats } from 'ui/registry/field_formats';
import getLookupFieldFormatClass from '../getLookupFieldFormatClass';

function createFieldFormat(fformat, FieldFormat) {
	var fformat = fformat;

	class FFormat extends getLookupFieldFormatClass(FieldFormat) {
		static id = fformat._id.replace("x-lff-lookup:", "");
		static title = fformat._source.lookupType;
		static fieldType = fformat._source.fieldType;
		constructor(params) {
			super(params);
			for(var i=0; i<fformat._source.map.length; i++) {
				this.map[fformat._source.map[i].key] = fformat._source.map[i]
			}
		}
	}
	return FFormat;
}

function registerFormatters(fformats) {
	for (var i=0; i < fformats.length; i++) {
		fieldFormats.register(function(FieldFormat) {
			var fformat = this;
			return createFieldFormat(fformat, FieldFormat);
		}.bind(fformats[i])); // Hack: bind fformats[i] as 'this' to the function's scope to cope with asynchronous behaviour.
	}
};

// Getting the data from the API
$.ajax({
	type: "GET",
	url: '../api/kibana_codelist_vis/lookup',
	// Data must be loaded synchronously during the Kibana web app init time.
	async: false,
	success: function(data) {
		var fformats = data["hits"]["hits"];
		registerFormatters(fformats);
	},
	error: function(error) {
		console.log(error);
	}
});
