# Switch View - Visualization Layers
# Visualization "Layers" help improve user experience by providing larger visualization areas
#
# Yahao(Frank) Yan
# Implemented on: 08/03/2018
# TIBCO Spotfire 7.0 API Reference: https://docs.tibco.com/pub/doc_remote/spotfire/7.0.1/doc/api/Index.aspx

# Classes for visuals
from Spotfire.Dxp.Application.Visuals import *
from System.Drawing import Color

#Different layers (In this example, there are 3 layers):
#Layer 1:
if Document.Properties["PropertyA"] == "Key1":
	# Modify X-Axis, Y-Axis, Coloring Categotiy, and Data Limit
	Document.Properties["ViewX"] = "[Column]"
	Document.Properties["ViewY"] = "UniqueCount([Column])"
	Document.Properties["ViewColorBy"] = "[Column]"
	Document.Properties["ViewDataLimit"] = "Condition"
#Layer 2:
elif Document.Properties["PropertyB"] == "Key2":
	Document.Properties["ViewX"] = "[Column]"
	Document.Properties["ViewY"] = "UniqueCount([Column])"
	Document.Properties["ViewColorBy"] = "[Column]"
	Document.Properties["ViewDataLimit"] = "Condition"
#Layer 3:
elif Document.Properties["PropertyC"] == "Key3":
	Document.Properties["ViewX"] = "[Column]"
	Document.Properties["ViewY"] = "UniqueCount([Column])"
	Document.Properties["ViewColorBy"] = "[Column]"
	Document.Properties["ViewDataLimit"] = "Condition"

#Change Visualization Properties (In this example, I am using bar charts):
#Set P to current Page
p = Document.ActivePageReference
#Loop through visualizations
for v in p.Visuals:
	if v.Title == "Title":
		#Layer 1:
		if Document.Properties["PropertyA"] == "Key1":
			vis = v.As[VisualContent]()
			#Set BarChart to Stacked
			vis.StackMode = vis.StackMode.Stack
		elif Document.Properties["PropertyB"] == "Key2":
		#Layer 2:
			vis = v.As[VisualContent]()
			#Set BarChart to Side-by-side
			vis.StackMode = 0
		#Layer 3:
		elif Document.Properties["PropertyC"] == "Key3":
			vis = v.As[VisualContent]()
			#Set BarChart to Stacked
			vis.StackMode = vis.StackMode.Stack
			#Change default colors
			vis.ColorAxis.Categorical.ColorMap["Column"] = Color.Green
			vis.ColorAxis.Categorical.ColorMap["Column"] = Color.Orange
