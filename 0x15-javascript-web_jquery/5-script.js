#!/usr/bin/node
const $ = window.$;
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
