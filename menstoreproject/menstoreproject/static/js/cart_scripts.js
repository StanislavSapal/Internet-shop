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
        let url = '/api/v1/cartitems/';
        let cart_item = $(this).parent().parent();
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

    function changeSum(current_tr, multiplier) {
        let cart_item_price = current_tr.find('td.price_td');
        let cart_item_price_value = cart_item_price.text().split(' ')[0];
        let cart_item_sum = cart_item_price_value * multiplier;
        let total_item_price_field = current_tr.find('td.total_item_price_td');
        total_item_price_field.html(cart_item_sum + ' грн')
    };

    function changeTotalCartSum(current_tr) {
        let url = '/api/v1/cart/';
        let cart = current_tr.closest('tbody')
        let cart_id = cart.attr('id');
        let total_cart_sum_field = $('h5[class=total_cart_sum_h]')

        $.ajax({
            url: url + cart_id + '/',
            type: 'GET',
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            contentType: 'application/json',
            dataType: 'json',
            success: function(response) {
                total_cart_sum_field.html(response.total_cart_sum.price_total + ' грн.');
            },
            error: function() {}
        });
    };

    $('button[class*=minus_button]').click(function() {
        let url = '/api/v1/cartitems/';
        let cart_item = $(this).closest('tr');
        let cart_item_id = cart_item.attr('id');
        let cart_item_quantity = cart_item.find('input.quantity_input');
        let cart_item_quantity_value = Number(cart_item_quantity.attr('value'));
        let new_quantity = cart_item_quantity_value - 1;
        let data = JSON.stringify({'quantity': new_quantity});

        if (cart_item_quantity_value > 1) {
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
                    alert(result)
                },
                success: function(result) {
                    cart_item_quantity.attr('value', new_quantity);
                    changeSum(cart_item, new_quantity);
                    changeTotalCartSum(cart_item)
                }
            });
        } else {}
    });

    $('button[class*=plus_button]').click(function() {
        let url = '/api/v1/cartitems/';
        let cart_item = $(this).closest('tr');
        let cart_item_id = cart_item.attr('id');
        let cart_item_quantity = cart_item.find('input.quantity_input');
        let cart_item_quantity_value = Number(cart_item_quantity.attr('value'));
        let new_quantity = cart_item_quantity_value + 1;
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
                alert(result)
            },
            success: function(result) {
                cart_item_quantity.attr('value', new_quantity);
                changeSum(cart_item, new_quantity);
                changeTotalCartSum(cart_item)
            }
        });
    });
});
