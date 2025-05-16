// Startet Autoplac auf index.html
const videos = [
    "/static/videos/3264304-hd_1280_720_30fps.mp4",
    "/static/videos/3569293-uhd_3840_2160_24fps.mp4",
    "/static/videos/5816530-hd_1920_1080_25fps.mp4",
    "/static/videos/5928849-hd_1920_1080_25fps.mp4",
    "/static/videos/4667121-uhd_4096_2160_25fps.mp4",
    "/static/videos/4686894-uhd_4096_2160_25fps.mp4",
    "/static/videos/4765778-hd_1920_1080_25fps.mp4"
];
let currentVideoIndex = 0;
const videoPlayer = document.getElementById("videoPlayer");
function playNextVideo() {
    currentVideoIndex = (currentVideoIndex + 1) % videos.length;
    videoPlayer.src = videos[currentVideoIndex];
    videoPlayer.play();}
videoPlayer.src = videos[currentVideoIndex];
videoPlayer.play();
videoPlayer.addEventListener("ended", playNextVideo);

// Leert alle Eingabefelder nach Absenden
document.addEventListener("DOMContentLoaded", function () {
const forms = document.querySelectorAll("form");
forms.forEach(form => {
form.addEventListener("submit", function () {
setTimeout(() => {
form.reset();
}, 100);
});
});
});
