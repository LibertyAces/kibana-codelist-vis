export default function getLookupFieldFormatClass(FieldFormat) {
	return class LookupFieldFormat extends FieldFormat {
		constructor(params) {
			super(params);
			this.map = {};
			this._convert = {
				text: (value) => {
					return this.convert(value);
				},
				html: (value, field, hit, parsedUrl) => {
					return this.convert(value);
				}
			}
		}
		convert(value) {
			var mapVal=this.map[value.toString()];
			if(!mapVal) mapVal = value;
			else mapVal=mapVal.label;
			return (mapVal ? mapVal+" ["+value+"]" : value);
		}
	}
}