(function() {
    'use strict';

    [].forEach.call(document.querySelectorAll('tbody tr'), function(i) {
        var link = i.attributes['data-link'].nodeValue;
        i.onclick = function(e) {
            var win = window.open(link, '_blank');
            win.focus();
        };
        return true;
    });
})();
