(function (jq) {
    jq('.multi-menu .title').click(function () {
        $(this).next().toggleClass('hide');
        console.log($(this).next().html())
    });
})(jQuery);