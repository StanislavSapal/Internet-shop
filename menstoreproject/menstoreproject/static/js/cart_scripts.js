$(document).ready(function() {
$('button[class*=minus]').click(function() {
    let url = 'http://127.0.0.1:8000/cart/'
    $.get(url, function() {
        let element = document.getElementById('31')
        alert(element)
    });
    });
});