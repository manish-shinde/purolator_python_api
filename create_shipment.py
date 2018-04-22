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

url = "https://devwebservices.purolator.com/ews/v1/Shipping/ShippingService.wsdl"
client = Client(url,username='myusername',password='mypassword')
Language = client.factory.create('ns0:Language')
RequestContext = client.factory.create('ns0:RequestContext')
RequestContext.Version = '1.5'
RequestContext.GroupID = 'xxx'
RequestContext.RequestReference = 'Create Shipment Example'
RequestContext.Language = Language.en
RequestContext.UserToken = 'myusertoken'
client.set_options(soapheaders=RequestContext)
print "thats client-->",client

################################################################################
#create basic shipment
#1 piece shipment, 10lbs, Purolator Express Service on a Thermal 4x6 Label
#CreateShipment(ns0:Shipment Shipment, ns0:PrinterType PrinterType)
MyShipment = client.factory.create('ns0:Shipment')
CreateShipmentRequestContainer = client.factory.create('ns0:CreateShipmentRequestContainer')
MyShipment.SenderInformation.Address.Name = 'Manish Shinde'
# OriginAddress.Company = None
# OriginAddress.Department = None
MyShipment.SenderInformation.Address.StreetNumber = 1234
MyShipment.SenderInformation.Address.StreetName = 'Main Street'
MyShipment.SenderInformation.Address.City = 'Mississauga'
MyShipment.SenderInformation.Address.Province = 'ON'
MyShipment.SenderInformation.Address.Country = 'CA'
MyShipment.SenderInformation.Address.PostalCode = 'L4W5M8'
PhoneNumber = client.factory.create('ns0:PhoneNumber')
MyShipment.SenderInformation.Address.PhoneNumber.CountryCode = '1'
MyShipment.SenderInformation.Address.PhoneNumber.AreaCode = '905'
MyShipment.SenderInformation.Address.PhoneNumber.Phone = '5555555'
MyShipment.SenderInformation.Address.PhoneNumber.Extension = '5555555'

ReceiverInformation = client.factory.create('ns0:ReceiverInformation')
MyShipment.ReceiverInformation.Address.Name = 'John Doe'
MyShipment.ReceiverInformation.Address.StreetNumber = 1234
MyShipment.ReceiverInformation.Address.StreetName = 'Douglas Road'
MyShipment.ReceiverInformation.Address.City = 'Burnaby'
MyShipment.ReceiverInformation.Address.Province = 'BC'
MyShipment.ReceiverInformation.Address.Country = 'CA'
MyShipment.ReceiverInformation.Address.PostalCode = 'V5C1A1'

MyShipment.ReceiverInformation.Address.PhoneNumber.CountryCode = '1'
MyShipment.ReceiverInformation.Address.PhoneNumber.AreaCode = '604'
MyShipment.ReceiverInformation.Address.PhoneNumber.Phone = '2982181'
MyShipment.ReceiverInformation.Address.PhoneNumber.Extension = '2982181'

MyShipment.PackageInformation.ServiceID = 'PurolatorExpress'
MyShipment.PackageInformation.Description = 'PurolatorExpress detail'
MyShipment.PackageInformation.TotalPieces = '1'

MyShipment.PackageInformation.TotalWeight.Value = 10
MyShipment.PackageInformation.TotalWeight.WeightUnit.value = 'lb'

MyShipment.PaymentInformation.PaymentType.value = "Sender"
MyShipment.PaymentInformation.RegisteredAccountNumber = #yourRegisteredAccountNumber
MyShipment.PaymentInformation.BillingAccountNumber = #yourBillingAccountNumber
MyShipment.ShipmentDate = '2017-12-05'

# Populate the Pickup Information
PickupInformation = client.factory.create('ns0:PickupInformation')
PickupInformation.PickupType.value = "DropOff"
MyShipment.PickupInformation = PickupInformation
CreateShipmentRequestContainer.Shipment = MyShipment
MyPrinterType = client.factory.create('ns0:PrinterType')
MyPrinterType.Thermal = 'Thermal'
CreateShipmentRequestContainer.PrinterType = MyPrinterType

response = client.service.CreateShipment(CreateShipmentRequestContainer)
print "CreateShipment_response",response

ValidateShipmentRequestContainer = client.factory.create('ns0:ValidateShipmentRequestContainer')
ValidateShipmentRequestContainer.Shipment = MyShipment
response2 = client.service.ValidateShipment(ValidateShipmentRequestContainer)

print "ValidateShipment_response",response2
