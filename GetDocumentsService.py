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


url = "https://devwebservices.purolator.com/EWS/V1/ShippingDocuments/ShippingDocumentsService.wsdl"
client = Client(url,username='myusername',password='mypassword')
Language = client.factory.create('ns0:Language')
RequestContext = client.factory.create('ns0:RequestContext')
RequestContext.Version = '1.3'
RequestContext.GroupID = 'xxx'
RequestContext.RequestReference = 'Rating Example'
RequestContext.Language = Language.en
RequestContext.UserToken = 'myusertoken'
client.set_options(soapheaders=RequestContext)
print "first client response",client
#######################################################################################################
# method1 :getdocument
ArrayOfDocumentCriteria = client.factory.create('ns0:ArrayOfDocumentCriteria')
DocumentCriteria = client.factory.create('ns0:DocumentCriteria')
DocumentCriteria.PIN.Value = 329015010179  #generic pin got after performing create shipment
DocumentCriteria.DocumentTypes.DocumentType = "DomesticBillOfLading"
ArrayOfDocumentCriteria.DocumentCriteria = DocumentCriteria
response1 = client.service.GetDocuments('PDF',False,ArrayOfDocumentCriteria)
print "GetDocuments_response",response1

##################################################################################
#method 2 :GetShipmentManifestDocument
ArrayOfShipmentManifestDocumentCriteria = client.factory.create('ns0:ArrayOfShipmentManifestDocumentCriteria')
ShipmentManifestDocumentCriteria = client.factory.create('ns0:ShipmentManifestDocumentCriteria')
ShipmentManifestDocumentCriteria.ManifestDate = '2010-03-15'
ArrayOfShipmentManifestDocumentCriteria.ShipmentManifestDocumentCriteria = ShipmentManifestDocumentCriteria

response2 = client.service.GetShipmentManifestDocument(ArrayOfShipmentManifestDocumentCriteria)
print "GetShipmentManifestDocument_response2>>>>>>>>>>>>>>>",response2




