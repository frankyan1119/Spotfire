# Authentication - User Groups
# Used to limit visualizations/data details to different user groups
#
# Yahao(Frank) Yan & Bank of Montreal DG&A spotfire developers
# Implemented on: 15/02/2018
# TIBCO Spotfire 7.0 API Reference: https://docs.tibco.com/pub/doc_remote/spotfire/7.0.1/doc/api/Index.aspx

# Import corresponding class
from System.Threading import Thread

# (User group)"rstrip" removes all whitespace
if Document.Properties["TestUser"].rstrip() == "":
	username = Thread.CurrentPrincipal.Identity.Name
# (Tester)
else:
	username = Document.Properties["TestUser"]

# Set username:
# Truncate the username at the @sign (Spotfire SSO login will contain username@domain
# however, if domain information is relevent, addition text capture is required
currentUser = username
if username.find("@") > 0:
	currentUser = username[0:username.find("@")]
	Document.Properties["username"] = currentUser

# Set Required document properties 
Document.Properties["ErrorMessage"] = ""

# Import filter classes
import Spotfire.Dxp.Application.Filters as filters
import Spotfire.Dxp.Application.Filters.RadioButtonFilter
from Spotfire.Dxp.Application.Filters import FilterTypeIdentifiers
from Spotfire.Dxp.Data import DataPropertyClass
from Spotfire.Dxp.Application.Filters import ItemFiltering

myDocument = Application.Document

# reset all filters
for i in range(0,Document.FilteringSchemes.Count):
    Document.FilteringSchemes[i].ResetAllFilters()

# iterates through user tables, and filters data based on the user id
# In this example, we are only connected to one data source,
# the following algorithm needs to be changed if there is more than one 
# data source
for eachPage in myDocument.Pages:
	myPanel = eachPage.FilterPanel
	myFilter=myPanel.TableGroups[0].GetFilter("AliasFilter")
	myFilter.FilterReference.TypeId = FilterTypeIdentifiers.RadioButtonFilter
	try:
		rbFilter = myFilter.FilterReference.As[filters.RadioButtonFilter]()
		rbFilter.Value=(Document.Properties["username"])
		# automatically moves to the next page if no error is generated
		Document.ActivePageReference = NextPage

	except ValueError:
		#"exception block" is entered if an error is generated from "try blcok"(user is not permitted to see any data)
		rbFilter = myFilter.FilterReference.As[filters.RadioButtonFilter]()
		rbFilter.Value=ItemFiltering.None
		Document.Properties["ErrorMessage"] = "You have no items to view"


#--------------------------Note: Developer has to hide filter feature from users to make this code work--------------------------
