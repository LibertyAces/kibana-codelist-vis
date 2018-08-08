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

		/*
		 * Converts given value to a text value from this.map
		 * this.map = {
		 *   "1": {"value":"One"},
		 *   "2": {"value":"Two"},
		 * }
		 */
		convert(value) {
			var s_val = value.toString();
			var m_val = this.map[s_val];
			return m_val ? m_val.value+" ["+s_val+"]" : s_val;
		}
	}
}
