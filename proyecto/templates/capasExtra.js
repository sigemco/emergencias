var covid19 = L.geoCsv(null, {
onEachFeature: function (feature, layer) {
    var popup = '';
    for (var clave in feature.properties) {
      var title = covid19.getPropertyTitle(clave);
      popup += '<b>'+title+' </b>'+feature.properties[clave]+'<br />';
    }
    layer.bindPopup(popup);

  },
  pointToLayer: function (feature, latlng) {
    return L.marker(latlng, {
      icon:L.icon({
        iconUrl: 'static/app/lib/leaflet/images/riezgo.png',

        iconSize: [41,41],
        shadowSize:   [41, 41],
        shadowAnchor: [13, 20]
      })
    });
  },
  firstLineTitles: true,
   fieldSeparator: ',',
  latitudeTitle:'Latitude',
  longitudeTitle:'Longitude'
  });
  //map.addLayer(geoLayer);
  $.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-18-2020.csv', function(csv) {
    covid19.addData(csv);

  })
//  covid19.addTo(map)
var lc = map.layerscontrol;
lc.addOverlay(covid19,'COVID19')

var peajes= L.cartoDB('https://cipetsig.carto.com:443/api/v2/sql?q=select * from public.estaciones_de_peajes_de_argentina', {
      pointToLayer: function(feature, latlng) {
      return L.marker(latlng, {
      icon: L.icon({
      iconSize: [27, 40],
      iconAnchor: [13, 27],
      popupAnchor: [1, -24],
      iconUrl: 'static/app/lib/leaflet/images/peaje.jpg'
                  })
                              })
                                              },
      onEachFeature: function(feature, layer) {
      layer.bindPopup('<strong> Concecionario:</strong>'
      + feature.properties.concesionario_vial
      +'<br><strong>Direccion:</strong>'
      + feature.properties.direccion+ '<br><strong>Telefono:</strong>'
      + feature.properties.telefono +'<strong><br>Nombre del peaje:</strong>'
      + feature.properties.nombre_del_peaje+'<strong><br>Mail:</strong>'
      + feature.properties.dir_email+'<strong><br>Telefono de la estacion:</strong>'
      + feature.properties.telefono_estacion_de_peaje+ '</br> <strong>Localidad:</strong>'
      + feature.properties.localidad);
                                              }      });
lc.addOverlay(peajes,'PEAJES')
 var bomberos= L.cartoDB('https://cipetsig.carto.com/api/v2/sql?q=SELECT * FROM cipet_bomberos', {
      pointToLayer: function(feature, latlng) {
      return L.marker(latlng, {
      icon: L.icon({
      iconSize: [27, 40],
      iconAnchor: [13, 27],
      popupAnchor: [1, -24],
      iconUrl: 'static/app/lib/leaflet/images/bomberos.png'
                  })
                              })
                                              },
      onEachFeature: function(feature, layer) {
      layer.bindPopup('<strong> Descripcion:</strong>'
      + feature.properties.descripcio  +'<br><strong>Calle:</strong>'
      + feature.properties.calle+'<br>Nro:'
      + feature.properties.nro+ '</strong><br>Telefono:'
      + feature.properties.telefono +'</strong><br>Fax:'
      + feature.properties.fax+'</strong><br>Mail:'
      + feature.properties.mail+'</strong><br>Manejo de sustancias peligrosas:'
      + feature.properties.capacitaci+ '</br> Localidad:'
      + feature.properties.localidad+'</br> Partido:'
      + feature.properties.partido);
    }});
      lc.addOverlay(bomberos,'BOMBEROS') ;

     var ACA= L.cartoDB('https://cipetsig.carto.com/api/v2/sql?q=SELECT * FROM cipet_aca', {
      pointToLayer: function(feature, latlng) {
      return L.marker(latlng, {
      icon: L.icon({
      iconSize: [27, 27],
      iconAnchor: [13, 27],
      popupAnchor: [1, -24],
      iconUrl: 'static/app/lib/leaflet/images/logoACA.png'
                  })
                              })
                                              },
      onEachFeature: function(feature, layer) {
      layer.bindPopup('<strong> Dependencia:'
      + feature.properties.dependenci  + '</strong><br>Direccion:'
      + feature.properties.direccion + '</br> Telefono:'
      + feature.properties.telefono);
                                              }
                                                    });
      lc.addOverlay(ACA,'ACA') ;
      var aeropuerto= L.cartoDB('https://cipetsig.carto.com/api/v2/sql?q=SELECT * FROM cipet_aeropuertos', {
      pointToLayer: function(feature, latlng) {
      return L.marker(latlng, {
      icon: L.icon({
      iconSize: [27, 27],
      iconAnchor: [13, 27],
      popupAnchor: [1, -24],
      iconUrl: 'static/app/lib/leaflet/images/aeropuerto.png'
                  })
                              })
                                              },
      onEachFeature: function(feature, layer) {
      layer.bindPopup('<strong> NOMBRE:'
      + feature.properties.nombre  + '</strong><br>TIPO:'
      + feature.properties.tipo + '</br> DEPARTAMENTO:'
      + feature.properties.departament);
                                              }
                                            });
      lc.addOverlay(aeropuerto,'PISTAS') ;

      var Hospitales= L.cartoDB('https://cipetsig.carto.com/api/v2/sql?q=SELECT* FROM cipet_hospitales', {
      pointToLayer: function(feature, latlng) {
      return L.marker(latlng, {
      icon: L.icon({
      iconSize: [27, 27],
      iconAnchor: [13, 27],
      popupAnchor: [1, -24],
      iconUrl: 'static/app/lib/leaflet/images/hospitales.png'
                  })
                              })
                                              },
      onEachFeature: function(feature, layer) {
      layer.bindPopup('<strong> Descripcion:'
      + feature.properties.descripcio  + '</strong><br>Telefono:'
      + feature.properties.tela_fono +'</strong><br>Calle:'
      + feature.properties.calle+'</strong><br>Nro:'
      + feature.properties.nro+ '</br> Localidad:'
      + feature.properties.localidad +'</strong><br>Hospital Tipo:'
      + feature.properties.tipo_de_es+'</strong><br>Modalidad 1:'
      + feature.properties.modalidad + '</strong><br>Modalidad 2:'
      + feature.properties.modalida_1 + '</strong><br>Cantidad de Camas:'
      + feature.properties.camas);
                                              }
                                                                                                });

      lc.addOverlay(Hospitales,'HOSPISTALES') ;
      var kilometraje= L.cartoDB('https://cipetsig.carto.com/api/v2/sql?q=SELECT* FROM kilometrajes', {
      pointToLayer: function(feature, latlng) {
      return L.marker(latlng, {
      icon: L.icon({
      iconSize: [27, 27],
      iconAnchor: [13, 27],
      popupAnchor: [1, -24],
      iconUrl: 'static/app/lib/leaflet/images/kilometro.png'
                  })
                              })
                                              },
      onEachFeature: function(feature, layer) {
      layer.bindPopup('<strong> PAIS:'
      + feature.properties.pais  + '</strong><br>Prov:'
      + feature.properties.prov + '</br> RUTA:'
      + feature.properties.nombre+'<br>Km:'
      +feature.properties.km+'</br>');
                                              }
                                                                                          });
      lc.addOverlay(kilometraje,'POSTAS') ;
      var police= L.cartoDB('https://cipetsig.carto.com/api/v2/sql?q=SELECT* FROM cipet_policia', {
      pointToLayer: function(feature, latlng) {
      return L.marker(latlng, {
      icon: L.icon({
      iconSize: [27, 27],
      iconAnchor: [13, 27],
      popupAnchor: [1, -24],
      iconUrl: 'static/app/lib/leaflet/images/police.png'
                  })
                              })
                                              },
      onEachFeature: function(feature, layer) {
      layer.bindPopup('<strong> Descripcion:'
      + feature.properties.descripcio  + '</strong><br>Telefono:'
      + feature.properties.telefono +'<br> Fax:'
      + feature.properties.fax+'<br> Calle:'
      + feature.properties.calle+'<br> Nro:'
      + feature.properties.nro+ '<br> Localidad:'
      + feature.properties.localidad);
                                              }});
        lc.addOverlay(police,'POLICIA') ;
