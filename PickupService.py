
from suds.client import Client

"""
required fields for basic client response : 
1.url  (different for each service)
development and production environment urls are different.please check with developers guide after creating developer account
2.username - provided by purolator
3.password - provided by purolator
4. Language- currently english and french are supported
5.UserToken -  provided with developer account. production account does not need one
6.Version - latest version of particular service. Provided in each pdf of each service's developer guide
"""

url = "https://devwebservices.purolator.com/EWS/V1/PickUp/PickUpService.wsdl"
client = Client(url,username='yourusername',password='yourpassword')
Language = client.factory.create('ns0:Language')
RequestContext = client.factory.create('ns0:RequestContext')
RequestContext.Version = '1.2'
RequestContext.GroupID = 'xxx'
RequestContext.RequestReference = 'Pickup Examples'
RequestContext.Language = Language.en
RequestContext.UserToken = 'YourUserToken'
print"RequestContext",RequestContext
client.set_options(soapheaders=RequestContext)
print "first client response",client
##########################################################################
PickUpHistorySearchCriteria = client.factory.create('ns0:PickUpHistorySearchCriteria')

PickUpHistorySearchCriteria.AccountNumber = "yourAccountNumber"
PickUpHistorySearchCriteria.ConfirmationNumber = "YourConfirmationNumber"
PickUpHistorySearchCriteria.FromDate = "2010-03-20"
PickUpHistorySearchCriteria.MaxNumOfRecords = 10
PickUpHistorySearchCriteria.ToDate = "2010-03-30"

response1 = client.service.GetPickUpHistory(PickUpHistorySearchCriteria)
print "GetPickUpHistory_response>>",response1
