import sys
import json
from quantiphy import Quantity

inv_units = {
   "Hz" : "s",
   "hz" : "s",
   "s"  : "Hz",
   "Ω"  : "S",
   "ohm": "S",
   "Ohm": "S",
   "S"  : "Ω"
}

try:
   iv = Quantity(sys.argv[1])
   if iv.units == '':
      conv_result = Quantity(1.0/iv).render()
   else:
      unit = inv_units.get(iv.units, iv.units + "⁻¹")
      conv_result = Quantity(1.0/iv, unit).render()
except Exception as e:
   conv_result = 'Invalid value'

# The output JSON file for Alfred
result_json = {"items": [
   {
   "title": conv_result,
   "subtitle": "Copy to Clipboard",
   "arg": conv_result
   }
]}

print(json.dumps(result_json))
