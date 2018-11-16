$(function () {
    document.documentElement.style.fontSize = innerWidth/10 + "px";
    urlStr=location.href;
    var idStr=urlStr.split("/")[3];
    console.log(idStr);
    var $span=$(document.getElementById(idStr));
    $span.css("background", "url(/static/common/img/"+idStr+"1.png)");
    $span.css("background-size", "0.8rem");
});