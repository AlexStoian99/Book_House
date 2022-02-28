$(function (){
   $("#register-form").submit(function (event){
       event.preventDefault();
        console.log(event.target);
        console.log(event.currentTarget);
        console.log(event.relatedTarget);
       let $target = $(event.target);
        console.log($target.data('bookId'));
        $.post({
            url:  $target.attr('action'),
            data: $target.serialize()
        }).done(
            function(data){
                console.log(data);
                if (data.status === 'OK'){
                    // console.log("Succes! Message: %s", data.message);
                    // $target.closest('div.card').remove();
                    var modal = bootstrap.Modal.getInstance($('#register-modal')[0]);
                    modal.hide();
                    location.reload();
                }
                else {
                    console.log("Error! Message: %s", data.message);
                    $('div.alert').text(data.message).addClass('alert-danger').removeClass('d-none');

                }
            }
        )
});
    $("#modal-book").on('show.bs.modal',function (){
        $.get({url: $("#modal-book").data("url")
        }).done(
            function(data){
                $("#modal-book div.modal-body").html(data);
                $("#book-form").submit(books_submit);
            }
        )
    });
    $("#modal-author").on('show.bs.modal',function (){
        $.get({url: $("#modal-author").data("url")
        }).done(
            function(data){
                $("#modal-author div.modal-body").html(data);
                $("#author-form").submit(author_submit);
            }
        )
    });
    $("#modal-library").on('show.bs.modal',function (){
        $.get({url: $("#modal-library").data("url")
        }).done(
            function(data){
                $("#modal-library div.modal-body").html(data);
                $("#library-form").submit(library_submit);
            }
        )
    });



});
function books_submit(event){
       event.preventDefault();
       let $target = $("#book-form");
       var formData = new FormData($target[0]);
        $.post({
            url:  $target.attr('action'),
            data: formData,
            async: false,
            cache: false,
            contentType: false,
            processData: false,
        }).done(
            function(data){
                console.log(data);
                if (data.status === 'OK'){

                    // console.log("Succes! Message: %s", data.message);
                    // $target.closest('div.card').remove();
                    var modal = bootstrap.Modal.getInstance($('#modal-book')[0]);
                    modal.hide();
                    location.reload();

                }
                else {
                    console.log("Error! Message: %s", data.message);
                    $('div.alert').text(data.message).addClass('alert-danger').removeClass('d-none');

                }
            }
        )
}
function author_submit(event){
       event.preventDefault();
       let $target = $("#author-form");
       var formData = new FormData($target[0]);
        $.post({
            url:  $target.attr('action'),
            data: formData,
            async: false,
            cache: false,
            contentType: false,
            processData: false,
        }).done(
            function(data){
                console.log(data);
                if (data.status === 'OK'){

                    // console.log("Succes! Message: %s", data.message);
                    // $target.closest('div.card').remove();
                    var modal = bootstrap.Modal.getInstance($('#modal-author')[0]);
                    modal.hide();
                    location.reload();

                }
                else {
                    console.log("Error! Message: %s", data.message);
                    $('div.alert').text(data.message).addClass('alert-danger').removeClass('d-none');

                }
            }
        )
}
function library_submit(event){
       event.preventDefault();
       let $target = $("#library-form");
       var formData = new FormData($target[0]);
        $.post({
            url:  $target.attr('action'),
            data: formData,
            async: false,
            cache: false,
            contentType: false,
            processData: false,
        }).done(
            function(data){
                console.log(data);
                if (data.status === 'OK'){

                    // console.log("Succes! Message: %s", data.message);
                    // $target.closest('div.card').remove();
                    var modal = bootstrap.Modal.getInstance($('#modal-library')[0]);
                    modal.hide();
                    location.reload();

                }
                else {
                    console.log("Error! Message: %s", data.message);
                    $('div.alert').text(data.message).addClass('alert-danger').removeClass('d-none');

                }
            }
        )
}
