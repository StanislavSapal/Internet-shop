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

    $('button[class*=add_to_cart_button]').click(function() {
        let url = '/api/v1/cartitems/';
        let minus_plus_add_div = $(this).parent();
        let product_info_and_options_div = minus_plus_add_div.parent();
        let size_div = product_info_and_options_div.find('div.size_div');
        size = size_div.attr('value');
        let product_id = minus_plus_add_div.attr('id');
        let product_quantity_input = minus_plus_add_div.find('input.quantity_input');
        let product_quantity = Number(product_quantity_input.attr('value'));
        let data = JSON.stringify({"product": product_id,
                                   "quantity": product_quantity,
                                   "size": size});

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
                alert(result)
            },
            success: function(result) {
                alert('Товар додано до кошика')
            }
        });
    });
});
