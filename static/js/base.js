//   David Alvarado    Cis 218    11/05/24

$(document).ready(function () {
    $('.like_button').click(function (event) {
        // Get required data
        let target = $(event.currentTarget);
        let twit_id = target.data('id'); // Get the Twit ID
        let twit_action = target.data('action'); // Like or unlike
        let twit_like_url = target.data('like_url'); // The URL for the like/unlike action

        // Get icon and count elements
        let like_icon = target.find('.like_icon'); // Optional: if you have an icon
        let like_count = target.find('.like_count'); // Like count element

        // Make AJAX request to like/unlike URL
        $.ajax({
            url: twit_like_url,
            type: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token
            },
            data: {
                action: twit_action, // The current action (like/unlike)
            },
        }).done(function (data) {
            // Check if the request was successful
            if (data.liked !== undefined) {
                if (data.liked) {
                    // Update elements to reflect "liked"
                    target.removeClass('btn-outline-secondary').addClass('btn-secondary');
                    if (like_icon) {
                        like_icon.removeClass('bi-hand-thumbs-up').addClass('bi-hand-thumbs-up-fill');
                    }
                    like_count.html(Number(like_count.html()) + 1);
                    target.data('action', 'unlike'); // Change the action to 'unlike'
                } else {
                    // Update elements to reflect "unliked"
                    target.removeClass('btn-secondary').addClass('btn-outline-secondary');
                    if (like_icon) {
                        like_icon.removeClass('bi-hand-thumbs-up-fill').addClass('bi-hand-thumbs-up');
                    }
                    like_count.html(Number(like_count.html()) - 1);
                    target.data('action', 'like'); // Change the action to 'like'
                }
            }
        }).fail(function () {
            alert('An error occurred while processing your request. Please try again.');
        });
    });

    // Helper function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
