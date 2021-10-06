var elements = document.getElementsByClassName('button');
for(var i = 0 ; i < elements.length; i++){
    elements[i].addEventListener("click", function(){
        console.log(this.classList)
        if(this.classList.contains('active')){
            this.classList.remove('active');
        }else{
            this.classList.add('active');
        }
    })
}


$('.heart').click(function(){
    var postid = $(this).attr("id");
    $.ajax({
        type:"GET",
        url: "likepost",
        data:{
                 post_id: postid
        },
        success: function( data ) 
        {
            $( '#like'+ postid ).remove();
            $( '#message' ).text(data);
        }
    })
})