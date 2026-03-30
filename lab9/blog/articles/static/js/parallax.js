$(document).ready(function(){

    var yPosition;
    var scrolled = 0;

    // получаем все элементы параллакса
    var $parallaxElements = $('.icons-for-parallax img');

    $(window).scroll(function(){

        // сколько прокручено
        scrolled = $(window).scrollTop();

        for (var i = 0; i < $parallaxElements.length; i++){

            // расчет смещения
            yPosition = scrolled * 0.15 * (i + 1);

            // применяем координаты
            $parallaxElements.eq(i).css({
                top: yPosition + 'px'
            });
        }

    });

});

$(document).ready(function(){

    var $logo = $('.logo');

    $(window).scroll(function(){

        var scrolled = $(window).scrollTop();

        // логотип двигается медленнее (дальний слой)
        var logoPosition = scrolled * 0.05;

        $logo.css({
            top: logoPosition + 'px',
            position: 'relative'
        });

    });

});