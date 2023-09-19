$(document).ready(function(){
  let params = new URLSearchParams(window.location.search);
  let podcastId = params.get('podcast_id');
  let podcastName = params.get('podcast_name');

  $.ajax({
      url: `/api/podcast_details/${podcastId}`,
      method: 'GET',
      success: function(response) {
          let details = response.details;
          let episodes = details.episodes.map(episode => 
              `<div class="episode-item" data-id="${episode.id}" data-name="${episode.title}">
                  <h5>${episode.title}</h5>
              </div>`
          ).join('');
          console.log(details);
          $('#podcast-details').html(`
              <h2>${details.title}</h2>
              <p>${details.description}</p>
              <h3>Episodes:</h3>
              <div>${episodes}</div>
          `);
      }
  });
});
