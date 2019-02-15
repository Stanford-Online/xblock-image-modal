/* eslint-disable no-unused-vars */
/**
 * Initialize the ImageModal student view
 * @param {Object} runtime - The XBlock JS Runtime
 * @param {Object} element - The containing DOM element for this instance of the XBlock
 * @returns {undefined} nothing
 */
function ImageModalView(runtime, element) {
    /* eslint-enable no-unused-vars */
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

    /**
     * Prevent the default event from bubbling up
     * @returns {boolean} False to stop event bubbling
     */
    function preventDefault() {
        return false;
    }

    /**
     * Zoom in on the image
     * @returns {undefined} nothing
     */
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
                containment: true,
            }
        );

        if (maskHeight > 0 && maskWidth > 0) {
            image.parent().css({
                left: -maskLeft,
                top: -maskTop,
                width: maskWidth,
                height: maskHeight,
            });
            image.css({
                top: maskTop / 2,
                left: maskLeft / 2,
            });
            draggie.enable();
        } else {
            draggie.enable();
        }
    }

    /**
     * Close the image modal
     * @returns {boolean} False to stop event bubbling
     */
    function closeModal() {
        body.css('overflow', '');
        curtain.hide();
        body.off('.imagemodal');
        buttonZoom.off('.imagemodal');
        curtain.off('.imagemodal');
        image.off('.imagemodal');
        return false;
    }

    /**
     * Zoom out from the image
     * @returns {undefined} nothing
     */
    function zoomOut() {
        buttonZoomText.text('Zoom In');
        buttonZoomIcon.removeClass('icon-zoom-out');
        buttonZoomIcon.addClass('icon-zoom-in');
        image.off('.imagemodal');
        // eslint-disable-next-line no-use-before-define
        image.on('click.imagemodal_zoomout', openModal);
        image.removeClass('zoomed');
        image.parent().css({
            left: 0,
            top: 0,
            width: '100%',
            height: '100%',
        });
        image.css({
            left: 0,
            top: 0,
        });
        if (draggie) {
            draggie.disable();
            draggie = null;
        }
    }

    /**
     * Toggle the zoom state in and out
     * @returns {boolean} False to stop event bubbling
     */
    function toggleZoom() {
        var isZoomed = image.hasClass('zoomed');
        if (isZoomed) {
            zoomOut();
        } else {
            zoomIn();
        }
        return false;
    }

    /**
     * Open the image modal div
     * @returns {boolean} False to stop event bubbling
     */
    function openModal() {
        curtain.show();
        body.css('overflow', 'hidden');
        body.on('keyup.imagemodal', function(event) {
            if (event.which === KEY_ESCAPE) {
                return closeModal();
            }
            if (event.which === KEY_ENTER) {
                return toggleZoom();
            }
            return true;
        });
        buttonZoom.on('click.imagemodal', toggleZoom);
        curtain.on('click.imagemodal', closeModal);
        image.on('click.imagemodal', toggleZoom);
        return false;
    }

    closeModal();
    if ($element.attr('data-runtime-class') === 'PreviewRuntime') {
        anchor.on('click.imagemodal', preventDefault);
    } else {
        anchor.on('click.imagemodal', openModal);
        buttonFullScreen.on('click.imagemodal', openModal);
    }
}
