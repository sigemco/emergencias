$(function() {
  window.addEventListener("load", function() {
    Notification.requestPermission(function(status) {
      // Esto me permite usar Notification.permission con Chrome/Safari
      if (Notification.permission !== status) {
        Notification.permission = status;
      }
    });
  });
  var endpoint = "";
  var loc = window.location;
  var wsStart = "ws://";
  if (loc.protocol == "https:") {
    wsStart = "wss://";
  }
  // endpoint = wsStart + loc.host + loc.pathname
  endpoint = wsStart + loc.host + "/usuarios/";

  var socket = new ReconnectingWebSocket(endpoint);

  socket.onmessage = function(e) {
    // console.log("message", e.data);
    var userData = JSON.parse(e.data);
    console.log(userData);
    switch (userData.type) {
      case "user_update":
        //console.log(userData);
        $("#new_user").html(userData.html_users);
        $("#conectados").html(userData.dato);

        break;
    }
  };
  /*https://developer.mozilla.org/es/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications
  Como la conexión es asincronica y es propensa a fallar, 
  no hay garantia de poder llamar al metodo send() inmediatamente 
  despúes de haber creado el objeto WebSocket de manera exitosa. 
  Para enviar información se debe estar seguro de que almenos una 
  conexión ya esta abierta, usando el manejador onopen:*/
  socket.onopen = function(e) {
    //console.log("open", e);
  };

  socket.onerror = function(e) {
    //console.log("error", e);
  };
  socket.onclose = function(e) {
    console.log("close", e);
  };
  /*
  var du = new DeviceUUID().parse();
  var dua = [
    du.browser,
    du.version,
    du.os,
    du.platform,
    du.source,
    du.isMobile,
    du.isDesktop,
    du.isBot
  ];

  console.log(dua);
  
  document.querySelector("#solicitar").onclick = function(e) {
    var message = "hola raul";
    socket.send(
      JSON.stringify({
        message: message
      })
    );
  };*/
});
