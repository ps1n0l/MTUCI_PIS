$(document).ready(function(){
    $('.one-post').hover(
        function(event) {
            $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0.1'}, 300);
        },
        function(event) {
            $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'}, 300);
        }
    );
});

$(document).ready(function(){
    $('.logo').hover(
        function() {
            var $this = $(this);
            var origWidth = $this.width();
            var origHeight = $this.height();
            $this.data('origWidth', origWidth);
            $this.data('origHeight', origHeight);

            var newWidth = origWidth + 20;
            var newHeight = origHeight * (newWidth / origWidth);

            $this.css({
                width: newWidth + 'px',
                height: newHeight + 'px'
            });
        },
        function() {
            var $this = $(this);
            $this.css({
                width: $this.data('origWidth') + 'px',
                height: $this.data('origHeight') + 'px'
            });
        }
    );
});