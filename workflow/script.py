import sys
import json
from quantiphy import Quantity


try:
   iv = Quantity(sys.argv[1])
   if iv.units == '':
      conv_result = Quantity(1.0/iv).render()
   else:
      conv_result = Quantity(1.0/iv, iv.units + "⁻¹").render()
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
