#正向的case
case1='''<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xmlns:xsd="http://www.w3.org/2001/XMLSchema">
          <soap:Header>
            <OGHeader xmlns="http://webservices.micros.com/og/4.3/Core/" transactionID="2019062118114433750450">
              <Origin entityID="OW1" systemType="WEB"/>
              <Destination entityID="TI" systemType="ORS"/>
            </OGHeader>
          </soap:Header>
          <soap:Body>
            <FetchProfileRequest xmlns="http://webservices.micros.com/oqq/5.1/Name.wsdl">
              <NameID type="INTERNAL">186217986</NameID>
            </FetchProfileRequest>
          </soap:Body>
        </soap:Envelope>'''
#反向的case
case2='''<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xmlns:xsd="http://www.w3.org/2001/XMLSchema">
          <soap:Header>
            <OGHeader xmlns="http://webservices.micros.com/og/4.3/Core/" transactionID="2019062118114433750450">
              <Origin entityID="OW1" systemType="WEB"/>
              <Destination entityID="TI" systemType="ORS"/>
            </OGHeader>
          </soap:Header>
          <soap:Body>
            <FetchProfileRequest xmlns="http://webservices.micros.com/oqq/5.1/Name.wsdl">
              <NameID type="INTERNAL">1862179863</NameID>
            </FetchProfileRequest>
          </soap:Body>
        </soap:Envelope>'''

dict1={"success":case1,"fail":case2}