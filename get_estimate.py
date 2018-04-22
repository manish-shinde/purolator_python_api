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


url = "https://devwebservices.purolator.com/EWS/V1/Estimating/EstimatingService.wsdl"
client = Client(url,username='myusername',password='mypassword')

Language = client.factory.create('ns0:Language')

RequestContext = client.factory.create('ns0:RequestContext')

RequestContext.Version = '1.4'
RequestContext.GroupID = 'xxx'
RequestContext.RequestReference = 'Rating Example'
RequestContext.Language = Language.en
RequestContext.UserToken = 'myusertoken'
print"RequestContext",RequestContext
client.set_options(soapheaders=RequestContext)
print "first client response",client
##################################################################################################

BillingAccountNumber = 'YOURBILLINGACCOUNTNUMER'
SenderPostalCode = 'L4W5M8'
ReceiverAddress = client.factory.create('ns0:ShortAddress')
ReceiverAddress.City = 'Burnaby'
ReceiverAddress.Province = 'BC'
ReceiverAddress.Country = 'CA'
ReceiverAddress.PostalCode = 'V5C1A1'
PackageType = 'ExpressPack'
TotalWeight = client.factory.create('ns0:TotalWeight')
TotalWeight.Value = 10
WeightUnit = client.factory.create('ns0:WeightUnit')
TotalWeight.WeightUnit.value = WeightUnit.lb
response = client.service.GetQuickEstimate(BillingAccountNumber,SenderPostalCode,ReceiverAddress,PackageType,TotalWeight)
print ">>>>>>>>response>>>>>>>>",response
##################################################################################################

