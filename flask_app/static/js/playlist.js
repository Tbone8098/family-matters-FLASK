var allSongEditBtns = document.querySelectorAll('.song-edit-btn')

if (allSongEditBtns.length > 0){
    for (let btn of allSongEditBtns) {
        btn.addEventListener('click', async function(){
            let modal = document.querySelector("[modal_name='edit__song']")
            let song_id = btn.getAttribute('song_id')
            let data = await apiGetInfo(song_id, 'song')
            let playlist_id = btn.getAttribute('playlist_id')
            console.log(playlist_id);
            
            content = modal.firstElementChild.children[1]

            content.innerHTML = `
            <form action="/admin/song/${song_id}/update" method="post">
                <input type="hidden" name="playlist_id" id="playlist_id" value="${playlist_id}">
                <div>
                    <label for="name">Name</label>
                    <input class="form-control" type="text" name="name" id="name" value="${data['data']['name']}">
                </div>
                <div class="mb-3">
                    <label for="artist">Artist</label>
                    <input class="form-control" type="text" name="artist" id="artist" value="${data['data']['artist']}">
                </div>
                <div class="mb-3">
                    <label for="link">YouTube Link</label>
                    <input class="form-control" type="text" name="link" id="link" value="${data['data']['link']}">
                </div>
                <div class="w-100">
                    <button class="btn btn-success w-100">Update Song</button>
                </div>
            </form>
            `
        })
    }
}