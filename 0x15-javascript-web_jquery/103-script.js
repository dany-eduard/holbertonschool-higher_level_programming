$(document).ready(function () {
  $('DOMContentLoaded', function () {
    const translate = function () {
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val();
      $.getJSON(url, function (data) {
        $('#hello').text(data.hello);
      });
    };
    $('#language_code').keypress(function (event) {
      const keycode = event.keyCode ? event.keyCode : event.which;
      if (keycode == '13') {
        translate();
      }
    });

    $('#btn_translate').click(function () {
      translate();
    });
  });
});
