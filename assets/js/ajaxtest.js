function like(id) {
    var element = document.getElementById('like-icon-' + id);
    var count = document.getElementById('like-count-' + id);
    
    if (!element || !count) {
        console.error('Could not find like elements for post:', id);
        return;
    }
    
    $.get(`/posts/like/${id}`)
        .done(function(response) {
            console.log('Response received:', response);
            
            if (response['response'] === "liked") {
                element.className = "fa fa-heart";
                count.innerText = response['count'];
            } else if (response['response'] === "unliked") {
                element.className = "fa fa-heart-o";
                count.innerText = response['count'];
            } else if (response['response'] === "error") {
                alert(response['message']);
            }
        })
        .fail(function(xhr, status, error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
}