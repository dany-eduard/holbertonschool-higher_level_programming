document.addEventListener('DOMContentLoaded', () => {
  const newElement = '<li>Item</li>';
  $('#add_item').on('click', () => {
    $('UL.my_list').append(newElement);
  });
  $('#remove_item').on('click', () => {
    $('UL.my_list li').last().remove();
  });
  $('#clear_list').on('click', () => {
    $('UL.my_list').empty();
  });
});
