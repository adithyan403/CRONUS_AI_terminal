document.addEventListener('DOMContentLoaded', () => {
    const introOverlay = document.getElementById('intro-overlay');
    const introVideo = document.getElementById('intro-video');
    const bgVideo = document.getElementById('bg-video');
    const startBtn = document.getElementById('start-intro');
    const skipBtn = document.getElementById('skip-intro');
    const appContent = document.getElementById('app-content');

    // Attempt to pause video initially to wait for user interaction
    introVideo.pause();

    const finishIntro = () => {
        // Fade out overlay
        introOverlay.style.transition = 'opacity 0.8s ease';
        introOverlay.style.opacity = '0';

        // Start background video (muted, loop)
        bgVideo.play().catch(e => console.log("BG Video autoplay blocked", e));

        setTimeout(() => {
            introOverlay.style.display = 'none';
            appContent.classList.remove('hidden');
            appContent.classList.add('visible');
            introVideo.pause();
        }, 800);
    };

    // User clicks "INITIALIZE SYSTEM" - Play with sound
    startBtn.addEventListener('click', () => {
        introVideo.muted = false; // Enable sound
        introVideo.currentTime = 0;
        introVideo.play().then(() => {
            // Hide buttons to show clean video
            document.querySelector('.intro-controls').style.display = 'none';
        }).catch(e => {
            console.error("Video play failed", e);
            finishIntro();
        });
    });

    // User clicks "SKIP"
    skipBtn.addEventListener('click', finishIntro);

    // When intro ends, transition
    introVideo.addEventListener('ended', finishIntro);

    // Dynamic Logo Extraction (Star Tower Frame)
    const extractLogo = () => {
        const video = document.createElement('video');
        video.src = 'assets/intro.mp4';
        video.muted = true;
        video.width = 300; // Work at reasonable resolution
        video.height = 168;

        // Wait for metadata to get duration
        video.addEventListener('loadedmetadata', () => {
            // Seek to near end (duration - 0.5s)
            video.currentTime = Math.max(0, video.duration - 0.5);
        });

        video.addEventListener('seeked', () => {
            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

            const logoImg = document.getElementById('cronus-logo');
            if (logoImg) {
                logoImg.src = canvas.toDataURL('image/png');
                logoImg.style.display = 'block';
            }
            // Cleanup intentionally omitted as video element is not in DOM
        });
    };

    // Start extraction
    extractLogo();

    // --- Download Modal Logic ---
    const downloadModal = document.getElementById('download-modal');
    const downloadBtns = document.querySelectorAll('a[href="#"]'); // Selects "DOWNLOAD BETA" nav link
    const closeModalBtn = document.getElementById('close-modal');
    const termsCheck = document.getElementById('terms-check');
    const confirmDownloadBtn = document.getElementById('confirm-download-btn');

    // Select the specific "DOWNLOAD BETA" button if generic selector is risky
    // Based on HTML structure, the generic selector might grab others. 
    // Let's refine the selector or add an ID to the button in HTML? 
    // HTML: <a href="#" class="btn-primary-small">DOWNLOAD BETA</a>
    // I will iterate and find the one that says "DOWNLOAD BETA" or add event listener to all matching buttons

    const triggerDownloadModal = (e) => {
        if (e.target.textContent && e.target.textContent.includes('DOWNLOAD BETA')) {
            e.preventDefault();
            downloadModal.classList.remove('hidden');
        }
    };

    // Attach to all relevant buttons
    document.querySelectorAll('.btn-primary-small').forEach(btn => {
        btn.addEventListener('click', triggerDownloadModal);
    });

    closeModalBtn.addEventListener('click', () => {
        downloadModal.classList.add('hidden');
    });

    // Close on click outside
    downloadModal.addEventListener('click', (e) => {
        if (e.target === downloadModal) {
            downloadModal.classList.add('hidden');
        }
    });

    // Terms & Conditions Checkbox
    termsCheck.addEventListener('change', () => {
        if (termsCheck.checked) {
            confirmDownloadBtn.classList.remove('disabled');
        } else {
            confirmDownloadBtn.classList.add('disabled');
        }
    });

    // Handle actual download click
    confirmDownloadBtn.addEventListener('click', () => {
        // Optional: Close modal after delay
        setTimeout(() => {
            downloadModal.classList.add('hidden');
        }, 1500);
    });
});
