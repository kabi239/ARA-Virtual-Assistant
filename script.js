$(document).ready(function () {
  $(document).ready(function () {

    $.line(0, $('.txtLine').first());


    $(window).resize(function () {
      $('.txtLine').css({ 'margin-left': Math.ceil($('body').outerWidth() / 5) });
    });
  });


  $.line = function (i, line) {
    $(line).delay(i * 1000).queue(function (n) {
      var shw = $(line).find('.show');
      var hid = $(line).find('.hide');
      var txt = $(hid).text();
      if ($(shw).hasClass('stretch')) {
        $(shw).parents('.speech').css({ 'height': 40 });
      }
      $(shw).prepend('<div></div>');
      for (var ii = 0; ii < txt.length; ii++) {

        $.letter(ii, line, shw, hid, txt, i);
      }

      n();

    });
  }

  $.letter = function (ii, line, shw, hid, txt, i) {
    $(line).delay(50).queue(function (n) {
      var char = txt[ii];
      $(shw).html($(shw).html() + char);
      n();

      if ($(shw).hasClass('stretch')) {

        if ($(shw).outerWidth() > $(shw).parents('.speech').outerWidth() - 20) {
          $(shw).parents('.speech').css({ 'width': $(shw).parents('.speech').outerWidth() + 1 });
        }
        if ($(shw).outerHeight() > $(shw).parents('.speech').outerHeight() - 20) {
          console.log($(shw).parents('.speech').outerHeight() + 10);
          $(shw).parents('.speech').css({ 'height': $(shw).parents('.speech').outerHeight() + 1 });
        }
        else{

        }

      } else {
        if ($(shw).outerHeight() > $(shw).parents('.speech').outerHeight() - 20) {
          $(shw).parents('.speech').css({ 'height': $(shw).parents('.speech').outerHeight() + 1 });
        }
      }


      if (ii == (txt.length - 1)) {

        $(line).delay(10).queue(function (n) {
          $(shw).css({ 'border-bottom': '', 'box-shadow': '' });
          $(shw).find('div').remove();
          var incr = i++;
          $.line(incr, $(line).next());
          n();
        });
      }
    });
  }
});