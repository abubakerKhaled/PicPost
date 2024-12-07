(function() {
    const siteUrl = '//172.0.0.1:8000/';
    const styleUrl = siteUrl + 'static/css/bookmarklet.css';
    const minWidth = 250;
    const minHeight = 250;

    // load the css
    function loadCSS() {
        let head = document.getElementsByTagName('head')[0];
        let link = document.createElement('link');
        link.rel = 'stylesheet';
        link.type = 'text/css';
        link.href = styleUrl + '?r=' + Math.floor(Math.random()*9999999999999999);
        head.appendChild(link);
    }

    // load HTML
    function injectBookmarkletHTML() {
        let body = document.getElementsByTagName('body')[0];
        let boxHtml = `
            <div class="bookmarklet-container" id="bookmarklet">
            <h1 class="bookmarklet-header">
                Bookmark Images
                <a href="#" class="bookmarklet-close">&times;</a>
            </h1>
            <div class="bookmarklet-images">
            </div>
            </div>`;
        body.insertAdjacentHTML('beforeend', boxHtml);
    }

    // Expose bookmarkletLaunch globally
    window.bookmarkletLaunch = function() {
        // Ensure the bookmarklet container exists
        if (!document.getElementById('bookmarklet')) {
            injectBookmarkletHTML();
        }

        let bookmarklet = document.getElementById('bookmarklet');
        let imagesFound = bookmarklet.querySelector('.bookmarklet-images');

        // clear images found
        imagesFound.innerHTML = '';
        
        // display bookmarklet 
        bookmarklet.style.display = 'block';

        // close event
        bookmarklet.querySelector('.bookmarklet-close').addEventListener('click', function(e) {
            e.preventDefault();
            bookmarklet.style.display = 'none';
        }); 

        // find images in the DOM with minimum dimensions
        let images = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"]');
        let validImages = Array.from(images).filter(image => 
            image.naturalWidth >= minWidth && image.naturalHeight >= minHeight
        );

        if (validImages.length === 0) {
            imagesFound.innerHTML = '<p>No suitable images found on this page.</p>';
            return;
        }

        // Add filtered images
        validImages.forEach(image => {
            let imageFound = document.createElement('img');
            imageFound.src = image.src;
            imageFound.classList.add('image-thumbnail');
            imagesFound.appendChild(imageFound);
        });

        // select image event
        imagesFound.querySelectorAll('img').forEach(image => {
            image.addEventListener('click', function(event) {
                let imageSelected = event.target;
                bookmarklet.style.display = 'none';
                window.open(
                    siteUrl + 'images/create/?url=' + 
                    encodeURIComponent(imageSelected.src) + 
                    '&title=' + 
                    encodeURIComponent(document.title),
                    '_blank'
                );
            });
        });
    };

    // Prepare the bookmarklet when script loads
    function initBookmarklet() {
        loadCSS();
    }

    // Initialize
    initBookmarklet();
})();