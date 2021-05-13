document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://www.fourtonfish.com/hellosalut/';
  $('#btn_translate').on('click', () => {
    const hi = `${url}?lang=` + $('#language_code').val();
    $.get(hi, (data) => {
      $('#hello').text(data.hello);
    });
  });
});
