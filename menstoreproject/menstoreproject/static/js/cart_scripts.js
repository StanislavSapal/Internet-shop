$(document).ready(function() {

    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + "=")) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }

    $('button[class*=delete_button]').click(function() {
        let url = '/api/v1/cartitems/'
        let cart_item_id = $(this).parent().parent().attr('id');
        $.ajax({
            url: url + cart_item_id + '/',
            type: 'DELETE',
            data: {},
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            contentType:'application/json',
            dataType: 'json',
            error: function(result){
                alrert('Error')
            },
            success: function(result) {
                alert('WOW');
            }
        });
    });
});