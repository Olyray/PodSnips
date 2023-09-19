$(document).ready(function(){
  $('#podcast-name').on('input', function(){
      let query = $(this).val();
      if(query.length > 2) {
          $.ajax({
              url: '/api/search_podcast',
              method: 'GET',
              data: { query: query },
              success: function(response) {
                  let suggestions = response.results.map(podcast => 
                      `<div class="suggestion-item" data-id="${podcast.id}" data-name="${podcast.title_original}">${podcast.title_original}</div>`
                  ).join('');
                  $('#suggestions').html(suggestions);
              }
          });
      } else {
          $('#suggestions').html('');
      }
  });

  $(document).on('click', '.suggestion-item', function(){
      let podcastId = $(this).data('id');
      let podcastName = $(this).data('name');
      window.location.href = `/podcast_details?podcast_id=${podcastId}&podcast_name=${podcastName}`;
  });
});
