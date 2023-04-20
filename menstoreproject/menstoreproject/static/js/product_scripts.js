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

    function changeCartitemQuantityOnNavbar(newValue) {
        let cart_item_quantity_span = $('span[class*=number_of_cartitems]');
        cart_item_quantity_span.text(newValue);
    };

    $('button[class*=minus_button]').click(function() {
        let plus_minus_buttons_div = $(this).parent().parent();
        let product_quantity_input = plus_minus_buttons_div.find('input.quantity_input');
        let product_quantity = Number(product_quantity_input.attr('value'));
        new_quantity = product_quantity - 1;
        if (new_quantity > 0) {
            product_quantity_input.attr('value', new_quantity)
        } else {}

    });

    $('button[class*=plus_button]').click(function() {
        let plus_minus_buttons_div = $(this).parent().parent();
        let product_quantity_input = plus_minus_buttons_div.find('input.quantity_input');
        let product_quantity = Number(product_quantity_input.attr('value'));
        new_quantity = product_quantity + 1;
        product_quantity_input.attr('value', new_quantity)
    });

    $('label[class*=size_choice_label]').click(function() {
        let size_div = $(this).parent().parent();
        let selected_size = $(this).text();
        size_div.attr('value', selected_size);
        let size_div_value = size_div.attr('value');
    });

    function successAddToCartMessage() {
        alert('Товар додано до кошика');
    }

    $('button[class*=add_to_cart_button]').click(function() {
        let url = '/api/v1/cartitems/';
        let minus_plus_add_div = $(this).parent();
        let product_info_and_options_div = minus_plus_add_div.parent();
        let size_div = product_info_and_options_div.find('div.size_div');
        size = size_div.attr('value');
        let product_id = minus_plus_add_div.attr('id');
        let product_quantity_input = minus_plus_add_div.find('input.quantity_input');
        let product_quantity = Number(product_quantity_input.attr('value'));
        let cart_item_quantity_span = $('span[class*=number_of_cartitems]');
        let cart_item_quantity = Number(cart_item_quantity_span.text());
        let new_cart_item_quantity = cart_item_quantity + 1;
        let data = JSON.stringify({"product": product_id,
                                   "quantity": product_quantity,
                                   "size": size});

        $.ajax({
            url: url,
            type: 'GET',
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            contentType:'application/json',
            dataType: 'json',
            success: function(result) {
                let cart_item_found = false;
                result.forEach(function(item) {
                    if (item.product == product_id && item.size == size) {
                        cart_item_found = true;
                        let cart_item_id = item.id;
                        let new_quantity = item.quantity + product_quantity;
                        let update_data = JSON.stringify({"quantity": new_quantity});
                        $.ajax({
                            url: url + cart_item_id + '/',
                            type: 'PATCH',
                            data: update_data,
                            headers: {
                                "X-CSRFToken": getCookie("csrftoken"),
                            },
                            contentType:'application/json',
                            dataType: 'json',
                            success: function(result) {
                                setTimeout(successAddToCartMessage, 50);
                            }
                        });
                    }
                });
                if (!cart_item_found) {
                    $.ajax({
                        url: url,
                        type: 'POST',
                        data: data,
                        headers: {
                            "X-CSRFToken": getCookie("csrftoken"),
                        },
                        contentType:'application/json',
                        dataType: 'json',
                        error: function(result){
                            alert("Обов'язково вкажіть розмір товару")
                        },
                        success: function(result) {
                            changeCartitemQuantityOnNavbar(new_cart_item_quantity);
                            setTimeout(successAddToCartMessage, 50);
                        }
                    });
                }
            }
        });
    })
});
