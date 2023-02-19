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
        let cart_item = $(this).parent().parent()
        let cart_item_id = cart_item.attr('id');
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
                alert('Error')
            },
            success: function(result) {
                $(cart_item).remove()
            }
        });
    });

    $('button[class*=minus_button]').click(function() {
        let url = '/api/v1/cartitems/'
        let cart_item = $(this).closest('tr')
        let cart_item_id = cart_item.attr('id');
        console.log(cart_item_id)
        let cart_item_quantity = cart_item.find('input.quantity_input');
        console.log(cart_item_quantity);
        let cart_item_quantity_value = Number(cart_item_quantity.attr('value'));
        console.log(cart_item_quantity_value);
        let new_quantity = cart_item_quantity_value - 1;
        console.log(new_quantity)
        console.log(typeof new_quantity)
        let data = JSON.stringify({'quantity': new_quantity});

        $.ajax({
            url: url + cart_item_id + '/',
            type: 'PATCH',
            data: data,
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            contentType:'application/json',
            dataType: 'json',
            error: function(result){
                console.log(result)
            },
            success: function(result) {
                cart_item_quantity.attr('value', new_quantity);
            }
        });
    });

    $('button[class*=plus_button]').click(function() {
        let url = '/api/v1/cartitems/'
        let cart_item = $(this).closest('tr')
        let cart_item_id = cart_item.attr('id');
        console.log(cart_item_id)
        let cart_item_quantity = cart_item.find('input.quantity_input');
        console.log(cart_item_quantity);
        let cart_item_quantity_value = Number(cart_item_quantity.attr('value'));
        console.log(cart_item_quantity_value);
        let new_quantity = cart_item_quantity_value + 1;
        console.log(new_quantity);
        let data = JSON.stringify({'quantity': new_quantity});

        $.ajax({
            url: url + cart_item_id + '/',
            type: 'PATCH',
            data: data,
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            contentType:'application/json',
            dataType: 'json',
            error: function(result){
                console.log(result)
            },
            success: function(result) {
                cart_item_quantity.attr('value', new_quantity)
            }
        });
    });
});
