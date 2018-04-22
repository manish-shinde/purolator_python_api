
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


url = "https://devwebservices.purolator.com/EWS/V1/Locator/LocatorService.wsdl"
client = Client(url,username='yourusername',password='yourpassword')
Language = client.factory.create('ns0:Language')
RequestContext = client.factory.create('ns0:RequestContext')
RequestContext.Version = '1.0'
RequestContext.GroupID = 'xxx'
RequestContext.RequestReference = 'Rating Example'
RequestContext.Language = Language.en
RequestContext.UserToken = 'YOURUserToken'
client.set_options(soapheaders=RequestContext)
print "client response-->",client
##########################################################################
# GetLocationsByAddress(ns0:Address Address, ns0:SearchOptions SearchOptions, ns0:LocationTypes LocationTypes, ns0:HoursOfOperation HoursOfOperation, ns0:DaysOfOperation DaysOfOperation)
# GetLocationsByCity(xs:string CountryCode, xs:string CityName, xs:string ProvinceStateCode, ns0:SearchOptions SearchOptions, ns0:LocationTypes LocationTypes, ns0:HoursOfOperation HoursOfOperation, ns0:DaysOfOperation DaysOfOperation)
# GetLocationsByCoordinates(ns0:Coordinates Coordinates, ns0:SearchOptions SearchOptions, ns0:LocationTypes LocationTypes, ns0:HoursOfOperation HoursOfOperation, ns0:DaysOfOperation DaysOfOperation)
# GetLocationsByPointOfInterest(xs:string PointOfInterest, ns0:SearchOptions SearchOptions, ns0:LocationTypes LocationTypes, ns0:HoursOfOperation HoursOfOperation, ns0:DaysOfOperation DaysOfOperation)
# GetLocationsByPostalCode(xs:string PostalCode, ns0:SearchOptions SearchOptions, ns0:LocationTypes LocationTypes, ns0:HoursOfOperation HoursOfOperation, ns0:DaysOfOperation DaysOfOperation)


#service 1 : GetLocationsByAddress

GetLocationsByAddressRequestContainer = client.factory.create('ns0:GetLocationsByAddressRequestContainer')

Address = client.factory.create('ns0:Address')
SearchOptions = client.factory.create('ns0:SearchOptions')
LocationTypes = client.factory.create('ns0:LocationTypes')
HoursOfOperation = client.factory.create('ns0:HoursOfOperation')
DaysOfOperation = client.factory.create('ns0:DaysOfOperation')



print "MyAddress>>>>>>>",GetLocationsByAddressRequestContainer
Address.AddressLine1 = '120 Dundas St E'
Address.AddressLine2 = 'Calgary, AB'
Address.AddressLine3 = 'T2P3N9'

SearchOptions.RadialDistanceInKM = '100'
# GetLocationsByAddressRequestContainer.SearchOptions.HoldForPickup = 'Edmonton'
SearchOptions.DangerousGoods = 'true'
# GetLocationsByAddressRequestContainer.SearchOptions.Kiosk = 'Edmonton'
SearchOptions.StreetAccess = 'true'
SearchOptions.WheelChairAccess = 'true'
SearchOptions.MaxNumberOfLocations = '10'
LocationTypes.LocationType = 'ShippingCentre'
HoursOfOperation.OpenTime = '09:00:00'
HoursOfOperation.CloseTime = '17:00:00'
HoursOfOperation.CurrentlyOpen = True
HoursOfOperation.GMTOffset = '17:00:00'
DaysOfOperation.DaysOfWeek =['Monday']
response = client.service.GetLocationsByAddress(Address, SearchOptions, LocationTypes, HoursOfOperation, DaysOfOperation)
print "GetLocationsByAddress_response",response
################################################################################################
#service 2  GetLocationsByCity
CountryCode  = 'ON'
CityName = 'Mississuaga'
ProvinceStateCode = 'CA'
response2= client.service.GetLocationsByCity(CountryCode,CityName,ProvinceStateCode,SearchOptions,LocationTypes,HoursOfOperation,DaysOfOperation)
print "GetLocationsByCity_response",response2
###############################################################################################
#service 3 GetLocationsByCoordinates
Coordinates = client.factory.create('ns0:Coordinates')
Coordinates.Longitude = '43.3310093000'
Coordinates.Latitude = '79.8195676000'
response3=client.service.GetLocationsByCoordinates(Coordinates,SearchOptions,LocationTypes,HoursOfOperation,DaysOfOperation)
print "GetLocationsByCoordinates_response",response3
###################################################################################
#method 4 GetLocationsByPointOfInterest
PointOfInterest ="FairView"
response4=client.service.GetLocationsByPointOfInterest(PointOfInterest,SearchOptions,LocationTypes,HoursOfOperation,DaysOfOperation)
print "GetLocationsByPointOfInterest_response",response4
#######################################################################
# method 5 GetLocationsByPostalCode
PostalCode = 'L5N3B5'
response5=client.service.GetLocationsByPostalCode(PostalCode,SearchOptions,LocationTypes,HoursOfOperation,DaysOfOperation)
print "GetLocationsByPostalCode_response",response5