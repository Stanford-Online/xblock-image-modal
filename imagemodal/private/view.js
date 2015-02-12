function ImageModalView(runtime, element) {
    'use strict';

    var $ = window.jQuery;
    var $element = $(element);
    var draggie;
    var KEY_ENTER = 13;
    var KEY_ESCAPE = 27;
    var Draggabilly = window.Draggabilly;
    var body = $('BODY');
    var anchor = $element.find('A');
    var curtain = $element.find('.curtain');
    var image = curtain.find('IMG');
    var mask = curtain.find('.mask');
    var wrapper = $element.find('.wrapper');
    var buttonFullScreen = wrapper.find('BUTTON.fullscreen');
    var buttonZoom = curtain.find('BUTTON.zoom');
    var buttonZoomText = buttonZoom.find('SPAN');
    var buttonZoomIcon = buttonZoom.find('I');

    function preventDefault() {
        return false;
    }

    function zoomIn() {
        var maskLeft;
        var maskTop;
        var maskWidth;
        var maskHeight;
        var imageWidth;
        var imageHeight;

        buttonZoomText.text('Zoom Out');
        buttonZoomIcon.removeClass('icon-zoom-in');
        buttonZoomIcon.addClass('icon-zoom-out');
        image.off('.imagemodal');
        image.on('click.imagemodal_zoomin', preventDefault);
        image.addClass('zoomed');
        imageHeight = image.height();
        imageWidth = image.width();
        maskLeft = imageWidth - mask.width();
        maskTop = imageHeight - mask.height();
        maskWidth = imageWidth + maskLeft;
        maskHeight = imageHeight + maskTop;
        draggie = draggie || new Draggabilly(
            image[0],
            {
                containment: true
            }
        );

        if (maskHeight > 0 && maskWidth > 0) {
            image.parent().css({
                left: -maskLeft,
                top: -maskTop,
                width: maskWidth,
                height: maskHeight
            });
            image.css({
                top: maskTop / 2,
                left: maskLeft / 2
            });
            draggie.enable();
        } else {
            draggie.enable();
        }
    }

    function zoomOut() {
        buttonZoomText.text('Zoom In');
        buttonZoomIcon.removeClass('icon-zoom-out');
        buttonZoomIcon.addClass('icon-zoom-in');
        image.off('.imagemodal');
        image.on('click.imagemodal_zoomout', openModal);
        image.removeClass('zoomed');
        image.parent().css({
            left: 0,
            top: 0,
            width: '100%',
            height: '100%'
        });
        image.css({
            left: 0,
            top: 0
        });
        if (draggie) {
            draggie.disable();
            draggie = null;
        }
    }

    function toggleZoom() {
        var isZoomed = image.hasClass('zoomed');
        if (isZoomed) {
            zoomOut();
        } else {
            zoomIn();
        }
        return false;
    }

    function closeModal() {
        body.css('overflow', '');
        curtain.hide();
        body.off('.imagemodal');
        buttonZoom.off('.imagemodal');
        curtain.off('.imagemodal');
        image.off('.imagemodal');
        return false;
    }

    function openModal(event) {
        curtain.show();
        body.css('overflow', 'hidden');
        body.on('keyup.imagemodal', function (event) {
            if (event.which === KEY_ESCAPE) {
                return closeModal();
            }
            if (event.which === KEY_ENTER) {
                return toggleZoom();
            }
        });
        buttonZoom.on('click.imagemodal', toggleZoom);
        curtain.on('click.imagemodal', closeModal);
        image.on('click.imagemodal', toggleZoom);
        return false;
    }

    runtime = runtime || {};
    closeModal();
    if ($element.attr('data-runtime-class') === 'PreviewRuntime') {
        anchor.on('click.imagemodal', preventDefault);
    } else {
        anchor.on('click.imagemodal', openModal);
        buttonFullScreen.on('click.imagemodal', openModal);
    }
}
