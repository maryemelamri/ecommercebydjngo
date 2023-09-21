$("#add-to-card-btn").on("click", function () {
  let product_title = $(".product-title").val();
  let product_id = $(".product-id").val();
  let product_price = $(".product-price").val();

  $.ajax({
    url: "/add-to-card",
    data: {
      id: product_id,
      title: product_title,
      price: product_price,
    },
    dataType: "json",
    success: function () {
      this_val.html("item add to card");
    },
  });
});
