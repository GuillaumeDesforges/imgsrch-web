$('progress').hide();

$("#submit").click(function (e) {
    e.preventDefault();
    $('progress').show();
    $.ajax({
        // Your server script to process the upload
        url: '/search',
        type: 'POST',
    
        // Form data
        data: new FormData($('form')[0]),
    
        // Tell jQuery not to process data or worry about content-type
        // You *must* include these options!
        cache: false,
        contentType: false,
        processData: false,
    
        // Custom XMLHttpRequest
        xhr: function() {
            var myXhr = $.ajaxSettings.xhr();
            if (myXhr.upload) {
                // For handling the progress of the upload
                myXhr.upload.addEventListener('progress', function(e) {
                    if (e.lengthComputable) {
                        $('progress').attr({
                            value: e.loaded,
                            max: e.total,
                        });
                    }
                } , false);
            }
            return myXhr;
        },
        success: function(data) {
            var results = $('#results');
            results.empty();
            var scores = data.scores;
            console.log(scores);
            for(var i = 0; i < scores.length; i++) {
                var image = scores[i];
                console.log(image);
                var imagePath = image.path;
                // var imageScore = image.score;
                results.append('<div class="col-3"><a href="'+ imagePath +'"><img class="img-fluid" src="'+ imagePath +'" /></a></div>');
            }
        },
        complete: function() {
            $('progress').hide();
        }
    });
});
