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

url = "https://devwebservices.purolator.com/EWS/V1/Tracking/TrackingService.wsdl"
client = Client(url,username='myusername',password='mypassword')
Language = client.factory.create('ns0:Language')
RequestContext = client.factory.create('ns0:RequestContext')
RequestContext.Version = '1.2'
RequestContext.GroupID = 'xxx'
RequestContext.RequestReference = 'Tracking service'
RequestContext.Language = Language.en
RequestContext.UserToken = 'myusertoken'
client.set_options(soapheaders=RequestContext)
print "first client response",client
######################################################################################################
# GetDeliveryDetails(ns0:PIN PIN)
# TrackPackagesByReference(ns0:TrackPackageByReferenceSearchCriteria TrackPackageByReferenceSearchCriteria)

PIN = client.factory.create('ns0:PIN')
PIN.Value = '329014521622'

GetDeliveryDetails_response = client.service.GetDeliveryDetails(PIN)
print ">>>>>>>>GetDeliveryDetails_response>>>>>>>>",GetDeliveryDetails_response

#######################################################################################
#dummy data 
TrackPackageByReferenceSearchCriteria = client.factory.create('ns0:TrackPackageByReferenceSearchCriteria')
TrackPackageByReferenceSearchCriteria.Reference = "RMA125"
TrackPackageByReferenceSearchCriteria.BillingAccountNumber = 'BILLING_ACCOUNT'
TrackPackageByReferenceSearchCriteria.ShipmentFromDate = "2009-04-22"
TrackPackageByReferenceSearchCriteria.ShipmentToDate = "2009-04-22"

# TrackPackageByReferenceSearchCriteria = MyTrackPackageByReferenceSearchCriteria
response = client.service.TrackPackagesByReference(TrackPackageByReferenceSearchCriteria)
print "TrackPackageByReferenceSearchCriteria_response",response