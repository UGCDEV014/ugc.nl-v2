// Dropdown functionality
document.addEventListener('DOMContentLoaded', function() {
  // Dropdown toggle
  const dropdowns = document.querySelectorAll('.dropdown');
  dropdowns.forEach(dropdown => {
    const toggle = dropdown.querySelector('.dropdown-toggle');
    if (toggle) {
      toggle.addEventListener('click', function(e) {
        e.stopPropagation();
        dropdown.classList.toggle('open');
      });
    }
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', function() {
    dropdowns.forEach(dropdown => {
      dropdown.classList.remove('open');
    });
  });

  // Header dropdown functionality
  const headerDropdowns = document.querySelectorAll('.header-dropdown');
  
  headerDropdowns.forEach(dropdown => {
    const toggle = dropdown.querySelector('.header-dropdown-toggle');
    const headerContainer = dropdown.closest('.header-container');
    const menu = headerContainer?.querySelector('.header-dropdown-menu');
    
    if (toggle && menu) {
      let hoverTimeout;
      
      // Click functionality
      toggle.addEventListener('click', function(e) {
        e.stopPropagation();
        dropdown.classList.toggle('open');
      });
      
      // Hover functionality - open on hover over dropdown
      dropdown.addEventListener('mouseenter', function() {
        clearTimeout(hoverTimeout);
        dropdown.classList.add('open');
      });
      
      // Keep open when hovering over dropdown menu
      menu.addEventListener('mouseenter', function() {
        clearTimeout(hoverTimeout);
        dropdown.classList.add('open');
      });
      
      // Close when leaving dropdown area
      dropdown.addEventListener('mouseleave', function(e) {
        // Check if we're moving to the menu
        const relatedTarget = e.relatedTarget;
        if (relatedTarget && (menu.contains(relatedTarget) || menu === relatedTarget)) {
          return; // Don't close, we're moving to the menu
        }
        // Small delay to allow smooth transition to menu
        hoverTimeout = setTimeout(() => {
          dropdown.classList.remove('open');
        }, 100);
      });
      
      // Close when leaving menu area
      menu.addEventListener('mouseleave', function(e) {
        const relatedTarget = e.relatedTarget;
        if (relatedTarget && (dropdown.contains(relatedTarget) || dropdown === relatedTarget)) {
          return; // Don't close, we're moving back to dropdown
        }
        hoverTimeout = setTimeout(() => {
          dropdown.classList.remove('open');
        }, 100);
      });
    }
  });

  // Close header dropdown when clicking outside
  document.addEventListener('click', function(e) {
    headerDropdowns.forEach(dropdown => {
      if (!dropdown.contains(e.target)) {
        const headerContainer = dropdown.closest('.header-container');
        const menu = headerContainer?.querySelector('.header-dropdown-menu');
        if (!menu || !menu.contains(e.target)) {
          dropdown.classList.remove('open');
        }
      }
    });
  });

  // FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  let currentOpenItem = null;
  
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    if (question) {
      question.addEventListener('click', function() {
        const isOpen = item.classList.contains('open');
        
        // Close currently open item if different
        if (currentOpenItem && currentOpenItem !== item) {
          currentOpenItem.classList.remove('open');
        }
        
        // Toggle clicked item
        if (isOpen) {
          item.classList.remove('open');
          currentOpenItem = null;
        } else {
          item.classList.add('open');
          currentOpenItem = item;
        }
      });
    }
  });

  // FAQ Tabs
  const faqTabs = document.querySelectorAll('.faq-tab');
  const faqTabPanels = document.querySelectorAll('.faq-tab-panel');
  
  faqTabs.forEach(tab => {
    tab.addEventListener('click', function() {
      const target = this.getAttribute('data-target');
      
      // Remove active from all tabs and panels
      faqTabs.forEach(t => t.classList.remove('active'));
      faqTabPanels.forEach(p => p.classList.remove('active'));
      
      // Add active to clicked tab and corresponding panel
      this.classList.add('active');
      if (target) {
        const panel = document.querySelector(`.faq-tab-panel[data-panel="${target}"]`);
        if (panel) {
          panel.classList.add('active');
        }
      }
    });
  });

  // Number animation for hero stats
  function animateNumber(element, target, duration = 2000) {
    const start = 0;
    const increment = target / (duration / 16); // 60fps
    let current = start;
    
    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      const formatted = Math.floor(current).toLocaleString('en-US');
      element.textContent = formatted + '+';
    }, 16);
  }

  // Animate numbers when hero section is visible
  const heroSection = document.querySelector('.hero-section');
  if (heroSection) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const creatorsCount = document.getElementById('creators-count');
          const merkenCount = document.getElementById('merken-count');
          
          if (creatorsCount && !creatorsCount.classList.contains('animated')) {
            creatorsCount.classList.add('animated');
            animateNumber(creatorsCount, 1500);
          }
          
          if (merkenCount && !merkenCount.classList.contains('animated')) {
            merkenCount.classList.add('animated');
            animateNumber(merkenCount, 2000);
          }
          
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    observer.observe(heroSection);
  }

  // Video play/pause functionality for creator cards
  const creatorCards = document.querySelectorAll('.creator-card');
  creatorCards.forEach(card => {
    const video = card.querySelector('.creator-video');
    const overlay = card.querySelector('.play-overlay');
    const muteBtn = card.querySelector('.creator-mute-btn');
    const muteIcon = card.querySelector('.creator-mute-icon');
    
    if (video && overlay) {
      // Click on overlay to play/pause
      overlay.addEventListener('click', function(e) {
        e.stopPropagation();
        if (video.paused) {
          video.play();
          overlay.textContent = '⏸';
          overlay.classList.add('playing');
        } else {
          video.pause();
          overlay.textContent = '▶';
          overlay.classList.remove('playing');
        }
      });

      // Click on video to play/pause
      video.addEventListener('click', function(e) {
        e.stopPropagation();
        if (video.paused) {
          video.play();
          overlay.textContent = '⏸';
          overlay.classList.add('playing');
        } else {
          video.pause();
          overlay.textContent = '▶';
          overlay.classList.remove('playing');
        }
      });

      // Mute/unmute button functionality
      if (muteBtn && muteIcon) {
        muteBtn.addEventListener('click', function(e) {
          e.stopPropagation();
          if (video.muted) {
            video.muted = false;
            muteIcon.innerHTML = '<path d="M11 5L6 9H2v6h4l5 4V5z"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line>';
          } else {
            video.muted = true;
            muteIcon.innerHTML = '<path d="M11 5L6 9H2v6h4l5 4V5z"></path><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line>';
          }
        });
      }

      // Update overlay when video ends
      video.addEventListener('ended', function() {
        overlay.textContent = '▶';
        overlay.classList.remove('playing');
      });

      // Show overlay when video is paused
      video.addEventListener('pause', function() {
        overlay.textContent = '▶';
        overlay.classList.remove('playing');
      });

      // Hide overlay slightly when playing (optional, or keep it visible as pause button)
      video.addEventListener('play', function() {
        overlay.textContent = '⏸';
        overlay.classList.add('playing');
      });
    }
  });

  // Expanding Card Carousel functionality
  function initExpandingCarousel(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const track = container.querySelector('.expanding-carousel-track');
    const dragHandle = container.querySelector('.expanding-carousel-drag-handle');
    const wrappers = container.querySelectorAll('.expanding-card-wrapper');
    const panels = container.querySelectorAll('.expanding-card-panel');

    if (!track || wrappers.length === 0) return;

    let activeIndex = 0;
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    let snapTimeout;
    let mouseLeaveTimeout;

    // Initialize body classes for all cards
    panels.forEach((panel, i) => {
      const body = panel.querySelector('.expanding-card-body');
      if (body) {
        if (i === 0) {
          body.classList.add('expanding-card-body-expanded');
          body.classList.remove('expanding-card-body-collapsed');
        } else {
          body.classList.add('expanding-card-body-collapsed');
          body.classList.remove('expanding-card-body-expanded');
        }
      }
    });

    // Set first card as active initially
    if (panels.length > 0) {
      setActiveCard(0);
    }
    
    // Hover on card to expand it
    wrappers.forEach((wrapper, index) => {
      wrapper.addEventListener('mouseenter', (e) => {
        if (index !== activeIndex) {
          setActiveCard(index);
        }
      });
    });
    
    // Return to first card when mouse leaves the carousel (with debounce to prevent conflicts)
    container.addEventListener('mouseleave', () => {
      // Clear any pending snap operations
      clearTimeout(snapTimeout);
      // Small delay to prevent conflicts with video transitions
      clearTimeout(mouseLeaveTimeout);
      mouseLeaveTimeout = setTimeout(() => {
        if (activeIndex !== 0) {
          setActiveCard(0);
        }
      }, 150);
    });

    function setActiveCard(index) {
      if (index === activeIndex && panels[index].classList.contains('active')) return;
      if (index < 0 || index >= panels.length) return;
      
      // Clear any pending mouseleave timeout when switching cards
      clearTimeout(mouseLeaveTimeout);
      activeIndex = index;
      
      // Update active class on panels and body classes
      panels.forEach((panel, i) => {
        const body = panel.querySelector('.expanding-card-body');
        if (i === index) {
          panel.classList.add('active');
          if (body) {
            body.classList.remove('expanding-card-body-collapsed');
            body.classList.add('expanding-card-body-expanded');
          }
          
          // Start video if it exists in this panel
          const video = panel.querySelector('video');
          if (video) {
            setTimeout(() => {
              const playVideo = () => {
                video.currentTime = 0; // Reset to start
                video.play().catch(e => {
                  console.log('Video autoplay prevented:', e);
                  setTimeout(() => {
                    video.play().catch(err => console.log('Video play failed:', err));
                  }, 500);
                });
              };
              
              if (video.readyState >= 2) {
                // Video is loaded enough to play
                playVideo();
              } else if (video.readyState >= 1) {
                // Video metadata is loaded, try to play
                playVideo();
              } else {
                // Wait for video to load
                const loadedHandler = () => {
                  playVideo();
                };
                video.addEventListener('loadeddata', loadedHandler, { once: true });
                video.addEventListener('canplay', loadedHandler, { once: true });
                video.load();
              }
            }, 200); // Small delay to ensure panel transition is visible
          }
        } else {
          panel.classList.remove('active');
          if (body) {
            body.classList.remove('expanding-card-body-expanded');
            body.classList.add('expanding-card-body-collapsed');
          }
          
          // Pause video if it exists in inactive panel
          const video = panel.querySelector('video');
          if (video) {
            video.pause();
            video.currentTime = 0; // Reset to start
          }
        }
      });
      
      // Snap to card after layout is stable
      debounceSnap(index);
    }
    
    function debounceSnap(index) {
      clearTimeout(snapTimeout);
      snapTimeout = setTimeout(() => {
        requestAnimationFrame(() => {
          requestAnimationFrame(() => {
            snapToCard(index);
          });
        });
      }, 100);
    }
    
    function snapToCard(index) {
      const wrapper = wrappers[index];
      if (!wrapper) return;
      
      const trackPadding = parseInt(getComputedStyle(track).paddingLeft) || 0;
      const targetScroll = wrapper.offsetLeft - trackPadding;
      
      track.scrollTo({
        left: targetScroll,
        behavior: prefersReducedMotion ? 'auto' : 'smooth'
      });
    }

    // Keyboard navigation
    track.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        if (activeIndex > 0) {
          setActiveCard(activeIndex - 1);
        }
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        if (activeIndex < wrappers.length - 1) {
          setActiveCard(activeIndex + 1);
        }
      }
    });

    // Make track focusable for keyboard navigation
    track.setAttribute('tabindex', '0');
  }

  // Initialize expanding carousels
  initExpandingCarousel('expanding-carousel-container-bedrijven');
  initExpandingCarousel('expanding-carousel-container-creators');
  
  // Watch for active panel changes and play videos
  const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
      if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
        const panel = mutation.target;
        if (panel.classList.contains('expanding-card-panel')) {
          const video = panel.querySelector('video');
          if (video) {
            if (panel.classList.contains('active')) {
              // Panel became active, play video
              setTimeout(() => {
                const playVideo = () => {
                  video.currentTime = 0; // Reset to start
                  video.play().catch(e => {
                    console.log('Video autoplay prevented:', e);
                    setTimeout(() => {
                      video.play().catch(err => console.log('Video play failed:', err));
                    }, 500);
                  });
                };
                
                if (video.readyState >= 2) {
                  // Video is loaded enough to play
                  playVideo();
                } else if (video.readyState >= 1) {
                  // Video metadata is loaded, try to play
                  playVideo();
                } else {
                  // Wait for video to load
                  const loadedHandler = () => {
                    playVideo();
                  };
                  video.addEventListener('loadeddata', loadedHandler, { once: true });
                  video.addEventListener('canplay', loadedHandler, { once: true });
                  video.load();
                }
              }, 200); // Small delay to ensure panel transition is visible
            } else {
              // Panel became inactive, pause video
              video.pause();
              video.currentTime = 0; // Reset to start
            }
          }
        }
      }
    });
  });
  
  // Observe all expanding card panels
  document.querySelectorAll('.expanding-card-panel').forEach(panel => {
    observer.observe(panel, { attributes: true, attributeFilter: ['class'] });
  });

  // View switcher functionality
  const switcherButtons = document.querySelectorAll('.view-switcher-btn');
  const bedrijvenContainer = document.getElementById('expanding-carousel-container-bedrijven');
  const creatorsContainer = document.getElementById('expanding-carousel-container-creators');

  switcherButtons.forEach(button => {
    button.addEventListener('click', () => {
      const view = button.getAttribute('data-view');
      
      // Update button states
      switcherButtons.forEach(btn => {
        if (btn === button) {
          btn.classList.add('active');
          btn.style.background = 'var(--color-primary)';
          btn.style.color = 'var(--color-white)';
        } else {
          btn.classList.remove('active');
          btn.style.background = 'transparent';
          btn.style.color = 'var(--color-text-secondary)';
        }
      });

      // Switch containers
      if (view === 'bedrijven') {
        bedrijvenContainer.style.display = 'block';
        creatorsContainer.style.display = 'none';
      } else {
        bedrijvenContainer.style.display = 'none';
        creatorsContainer.style.display = 'block';
      }
    });
  });

  // Notification pop-up animation on scroll
  const notificationsSection = document.getElementById('notifications-section');
  if (notificationsSection) {
    const notificationItems = notificationsSection.querySelectorAll('.notification-item');
    let hasAnimated = false;
    
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !hasAnimated) {
          hasAnimated = true;
          notificationItems.forEach((item, index) => {
            setTimeout(() => {
              item.classList.add('animate');
            }, index * 150);
          });
          observer.unobserve(entry.target);
        }
      });
    }, { 
      threshold: 0.2,
      rootMargin: '0px 0px -50px 0px'
    });

    observer.observe(notificationsSection);
  }

  // Niche filter functionality - update all videos to same video when clicking niche buttons
  const nicheButtons = document.querySelectorAll('.niche-button');
  const creatorVideosGrid = document.getElementById('creator-videos-grid');
  const defaultVideo = 'tech_homepage/Case Study van het merk_ Halsbandje.mp4';

  if (nicheButtons.length > 0 && creatorVideosGrid) {
    nicheButtons.forEach(button => {
      button.addEventListener('click', function() {
        // Remove active class from all buttons
        nicheButtons.forEach(btn => btn.classList.remove('active'));
        // Add active class to clicked button
        this.classList.add('active');

        // Update all videos to the same video
        const videos = creatorVideosGrid.querySelectorAll('.creator-video');
        videos.forEach(video => {
          // Pause current video
          video.pause();
          // Update source
          video.src = defaultVideo;
          // Load new video
          video.load();
        });
      });
    });
  }


});


