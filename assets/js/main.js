/**
 * Main JS file for theme behaviours
 */

// Responsive video embeds
var videoEmbeds = [
  'iframe[src*="youtube.com"]',
  'iframe[src*="vimeo.com"]'
];
reframe(videoEmbeds.join(','));

// Header background image
var header = document.querySelector('#masthead');
if (header) {
  headerBg = document.querySelector('#header-bg');
  if (headerBg) {
    imagesLoaded(headerBg, { background: true }, function () {
      header.classList.add('bg--loaded');
    });
  } else {
    header.classList.add('bg--loaded');
  }
}

// Back to top
document.querySelector('#to-top').addEventListener('click', function (e) {
  e.preventDefault();
  document.querySelector('#page').scrollIntoView({ behavior: 'smooth' });
});

// Image animation when gets visible
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      return;
    }
    entry.target.classList.remove('visible');
  });
});
document.querySelectorAll('article p > img').forEach(el => observer.observe(el));
